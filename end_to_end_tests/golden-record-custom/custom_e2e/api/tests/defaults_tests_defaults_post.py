from typing import Optional

import httpx

from ...types import Response

Client = httpx.Client

import datetime
from typing import Dict, List, Optional, Union

from dateutil.parser import isoparse

from ...models.an_enum import AnEnum
from ...models.http_validation_error import HTTPValidationError
from ...models.model_with_union_property import ModelWithUnionProperty
from ...types import UNSET, Unset


def _parse_response(*, response: httpx.Response) -> Optional[Union[None, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = None

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[None, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def httpx_request(
    *,
    client: Client,
    string_prop: Union[Unset, None, str] = "the default string",
    not_required_not_nullable_datetime_prop: Union[Unset, None, datetime.datetime] = isoparse("1010-10-10T00:00:00"),
    not_required_nullable_datetime_prop: Union[Unset, None, datetime.datetime] = isoparse("1010-10-10T00:00:00"),
    required_not_nullable_datetime_prop: datetime.datetime = isoparse("1010-10-10T00:00:00"),
    required_nullable_datetime_prop: Optional[datetime.datetime] = isoparse("1010-10-10T00:00:00"),
    date_prop: Union[Unset, None, datetime.date] = isoparse("1010-10-10").date(),
    float_prop: Union[Unset, None, float] = 3.14,
    int_prop: Union[Unset, None, int] = 7,
    boolean_prop: Union[Unset, None, bool] = False,
    list_prop: Union[Unset, None, List[AnEnum]] = UNSET,
    union_prop: Union[Unset, None, float, str] = "not a float",
    union_prop_with_ref: Union[Unset, None, float, AnEnum] = 0.6,
    enum_prop: Union[Unset, None, AnEnum] = UNSET,
    model_prop: Union[Unset, None, ModelWithUnionProperty] = UNSET,
) -> Response[Union[None, HTTPValidationError]]:

    json_not_required_not_nullable_datetime_prop: Union[Unset, None, str] = UNSET
    if not isinstance(not_required_not_nullable_datetime_prop, Unset):
        json_not_required_not_nullable_datetime_prop = (
            not_required_not_nullable_datetime_prop.isoformat() if not_required_not_nullable_datetime_prop else None
        )

    json_not_required_nullable_datetime_prop: Union[Unset, None, str] = UNSET
    if not isinstance(not_required_nullable_datetime_prop, Unset):
        json_not_required_nullable_datetime_prop = (
            not_required_nullable_datetime_prop.isoformat() if not_required_nullable_datetime_prop else None
        )

    json_required_not_nullable_datetime_prop = required_not_nullable_datetime_prop.isoformat()

    json_required_nullable_datetime_prop = (
        required_nullable_datetime_prop.isoformat() if required_nullable_datetime_prop else None
    )

    json_date_prop: Union[Unset, None, str] = UNSET
    if not isinstance(date_prop, Unset):
        json_date_prop = date_prop.isoformat() if date_prop else None

    json_list_prop: Union[Unset, None, List[Any]] = UNSET
    if not isinstance(list_prop, Unset):
        if list_prop is None:
            json_list_prop = None
        else:
            json_list_prop = []
            for list_prop_item_data in list_prop:
                list_prop_item = list_prop_item_data.value

                json_list_prop.append(list_prop_item)

    json_union_prop: Union[Unset, None, float, str]
    if isinstance(union_prop, Unset):
        json_union_prop = UNSET
    elif union_prop is None:
        json_union_prop = None
    else:
        json_union_prop = union_prop

    json_union_prop_with_ref: Union[Unset, None, float, int]
    if isinstance(union_prop_with_ref, Unset):
        json_union_prop_with_ref = UNSET
    elif union_prop_with_ref is None:
        json_union_prop_with_ref = None
    elif isinstance(union_prop_with_ref, AnEnum):
        json_union_prop_with_ref = UNSET
        if not isinstance(union_prop_with_ref, Unset):
            json_union_prop_with_ref = union_prop_with_ref.value

    else:
        json_union_prop_with_ref = union_prop_with_ref

    json_enum_prop: Union[Unset, None, int] = UNSET
    if not isinstance(enum_prop, Unset):
        json_enum_prop = enum_prop.value if enum_prop else None

    json_model_prop: Union[Unset, None, Dict[str, Any]] = UNSET
    if not isinstance(model_prop, Unset):
        json_model_prop = model_prop.to_dict() if model_prop else None

    params: Dict[str, Any] = {
        "required_not_nullable_datetime_prop": json_required_not_nullable_datetime_prop,
    }
    if not isinstance(string_prop, Unset) and string_prop is not None:
        params["string_prop"] = string_prop
    if (
        not isinstance(json_not_required_not_nullable_datetime_prop, Unset)
        and json_not_required_not_nullable_datetime_prop is not None
    ):
        params["not_required_not_nullable_datetime_prop"] = json_not_required_not_nullable_datetime_prop
    if (
        not isinstance(json_not_required_nullable_datetime_prop, Unset)
        and json_not_required_nullable_datetime_prop is not None
    ):
        params["not_required_nullable_datetime_prop"] = json_not_required_nullable_datetime_prop
    if json_required_nullable_datetime_prop is not None:
        params["required_nullable_datetime_prop"] = json_required_nullable_datetime_prop
    if not isinstance(json_date_prop, Unset) and json_date_prop is not None:
        params["date_prop"] = json_date_prop
    if not isinstance(float_prop, Unset) and float_prop is not None:
        params["float_prop"] = float_prop
    if not isinstance(int_prop, Unset) and int_prop is not None:
        params["int_prop"] = int_prop
    if not isinstance(boolean_prop, Unset) and boolean_prop is not None:
        params["boolean_prop"] = boolean_prop
    if not isinstance(json_list_prop, Unset) and json_list_prop is not None:
        params["list_prop"] = json_list_prop
    if not isinstance(json_union_prop, Unset) and json_union_prop is not None:
        params["union_prop"] = json_union_prop
    if not isinstance(json_union_prop_with_ref, Unset) and json_union_prop_with_ref is not None:
        params["union_prop_with_ref"] = json_union_prop_with_ref
    if not isinstance(json_enum_prop, Unset) and json_enum_prop is not None:
        params["enum_prop"] = json_enum_prop
    if not isinstance(json_model_prop, Unset) and json_model_prop is not None:
        params.update(json_model_prop)

    response = client.request(
        "post",
        "/tests/defaults",
        params=params,
    )

    return _build_response(response=response)
