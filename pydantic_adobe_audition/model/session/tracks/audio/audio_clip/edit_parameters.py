from pydantic_xml import attr

from pydantic_adobe_audition.common import BaseSesxModel


class AudioClipEditParameter(BaseSesxModel, tag="editParameter"):
    parameter_index: int = attr(name="parameterIndex")
    slot_index: int = attr(name="slotIndex")
