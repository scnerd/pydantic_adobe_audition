"""Tracks referenced external audio files."""

from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel


class File(BaseSesxModel, tag="file"):
    absolute_path: str = attr(name="absolutePath")
    id: int = attr(name="id")
    importer_private_settings: str | None = attr(name="importerPrivateSettings", default=None)
    media_handler: str = attr(name="mediaHandler")
    relative_path: str = attr(name="relativePath")


class Files(BaseSesxModel, tag="files"):
    text: str | None = element(default=None)
    files: list[File] = element()
