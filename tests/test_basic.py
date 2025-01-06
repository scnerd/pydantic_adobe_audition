import re
from pathlib import Path
from xml.etree import ElementTree as ET

import pytest
from pydantic_xml import BaseXmlModel

from pydantic_adobe_audition.model import Sesx
from pydantic_adobe_audition.model.session import Tracks
from pydantic_adobe_audition.model.session.tracks import AudioTrack, BusTrack, MasterTrack
from pydantic_adobe_audition.model.session.tracks.audio import AudioClip

from . import TEST_ROOT


def _stem(path: Path):
    return path.stem


def _normalize_xml(xml_content: str) -> str:
    xml = ET.tostring(ET.fromstring(xml_content), encoding="unicode")
    xml = re.sub(r"\n\s*", "", xml)
    return xml


def _check(model: type[BaseXmlModel], path: Path):
    xml_content = path.read_text()

    # Check that the XML even parses properly
    parsed = model.from_xml(xml_content)

    # Check that re-serializing the result results in no meaningful changes
    assert _normalize_xml(parsed.to_xml()) == _normalize_xml(xml_content)


# Get a list of all .sesx files in the sample_projects directory
@pytest.mark.parametrize("path", list(TEST_ROOT.glob("sample_projects/*.sesx")), ids=_stem)
def test_sesx(path):
    _check(Sesx, path)


@pytest.mark.parametrize("path", list(TEST_ROOT.glob("sample_chunks/audio_clip_*.xml")), ids=_stem)
def test_audio_clip(path):
    _check(AudioClip, path)


@pytest.mark.parametrize("path", list(TEST_ROOT.glob("sample_chunks/audio_track_*.xml")), ids=_stem)
def test_audio_track(path):
    _check(AudioTrack, path)


@pytest.mark.parametrize("path", list(TEST_ROOT.glob("sample_chunks/bus_track_*.xml")), ids=_stem)
def test_bus_track(path):
    _check(BusTrack, path)


@pytest.mark.parametrize("path", list(TEST_ROOT.glob("sample_chunks/master_track_*.xml")), ids=_stem)
def test_master_track(path):
    _check(MasterTrack, path)


@pytest.mark.parametrize("path", list(TEST_ROOT.glob("sample_chunks/tracks_*.xml")), ids=_stem)
def test_tracks(path):
    _check(Tracks, path)
