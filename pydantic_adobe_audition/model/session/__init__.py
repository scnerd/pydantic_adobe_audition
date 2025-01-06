"""Contains data about the multi-track session, apart from external dependencies."""

from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel
from pydantic_adobe_audition.model.session.clip_groups import ClipGroups
from pydantic_adobe_audition.model.session.metronome import Metronome
from pydantic_adobe_audition.model.session.properties import SessionProperties
from pydantic_adobe_audition.model.session.state import SessionState
from pydantic_adobe_audition.model.session.tracks import Tracks


class Session(BaseSesxModel, tag="session"):
    app_build: str = attr(name="appBuild")
    app_version: str = attr(name="appVersion")
    audio_channel_type: str = attr(name="audioChannelType")
    bit_depth: str = attr(name="bitDepth")
    duration: str = attr(name="duration")
    sample_rate: int = attr(name="sampleRate")
    text: str | None = None
    tracks: Tracks = element()
    session_state: SessionState = element(tag="sessionState")
    xmp_metadata: str = element(tag="xmpMetadata")
    clip_groups: ClipGroups = element(tag="clipGroups")
    metronome: Metronome = element()
    properties: SessionProperties = element()
