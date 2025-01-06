from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class Property(BaseSesxModel, tag="property"):
    key: str = attr(name="key")
    text: str | None = None


class SessionProperties(BaseSesxModel, tag="properties"):
    text: str | None = None
    properties: list[Property] = element(tag="property", default_factory=list)
