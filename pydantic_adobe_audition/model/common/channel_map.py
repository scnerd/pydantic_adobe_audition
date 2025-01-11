from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class ChannelMapChannel(BaseSesxModel, tag="channel"):
    index: int = attr(name="index")
    source_index: int = attr(name="sourceIndex")


class ChannelMap(BaseSesxModel, tag="channelMap"):
    direction: str | None = attr(name="direction", default=None)
    channels: list[ChannelMapChannel] = element()
