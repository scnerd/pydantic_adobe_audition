from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel
from pydantic_adobe_audition.model.common.channel_map import ChannelMap
from pydantic_adobe_audition.model.common.edit_parameter import EditParameter
from pydantic_adobe_audition.model.session.tracks.audio.audio_clip.fade import FadeIn, FadeOut
from pydantic_adobe_audition.model.session.tracks.audio.audio_clip.properties import AudioClipProperties
from pydantic_adobe_audition.model.session.tracks.common.component import Component
from pydantic_adobe_audition.model.session.tracks.common.effects_rack import EffectsRack


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
    properties: AudioClipProperties | None = element(default=None)
    effects_rack: EffectsRack | None = element(default=None)
    components: list[Component] = element(default_factory=list)
    fade_in: FadeIn = element()
    fade_out: FadeOut = element()
    edit_parameters: list[EditParameter] = element(default_factory=list)
    channel_map: ChannelMap = element()
