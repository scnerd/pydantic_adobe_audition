"""Tracks referenced audio devices."""

import uuid
from typing import Annotated

from pydantic import WrapSerializer
from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel, uppercase_uuid_serializer


class InputPort(BaseSesxModel, tag="inputPort"):
    id: int = attr(name="id")
    name: str = attr(name="name")


class OutputPort(BaseSesxModel, tag="outputPort"):
    id: int = attr(name="id")
    name: str = attr(name="name")


class AudioDevice(BaseSesxModel, tag="audioDevice"):
    """Audio device available when last working on the project."""

    input_id: Annotated[uuid.UUID, WrapSerializer(uppercase_uuid_serializer)] = attr(name="inputID")
    """"""

    output_id: Annotated[uuid.UUID, WrapSerializer(uppercase_uuid_serializer)] = attr(name="outputID")
    """"""

    # text: str | None = element(default=None)

    input_ports: list[InputPort] = element()
    """Available audio input devices"""

    output_ports: list[OutputPort] = element()
    """Available audio output devices"""
