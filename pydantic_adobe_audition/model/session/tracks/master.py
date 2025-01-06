import uuid

from pydantic_xml import BaseXmlModel, attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class MasterTrackTrackParameters(BaseSesxModel, tag="trackParameters"):
    track_height: str = attr(name="trackHeight")
    track_hue: str = attr(name="trackHue")
    track_minimized: str = attr(name="trackMinimized")
    text: str | None = None
    name: str = element()


class MasterTrackTrackAudioParametersTrackOutput(BaseSesxModel, tag="trackOutput"):
    output_id: str = attr(name="outputID")
    track_output_type: str = attr(name="type")


class MasterTrackTrackAudioParametersTrackInput(BaseSesxModel, tag="trackInput"):
    input_id: str = attr(name="inputID")


class TracksMasterTrackTrackAudioParametersComponentParameter(BaseXmlModel, tag="parameter"):
    index: int = attr(name="index")
    name: str | None = attr(name="name", default=None)
    parameter_value: str = attr(name="parameterValue")


class TracksMasterTrackTrackAudioParametersComponent(BaseSesxModel, tag="component"):
    component_guid: uuid.UUID = attr(name="componentGuid")
    component_id: str = attr(name="componentID")
    id: str = attr(name="id")
    name: str = attr(name="name")
    powered: str = attr(name="powered")
    text: str | None = None
    parameters: list[TracksMasterTrackTrackAudioParametersComponentParameter] = element(default_factory=list)


class MasterTrackTrackAudioParameters(BaseSesxModel, tag="trackAudioParameters"):
    audio_channel_type: str = attr(name="audioChannelType")
    automation_mode: str = attr(name="automationMode")
    monitoring: str = attr(name="monitoring")
    record_armed: str = attr(name="recordArmed")
    solo: str = attr(name="solo")
    solo_safe: str = attr(name="soloSafe")
    text: str | None = None
    track_output: MasterTrackTrackAudioParametersTrackOutput = element()
    track_input: MasterTrackTrackAudioParametersTrackInput = element()
    components: list[TracksMasterTrackTrackAudioParametersComponent] = element(default_factory=list)


class MasterTrackEditParameter(BaseSesxModel, tag="editParameter"):
    parameter_index: int = attr(name="parameterIndex")
    slot_index: int = attr(name="slotIndex")


class MasterTrack(BaseSesxModel, tag="masterTrack"):
    automation_lane_open_state: str = attr(name="automationLaneOpenState")
    id: int = attr(name="id")
    index: int = attr(name="index")
    select: bool = attr(name="select")
    visible: bool = attr(name="visible")
    text: str | None = None
    track_parameters: MasterTrackTrackParameters = element()
    track_audio_parameters: MasterTrackTrackAudioParameters = element()
    edit_parameter: MasterTrackEditParameter = element()
