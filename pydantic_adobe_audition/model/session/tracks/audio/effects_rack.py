import uuid

from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class TracksAudioTrackEffectsRackComponentParameter(BaseSesxModel, tag="parameter"):
    index: int = attr(name="index")
    parameter_value: str = attr(name="parameterValue")


class TracksAudioTrackEffectsRackComponent(BaseSesxModel, tag="component"):
    component_guid: uuid.UUID = attr(name="componentGuid")
    component_id: str | None = attr(name="componentID", default=None)
    id: int = attr(name="id")
    powered: str = attr(name="powered")
    text: str | None = None
    parameters: list[TracksAudioTrackEffectsRackComponentParameter] = element()


class ComponentChannelMapChannel(BaseSesxModel, tag="channel"):
    index: int = attr(name="index")
    source_index: int = attr(name="sourceIndex")


class ComponentChannelMap(BaseSesxModel, tag="channelMap"):
    direction: str = attr(name="direction")
    text: str | None = None
    channels: list[ComponentChannelMapChannel] = element(tag="channel")


class AudioTrackEffectsRackSlotComponentParameter(BaseSesxModel, tag="parameter"):
    index: int = attr(name="index")
    name: str = attr(name="name")
    parameter_value: str = attr(name="parameterValue")


class AudioTrackEffectsRackSlotComponent(BaseSesxModel, tag="component"):
    component_guid: uuid.UUID = attr(name="componentGuid")
    component_id: str = attr(name="componentID")
    name: str = attr(name="name")
    preset_name: str = attr(name="presetName")
    text: str | None = None
    bus_config: str = element(tag="busConfig")
    channel_map: ComponentChannelMap = element()
    parameters: list[AudioTrackEffectsRackSlotComponentParameter] = element()


class AudioTrackEffectsRackSlot(BaseSesxModel, tag="slot"):
    powered: str = attr(name="powered")
    slot_index: int = attr(name="slotIndex")
    text: str | None = None
    components: list[AudioTrackEffectsRackSlotComponent] = element()


class AudioTrackEffectsRack(BaseSesxModel, tag="effectsRack"):
    pre_fader: str = attr(name="preFader")
    components: list[TracksAudioTrackEffectsRackComponent] = element()
    slots: list[AudioTrackEffectsRackSlot] = element()
