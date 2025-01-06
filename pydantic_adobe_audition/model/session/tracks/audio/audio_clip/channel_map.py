from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class AudioClipChannelMapChannel(BaseSesxModel, tag="channel"):
    index: int = attr(name="index")
    source_index: int = attr(name="sourceIndex")


class AudioClipChannelMap(BaseSesxModel, tag="channelMap"):
    text: str | None = None
    channels: list[AudioClipChannelMapChannel] = element(tag="channel")
