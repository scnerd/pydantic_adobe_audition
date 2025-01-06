import uuid
from collections import defaultdict
from typing import Any

from pydantic import ConfigDict
from pydantic_xml import BaseXmlModel


class BaseSesxModel(BaseXmlModel, __xml_abstract__=True):
    model_config = ConfigDict(extra="forbid")

    __xml_field_serializers__ = defaultdict(str)

    def to_xml(
        self,
        *,
        exclude_unset: bool = True,
        **kwargs: Any,
    ) -> str | bytes:
        return super().to_xml(exclude_unset=exclude_unset, **kwargs)


def lowercase_uuid_serializer(v: uuid.UUID, _handler, _info) -> str:
    return str(v).lower()


def uppercase_uuid_serializer(v: uuid.UUID, _handler, _info) -> str:
    return str(v).upper()
