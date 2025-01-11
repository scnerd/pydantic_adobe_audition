import uuid

from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel
from pydantic_adobe_audition.model.common.channel_map import ChannelMap
from pydantic_adobe_audition.model.session.tracks.common.component import Component


class ParameterKeyframe(BaseSesxModel, tag="parameterKeyframe"):
    sample_offset: str = attr(name="sampleOffset")
    select: bool = attr(name="select")
    parameter_keyframe_type: str = attr(name="type")
    value: str = attr(name="value")


class ParameterKeyframes(BaseSesxModel, tag="parameterKeyframes"):
    enable_splines: bool = attr(name="enableSplines")
    read_only: bool = attr(name="readOnly")
    parameter_keyframe: list[ParameterKeyframe] = element(tag="parameterKeyframe", default_factory=list)


class EffectsRackSlotComponentParameter(BaseSesxModel, tag="parameter"):
    index: int = attr(name="index")
    name: str = attr(name="name")
    parameter_value: str = attr(name="parameterValue")
    parameter_keyframes: ParameterKeyframes | None = element(tag="parameterKeyframes", default=None)


class EffectsRackSlotComponent(BaseSesxModel, tag="component"):
    component_guid: uuid.UUID = attr(name="componentGuid")
    component_id: str = attr(name="componentID")
    editor_height: int | None = attr(name="editorHeight", default=None)
    editor_left: int | None = attr(name="editorLeft", default=None)
    editor_top: int | None = attr(name="editorTop", default=None)
    editor_width: int | None = attr(name="editorWidth", default=None)
    name: str = attr(name="name")
    preset_name: str = attr(name="presetName")
    bus_config: str = element(tag="busConfig")
    channel_map: ChannelMap | None = element(default=None)
    parameters: list[EffectsRackSlotComponentParameter] = element(default_factory=list)

    @property
    def bus_config_dict(self):
        import json

        return json.loads(self.bus_config) if self.bus_config else None


class EffectsRackSlot(BaseSesxModel, tag="slot"):
    powered: bool = attr(name="powered")
    slot_index: int = attr(name="slotIndex")
    components: list[EffectsRackSlotComponent] = element()


class EffectsRack(BaseSesxModel, tag="effectsRack"):
    pre_fader: str = attr(name="preFader")
    components: list[Component] = element(default_factory=list)
    slots: list[EffectsRackSlot] = element(default_factory=list)
