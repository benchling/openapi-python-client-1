""" A Reference is ultimately a Class which will be in models, usually defined in a body input or return type """

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from .. import utils

class_overrides: Dict[str, Reference] = {}


@dataclass
class Reference:
    """ A reference to a class which will be in models """

    class_name: str
    mixins: Set[str]
    module_name: str

    @staticmethod
    def from_ref(ref: str, mixins: Set[str] = None) -> Reference:
        """ Get a Reference from the openapi #/schemas/blahblah string """
        ref_value = ref.split("/")[-1]
        # ugly hack to avoid stringcase ugly pascalcase output when ref_value isn't snake case
        class_name = utils.pascal_case(ref_value.replace(" ", ""))
        mixins = {utils.pascal_case(mixin.replace(" ", "")) for mixin in (mixins or set())}

        if class_name in class_overrides:
            return class_overrides[class_name]

        return Reference(class_name=class_name, module_name=utils.snake_case(class_name), mixins=mixins)
