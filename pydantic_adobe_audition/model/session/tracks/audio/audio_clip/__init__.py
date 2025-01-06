from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel
from pydantic_adobe_audition.model.session.tracks.audio.audio_clip.channel_map import AudioClipChannelMap
from pydantic_adobe_audition.model.session.tracks.audio.audio_clip.component import TracksAudioTrackAudioClipComponent
from pydantic_adobe_audition.model.session.tracks.audio.audio_clip.edit_parameters import AudioClipEditParameter
from pydantic_adobe_audition.model.session.tracks.audio.audio_clip.effects_rack import AudioClipEffectsRack
from pydantic_adobe_audition.model.session.tracks.audio.audio_clip.properties import AudioClipProperties


class _Fade(BaseSesxModel, __xml_abstract__=True):
    cross_fade_link_type: str = attr(name="crossFadeLinkType")
    end_point: str = attr(name="endPoint")
    shape: str = attr(name="shape")
    start_point: str = attr(name="startPoint")


class FadeIn(_Fade, tag="fadeIn"):
    fade_in_type: str = attr(name="type")


class FadeOut(_Fade, tag="fadeOut"):
    fade_out_type: str = attr(name="type")


class AudioClip(BaseSesxModel, tag="audioClip"):
    clip_auto_crossfade: bool = attr(name="clipAutoCrossfade")
    cross_fade_head_clip_id: int = attr(name="crossFadeHeadClipID")
    cross_fade_tail_clip_id: int = attr(name="crossFadeTailClipID")
    end_point: int = attr(name="endPoint")
    file_id: int = attr(name="fileID")
    hue: str = attr(name="hue")
    id: int = attr(name="id")
    locked_in_time: bool = attr(name="lockedInTime")
    looped: bool = attr(name="looped")
    name: str = attr(name="name")
    offline: bool = attr(name="offline")
    select: bool = attr(name="select")
    source_in_point: int = attr(name="sourceInPoint")
    source_out_point: int = attr(name="sourceOutPoint")
    start_point: int = attr(name="startPoint")
    z_order: int = attr(name="zOrder")
    text: str | None = None
    properties: AudioClipProperties | None = element(default=None)
    effects_rack: AudioClipEffectsRack | None = element(default=None)
    components: list[TracksAudioTrackAudioClipComponent] = element(default_factory=list)
    fade_in: FadeIn = element()
    fade_out: FadeOut = element()
    edit_parameters: list[AudioClipEditParameter] = element(default_factory=list)
    channel_map: AudioClipChannelMap = element()
