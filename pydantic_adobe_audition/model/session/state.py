from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class SelectionState(BaseSesxModel, tag="selectionState"):
    selection_duration: str = attr(name="selectionDuration")
    selection_start: str = attr(name="selectionStart")


class ViewState(BaseSesxModel, tag="viewState"):
    horizontal_view_duration: str = attr(name="horizontalViewDuration")
    horizontal_view_start: str = attr(name="horizontalViewStart")
    track_controls_width: str = attr(name="trackControlsWidth")
    vertical_scroll_offset: str = attr(name="verticalScrollOffset")


class TimeFormatState(BaseSesxModel, tag="timeFormatState"):
    beats_per_bar: str = attr(name="beatsPerBar")
    beats_per_minute: str = attr(name="beatsPerMinute")
    custom_frame_rate: str = attr(name="customFrameRate")
    link_to_default_time_settings: str = attr(name="linkToDefaultTimeSettings")
    note_length: str = attr(name="noteLength")
    subdivisions: str = attr(name="subdivisions")
    time_code_drop_frame: str = attr(name="timeCodeDropFrame")
    time_code_frame_rate: str = attr(name="timeCodeFrameRate")
    time_code_ntsc: str = attr(name="timeCodeNTSC")
    time_format: str = attr(name="timeFormat")


class MixingOptionState(BaseSesxModel, tag="mixingOptionState"):
    default_pan_mode_logarithmic: str = attr(name="defaultPanModeLogarithmic")
    pan_power: str = attr(name="panPower")
    play_overlapping_clips: str = attr(name="playOverlappingClips")


class SessionState(BaseSesxModel, tag="SessionState"):
    cti_position: str = attr(name="ctiPosition")
    smpte_start: str = attr(name="smpteStart")
    text: str | None = None
    selection_state: SelectionState = element()
    view_state: ViewState = element()
    time_format_state: TimeFormatState = element()
    mixing_option_state: MixingOptionState = element()
