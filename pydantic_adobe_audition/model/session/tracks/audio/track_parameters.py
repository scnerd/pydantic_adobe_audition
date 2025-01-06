from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class AudioTrackTrackParameters(BaseSesxModel, tag="trackParameters"):
    track_height: str = attr(name="trackHeight")
    track_hue: str = attr(name="trackHue")
    track_minimized: bool = attr(name="trackMinimized")
    text: str | None = None
    name: str = element()
