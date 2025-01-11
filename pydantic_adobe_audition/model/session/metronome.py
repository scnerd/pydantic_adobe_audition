"""Top-level metronome configuration."""

from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel
from pydantic_adobe_audition.model.session.tracks.metronome import MetronomeTrack


class Metronome(BaseSesxModel, tag="metronome"):
    enabled: bool = attr(name="enabled")
    pattern: str = attr(name="pattern")
    sound_set: str = attr(name="soundSet")
    metronome_track: MetronomeTrack = element()
