from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel
from pydantic_adobe_audition.model.common.edit_parameter import EditParameter
from pydantic_adobe_audition.model.session.tracks.common.track_audio_parameters import TrackAudioParameters
from pydantic_adobe_audition.model.session.tracks.common.track_parameters import TrackParameters


class BaseTrack(BaseSesxModel, __xml_abstract__=True):
    automation_lane_open_state: bool = attr(name="automationLaneOpenState")
    id: int = attr(name="id")
    index: int = attr(name="index")
    select: bool = attr(name="select")
    visible: bool = attr(name="visible")
    track_parameters: TrackParameters = element()
    track_audio_parameters: TrackAudioParameters = element()
    edit_parameters: list[EditParameter] = element(default_factory=list)
