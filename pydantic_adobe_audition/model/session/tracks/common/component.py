import uuid

from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class ComponentParameter(BaseSesxModel, tag="parameter"):
    index: int = attr(name="index")
    name: str | None = attr(name="name", default=None)
    parameter_value: str = attr(name="parameterValue")


class Component(BaseSesxModel, tag="component"):
    component_guid: uuid.UUID = attr(name="componentGuid")
    component_id: str | None = attr(name="componentID", default=None)
    id: str = attr(name="id")
    name: str | None = attr(name="name", default=None)
    powered: bool = attr(name="powered")
    parameters: list[ComponentParameter] = element(default_factory=list)
