from pydantic_xml import element

from pydantic_adobe_audition.model.session.tracks.common import BaseTrack
from pydantic_adobe_audition.model.session.tracks.common.effects_rack import EffectsRack


class BusTrack(BaseTrack, tag="busTrack"):
    effects_rack: EffectsRack | None = element(default=None)
