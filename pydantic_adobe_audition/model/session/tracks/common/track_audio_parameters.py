from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel
from pydantic_adobe_audition.model.session.tracks.common.component import Component


class TrackAudioParametersTrackOutput(BaseSesxModel, tag="trackOutput"):
    output_id: str = attr(name="outputID")
    track_output_type: str = attr(name="type")


class TrackAudioParametersTrackInput(BaseSesxModel, tag="trackInput"):
    input_id: str = attr(name="inputID")


class TrackAudioParameters(BaseSesxModel, tag="trackAudioParameters"):
    audio_channel_type: str = attr(name="audioChannelType")
    automation_mode: str = attr(name="automationMode")
    monitoring: bool = attr(name="monitoring")
    record_armed: bool = attr(name="recordArmed")
    solo: bool = attr(name="solo")
    solo_safe: bool = attr(name="soloSafe")
    track_output: TrackAudioParametersTrackOutput = element()
    track_input: TrackAudioParametersTrackInput = element()
    components: list[Component] = element(default_factory=list)
