from pydantic_xml import attr

from pydantic_adobe_audition.common import BaseSesxModel


class _Fade(BaseSesxModel, __xml_abstract__=True):
    cross_fade_link_type: str = attr(name="crossFadeLinkType")
    end_point: str = attr(name="endPoint")
    shape: str = attr(name="shape")
    start_point: str = attr(name="startPoint")


class FadeIn(_Fade, tag="fadeIn"):
    fade_in_type: str = attr(name="type")


class FadeOut(_Fade, tag="fadeOut"):
    fade_out_type: str = attr(name="type")
