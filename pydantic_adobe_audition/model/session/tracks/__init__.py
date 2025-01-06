"""Structures for each track in the multi-track session."""

from pydantic_xml import element

from pydantic_adobe_audition.common import BaseSesxModel
from pydantic_adobe_audition.model.session.tracks.audio import AudioTrack
from pydantic_adobe_audition.model.session.tracks.bus import BusTrack
from pydantic_adobe_audition.model.session.tracks.master import MasterTrack


class Tracks(BaseSesxModel, tag="tracks"):
    text: str | None = None
    audio_tracks: list[AudioTrack] = element(tag="audioTrack", default_factory=list)
    bus_tracks: list[BusTrack] = element(tag="busTrack", default_factory=list)
    master_tracks: list[MasterTrack] = element(tag="masterTrack", default_factory=list)
