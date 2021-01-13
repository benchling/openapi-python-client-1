from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING, ClassVar, Dict, List, Set, Union

import attr

from ... import schema as oai
from ..errors import PropertyError
from ..reference import Reference
from .property import Property

if TYPE_CHECKING:
    from .schemas import Schemas


@attr.s(auto_attribs=True, frozen=True)
class ModelProperty(Property):
    """ A property which refers to another Schema """

    reference: Reference
    references: List[oai.Reference]
    required_properties: List[Property]
    optional_properties: List[Property]
    description: str
    relative_imports: Set[str]
    additional_properties: Union[bool, Property]

    template: ClassVar[str] = "model_property.pyi"

    def resolve_references(
        self, components: Dict[str, Union[oai.Reference, oai.Schema]], schemas: Schemas
    ) -> Union[Schemas, PropertyError]:
        from ..properties import property_from_data

        required_set = set()
        props = {}
        while self.references:
            reference = self.references.pop()
            source_name = Reference.from_ref(reference.ref).class_name
            referenced_prop = components[source_name]
            assert isinstance(referenced_prop, oai.Schema)
            for p, val in (referenced_prop.properties or {}).items():
                props[p] = (val, source_name)
            for sub_prop in referenced_prop.allOf or []:
                if isinstance(sub_prop, oai.Reference):
                    self.references.append(sub_prop)
                else:
                    for p, val in (sub_prop.properties or {}).items():
                        props[p] = (val, source_name)
            if isinstance(referenced_prop.required, Iterable):
                for sub_prop_name in referenced_prop.required:
                    required_set.add(sub_prop_name)

        for key, (value, source_name) in (props or {}).items():
            required = key in required_set
            prop, schemas = property_from_data(
                name=key, required=required, data=value, schemas=schemas, parent_name=source_name
            )
            if isinstance(prop, PropertyError):
                return prop
            if isinstance(prop, ModelProperty):
                prop.resolve_references(components, schemas)
            if required:
                self.required_properties.append(prop)
                # Remove the optional version
                new_optional_props = [op for op in self.optional_properties if op.name != prop.name]
                self.optional_properties.clear()
                self.optional_properties.extend(new_optional_props)
            elif not any(ep for ep in (self.optional_properties + self.required_properties) if ep.name == prop.name):
                self.optional_properties.append(prop)
            self.relative_imports.update(prop.get_imports(prefix=".."))

        return schemas

    def get_type_string(self, no_optional: bool = False) -> str:
        """ Get a string representation of type that should be used when declaring this property """
        type_string = self.reference.class_name
        if no_optional:
            return type_string
        if self.nullable:
            type_string = f"Optional[{type_string}]"
        if not self.required:
            type_string = f"Union[{type_string}, Unset]"
        return type_string

    def get_imports(self, *, prefix: str) -> Set[str]:
        """
        Get a set of import strings that should be included when this property is used somewhere

        Args:
            prefix: A prefix to put before any relative (local) module names. This should be the number of . to get
            back to the root of the generated client.
        """
        imports = super().get_imports(prefix=prefix)
        imports.update(
            {
                f"from {prefix}models.{self.reference.module_name} import {self.reference.class_name}",
                "from typing import Dict",
                "from typing import cast",
            }
        )
        return imports
