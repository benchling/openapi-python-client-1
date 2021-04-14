from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ModelFromAllOf")


@attr.s(auto_attribs=True)
class ModelFromAllOf:
    """  """

    a_sub_property: Union[Unset, str] = UNSET
    another_sub_property: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        a_sub_property = self.a_sub_property
        another_sub_property = self.another_sub_property

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if a_sub_property is not UNSET:
            field_dict["a_sub_property"] = a_sub_property
        if another_sub_property is not UNSET:
            field_dict["another_sub_property"] = another_sub_property

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        a_sub_property = d.pop("a_sub_property", UNSET)

        another_sub_property = d.pop("another_sub_property", UNSET)

        model_from_all_of = cls(
            a_sub_property=a_sub_property,
            another_sub_property=another_sub_property,
        )

        return model_from_all_of
