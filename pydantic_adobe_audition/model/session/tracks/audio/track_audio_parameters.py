import uuid

from pydantic_xml import BaseXmlModel, attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class AudioTrackTrackAudioParametersTrackOutput(BaseSesxModel, tag="trackOutput"):
    output_id: str = attr(name="outputID")
    track_output_type: str = attr(name="type")


class AudioTrackTrackAudioParametersTrackInput(BaseSesxModel, tag="trackInput"):
    input_id: str = attr(name="inputID")


class TracksAudioTrackTrackAudioParametersComponentParameter(BaseXmlModel, tag="parameter"):
    index: int = attr(name="index")
    name: str | None = attr(name="name", default=None)
    parameter_value: str = attr(name="parameterValue")


class TracksAudioTrackTrackAudioParametersComponent(BaseSesxModel, tag="component"):
    component_guid: uuid.UUID = attr(name="componentGuid")
    component_id: str = attr(name="componentID")
    id: str = attr(name="id")
    name: str = attr(name="name")
    powered: str = attr(name="powered")
    text: str | None = None
    parameters: list[TracksAudioTrackTrackAudioParametersComponentParameter] = element(tag="parameter")


class AudioTrackTrackAudioParameters(BaseSesxModel, tag="trackAudioParameters"):
    audio_channel_type: str = attr(name="audioChannelType")
    automation_mode: str = attr(name="automationMode")
    monitoring: str = attr(name="monitoring")
    record_armed: str = attr(name="recordArmed")
    solo: str = attr(name="solo")
    solo_safe: str = attr(name="soloSafe")
    text: str | None = None
    track_output: AudioTrackTrackAudioParametersTrackOutput = element()
    track_input: AudioTrackTrackAudioParametersTrackInput = element()
    components: list[TracksAudioTrackTrackAudioParametersComponent] = element()
