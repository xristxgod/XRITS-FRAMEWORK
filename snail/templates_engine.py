import os
import re
from typing import Dict

from .requests import Request


FOR_BLOCK_PATTERN = re.compile(
    r'{% for (?P<variable>[a-zA-Z]+) in (?P<seq>[a-zA-Z]+) %}(?P<content>[\S\s]+)(?={% endblock %}){% endblock %}'
)
VARIABLE_PATTERN = re.compile(r'{{ (?P<variable>[a-zA-Z_]+) }}')


class Engine:

    def __init__(self, base_dir: str, template_dir: str):
        self.template_dir = os.path.join(base_dir, template_dir)

    def _get_template_as_string(self, template_name: str):
        template_path = os.path.join(self.template_dir, template_name)
        if not os.path.isfile(template_path):
            raise Exception(f"{template_path} is not file")
        with open(template_path) as template:
            return template.read()

    @staticmethod
    def _build_block(context: Dict, raw_template_block: str) -> str:
        used_vars = VARIABLE_PATTERN.findall(raw_template_block)
        if used_vars is None:
            return raw_template_block
        for var in used_vars:
            var_in_template = "{{ %s }}" % var
            raw_template_block = re.sub(
                var_in_template, str(context.get(var, '')), raw_template_block
            )
        return raw_template_block

    def _build_for_block(self, context: Dict, raw_template: str) -> str:
        for_block = FOR_BLOCK_PATTERN.search(raw_template)
        if for_block is None:
            return raw_template
        build_for_block = ""
        for i in context.get(for_block.group("seq"), []):
            build_for_block += self._build_block(
                {**context, for_block.group("variable"): i},
                for_block.group("content")
            )
        return FOR_BLOCK_PATTERN.sub(build_for_block, raw_template)

    def build(self, context: Dict, template_name: str) -> str:
        raw_template: str = self._get_template_as_string(template_name)
        raw_template: str = self._build_for_block(context, raw_template)
        return self._build_block(context, raw_template)


def build_template(request: Request, context: Dict, template_name: str):
    return Engine(
        request.settings.get("BASE_DIR"),
        request.settings.get("TEMPLATE_DIR_NAME")
    ).build(context, template_name)


__all__ = [
    "Engine"
]
