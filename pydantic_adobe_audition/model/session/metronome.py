"""Top-level metronome configuration."""

import uuid

from pydantic_xml import BaseXmlModel, attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class MetronomeTrackTrackParameters(BaseSesxModel, tag="trackParameters"):
    track_height: str = attr(name="trackHeight")
    track_hue: str = attr(name="trackHue")
    track_minimized: str = attr(name="trackMinimized")
    text: str | None = None
    name: str = element()


class MetronomeTrackTrackAudioParametersTrackOutput(BaseSesxModel, tag="trackOutput"):
    output_id: str = attr(name="outputID")
    track_output_type: str = attr(name="type")


class MetronomeTrackTrackAudioParametersTrackInput(BaseSesxModel, tag="trackInput"):
    input_id: str = attr(name="inputID")


class MetronomeMetronomeTrackTrackAudioParametersComponentParameter(BaseXmlModel, tag="parameter"):
    """
    Represents a component parameter within the metronome track's audio parameters.
    """

    index: int = attr(name="index")
    name: str | None = attr(name="name", default=None)
    parameter_value: str = attr(name="parameterValue")


class MetronomeMetronomeTrackTrackAudioParametersComponent(BaseXmlModel, tag="component"):
    component_guid: uuid.UUID = attr(name="componentGuid")
    component_id: str = attr(name="componentID")
    id: str = attr(name="id")
    name: str = attr(name="name")
    powered: str = attr(name="powered")
    text: str | None = None
    parameters: list[MetronomeMetronomeTrackTrackAudioParametersComponentParameter] = element(default_factory=list)


class MetronomeTrackEditParameter(BaseSesxModel, tag="editParameter"):
    parameter_index: int = attr(name="parameterIndex")
    slot_index: int = attr(name="slotIndex")


class MetronomeTrackTrackAudioParameters(BaseXmlModel, tag="trackAudioParameters"):
    audio_channel_type: str = attr(name="audioChannelType")
    automation_mode: str = attr(name="automationMode")
    monitoring: str = attr(name="monitoring")
    record_armed: str = attr(name="recordArmed")
    solo: str = attr(name="solo")
    solo_safe: str = attr(name="soloSafe")
    text: str | None = None
    track_output: MetronomeTrackTrackAudioParametersTrackOutput = element()
    track_input: MetronomeTrackTrackAudioParametersTrackInput = element()
    components: list[MetronomeMetronomeTrackTrackAudioParametersComponent] = element(default_factory=list)


class MetronomeTrack(BaseSesxModel, tag="metronomeTrack"):
    automation_lane_open_state: str = attr(name="automationLaneOpenState")
    id: int = attr(name="id")
    index: int = attr(name="index")
    select: bool = attr(name="select")
    visible: bool = attr(name="visible")
    text: str | None = None
    track_parameters: MetronomeTrackTrackParameters = element(name="trackParameters")
    track_audio_parameters: MetronomeTrackTrackAudioParameters = element(name="trackAudioParameters")
    edit_parameter: MetronomeTrackEditParameter = element(name="editParameter")


class Metronome(BaseSesxModel, tag="metronome"):
    enabled: str = attr(name="enabled")
    pattern: str = attr(name="pattern")
    sound_set: str = attr(name="soundSet")
    text: str | None = None
    metronome_track: MetronomeTrack = element()
