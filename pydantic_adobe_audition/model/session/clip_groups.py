"""Top-level information about groups of clips"""

from pydantic_adobe_audition.common import BaseSesxModel


class ClipGroups(BaseSesxModel, tag="clipGroups"):
    text: str | None = None
