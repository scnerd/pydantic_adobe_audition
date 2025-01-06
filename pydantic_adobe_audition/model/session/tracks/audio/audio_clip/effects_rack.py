import uuid

from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class AudioTrackAudioClipEffectsRackComponentParameter(BaseSesxModel, tag="parameter"):
    index: int = attr(name="index")
    parameter_value: str = attr(name="parameterValue")


class AudioTrackAudioClipEffectsRackComponent(BaseSesxModel, tag="component"):
    component_guid: uuid.UUID = attr(name="componentGuid")
    component_id: str | None = attr(name="componentID", default=None)
    id: str = attr(name="id")
    powered: str = attr(name="powered")
    text: str | None = None
    parameters: list[AudioTrackAudioClipEffectsRackComponentParameter] = element(tag="parameter")


class ParameterKeyframe(BaseSesxModel, tag="parameterKeyframe"):
    sample_offset: str = attr(name="sampleOffset")
    select: bool = attr(name="select")
    parameter_keyframe_type: str = attr(name="type")
    value: str = attr(name="value")


class ParameterKeyframes(BaseSesxModel, tag="parameterKeyframes"):
    enable_splines: str = attr(name="enableSplines")
    read_only: str = attr(name="readOnly")
    text: str | None = None
    parameter_keyframe: ParameterKeyframe = element(tag="parameterKeyframe")


class AudioClipEffectsRackSlotComponentParameter(BaseSesxModel, tag="parameter"):
    index: int = attr(name="index")
    name: str = attr(name="name")
    parameter_value: str = attr(name="parameterValue")
    # text: str | None = None
    parameter_keyframes: ParameterKeyframes | None = element(tag="parameterKeyframes", default=None)


class AudioClipEffectsRackSlotComponent(BaseSesxModel, tag="component"):
    component_guid: uuid.UUID = attr(name="componentGuid")
    component_id: str = attr(name="componentID")
    name: str = attr(name="name")
    preset_name: str = attr(name="presetName")
    # text: str | None = None
    bus_config: str = element(tag="busConfig")
    parameters: list[AudioClipEffectsRackSlotComponentParameter] = element()


class AudioClipEffectsRackSlot(BaseSesxModel, tag="slot"):
    powered: str = attr(name="powered")
    slot_index: int = attr(name="slotIndex")
    # text: str | None = None
    components: list[AudioClipEffectsRackSlotComponent] = element(default_factory=list)


class AudioClipEffectsRack(BaseSesxModel, tag="effectsRack"):
    pre_fader: str = attr(name="preFader")
    # text: str | None = None
    components: list[AudioTrackAudioClipEffectsRackComponent] = element(default_factory=list)
    slot: AudioClipEffectsRackSlot = element()
