"""Base model for the entire contents of a SESX file."""

from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel
from pydantic_adobe_audition.model.audio_device import AudioDevice
from pydantic_adobe_audition.model.files import Files
from pydantic_adobe_audition.model.session import Session


class Sesx(BaseSesxModel, tag="sesx"):
    """
    Represents the base model for the entire contents of a SESX file.
    """

    version: str = attr(name="version")
    """Sesx file format version"""

    # text: str | None = None

    session: Session = element()
    """Internal information about the multi-track session"""

    files: Files = element()
    """List of files referenced by the session"""

    audio_device: AudioDevice = element(alias="audioDevice")
    """Information about audio devices used in the session"""


# __all__ = (
#     "Sesx",
# )
