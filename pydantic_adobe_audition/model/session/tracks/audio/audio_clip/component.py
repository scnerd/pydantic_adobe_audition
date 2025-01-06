import uuid

from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class TracksAudioTrackAudioClipComponentParameter(BaseSesxModel, tag="parameter"):
    index: int = attr(name="index")
    name: str | None = attr(name="name", default=None)
    parameter_value: str = attr(name="parameterValue")


class TracksAudioTrackAudioClipComponent(BaseSesxModel, tag="component"):
    component_guid: uuid.UUID = attr(name="componentGuid")
    component_id: str = attr(name="componentID")
    id: str = attr(name="id")
    name: str = attr(name="name")
    powered: bool = attr(name="powered")
    parameters: list[TracksAudioTrackAudioClipComponentParameter] = element()
