from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel
from pydantic_adobe_audition.model.session.tracks.audio.audio_clip import AudioClip
from pydantic_adobe_audition.model.session.tracks.audio.edit_parameters import AudioTrackEditParameter
from pydantic_adobe_audition.model.session.tracks.audio.effects_rack import AudioTrackEffectsRack
from pydantic_adobe_audition.model.session.tracks.audio.track_audio_parameters import AudioTrackTrackAudioParameters
from pydantic_adobe_audition.model.session.tracks.audio.track_parameters import AudioTrackTrackParameters


class AudioTrack(BaseSesxModel, tag="audioTrack"):
    automation_lane_open_state: str = attr(name="automationLaneOpenState")
    id: int = attr(name="id")
    index: int = attr(name="index")
    select: bool = attr(name="select")
    visible: bool = attr(name="visible")
    text: str | None = None
    effects_rack: AudioTrackEffectsRack | None = element(default=None)
    track_parameters: AudioTrackTrackParameters = element()
    track_audio_parameters: AudioTrackTrackAudioParameters = element()
    edit_parameter: AudioTrackEditParameter = element()
    clips: list[AudioClip] = element(default_factory=list)
