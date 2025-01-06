import uuid

from pydantic_xml import BaseXmlModel, attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class BusTrackTrackParameters(BaseSesxModel, tag="trackParameters"):
    track_height: str = attr(name="trackHeight")
    track_hue: str = attr(name="trackHue")
    track_minimized: str = attr(name="trackMinimized")
    name: str = element()


class BusTrackTrackAudioParametersTrackOutput(BaseSesxModel, tag="trackOutput"):
    output_id: str = attr(name="outputID")
    track_output_type: str = attr(name="type")


class BusTrackTrackAudioParametersTrackInput(BaseSesxModel, tag="trackInput"):
    input_id: str = attr(name="inputID")


class TracksBusTrackTrackAudioParametersComponentParameter(BaseXmlModel, tag="parameter"):
    index: int = attr(name="index")
    name: str | None = attr(name="name", default=None)
    parameter_value: str = attr(name="parameterValue")


class TracksBusTrackTrackAudioParametersComponent(BaseSesxModel, tag="component"):
    component_guid: uuid.UUID = attr(name="componentGuid")
    component_id: str = attr(name="componentID")
    id: str = attr(name="id")
    name: str = attr(name="name")
    powered: str = attr(name="powered")
    parameters: list[TracksBusTrackTrackAudioParametersComponentParameter] = element(default_factory=list)


class BusTrackTrackAudioParameters(BaseSesxModel, tag="trackAudioParameters"):
    audio_channel_type: str = attr(name="audioChannelType")
    automation_mode: str = attr(name="automationMode")
    monitoring: str = attr(name="monitoring")
    record_armed: str = attr(name="recordArmed")
    solo: str = attr(name="solo")
    solo_safe: str = attr(name="soloSafe")
    text: str | None = None
    track_output: BusTrackTrackAudioParametersTrackOutput = element()
    track_input: BusTrackTrackAudioParametersTrackInput = element()
    components: list[TracksBusTrackTrackAudioParametersComponent] = element(default_factory=list)


class BusTrackEffectsRackSlotComponentParameter(BaseSesxModel, tag="parameter"):
    index: int = attr(name="index")
    name: str = attr(name="name")
    parameter_value: str = attr(name="parameterValue")


class BusTrackEffectsRackSlotComponent(BaseSesxModel, tag="component"):
    component_guid: uuid.UUID = attr(name="componentGuid")
    component_id: str = attr(name="componentID")
    editor_height: str = attr(name="editorHeight")
    editor_left: str = attr(name="editorLeft")
    editor_top: str = attr(name="editorTop")
    editor_width: str = attr(name="editorWidth")
    name: str = attr(name="name")
    preset_name: str = attr(name="presetName")
    bus_config: str = element(tag="busConfig")
    parameters: list[BusTrackEffectsRackSlotComponentParameter] = element(default_factory=list)


class BusTrackEffectsRackSlot(BaseSesxModel, tag="slot"):
    powered: str = attr(name="powered")
    slot_index: int = attr(name="slotIndex")
    components: list[BusTrackEffectsRackSlotComponent] = element(default_factory=list)


class TracksBusTrackEffectsRackComponentParameter(BaseSesxModel, tag="parameter"):
    index: int = attr(name="index")
    parameter_value: str = attr(name="parameterValue")


class TracksBusTrackEffectsRackComponent(BaseSesxModel, tag="component"):
    component_guid: uuid.UUID = attr(name="componentGuid")
    component_id: str | None = attr(name="componentID", default=None)
    id: str = attr(name="id")
    powered: str = attr(name="powered")
    parameters: list[TracksBusTrackEffectsRackComponentParameter] = element(default_factory=list)


class BusTrackEffectsRack(BaseSesxModel, tag="effectsRack"):
    pre_fader: str = attr(name="preFader")
    components: list[TracksBusTrackEffectsRackComponent] = element(default_factory=list)
    slots: list[BusTrackEffectsRackSlot] = element()


class BusTrackEditParameter(BaseSesxModel, tag="editParameter"):
    parameter_index: int = attr(name="parameterIndex")
    slot_index: int = attr(name="slotIndex")


class BusTrack(BaseSesxModel, tag="busTrack"):
    automation_lane_open_state: str = attr(name="automationLaneOpenState")
    id: int = attr(name="id")
    index: int = attr(name="index")
    select: bool = attr(name="select")
    visible: bool = attr(name="visible")
    track_parameters: BusTrackTrackParameters = element()
    track_audio_parameters: BusTrackTrackAudioParameters = element()
    effects_rack: BusTrackEffectsRack | None = element(default=None)
    edit_parameter: BusTrackEditParameter = element()
