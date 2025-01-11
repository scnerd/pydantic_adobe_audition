"""Top-level information about groups of clips"""

from pydantic_xml import attr, element

from pydantic_adobe_audition.common import BaseSesxModel

# <clipGroups>
#    <clipGroup hue="292" id="0">
#      <name>Group 44</name>
#      <item clipID="21" trackID="10003"/>
#      <item clipID="83" trackID="10002"/>
#      <item clipID="19" trackID="10005"/>
#    </clipGroup>
#    <clipGroup hue="92" id="1">
#      <name>Group 43</name>
#      <item clipID="20" trackID="10003"/>
#      <item clipID="18" trackID="10005"/>
#    </clipGroup>
#    ...
# </clipGroups>


class ClipGroupItem(BaseSesxModel, tag="item"):
    clip_id: int = attr(name="clipID")
    track_id: int = attr(name="trackID")


class ClipGroup(BaseSesxModel, tag="clipGroup"):
    hue: int = attr(name="hue")
    id: int = attr(name="id")
    name: str = element()
    items: list[ClipGroupItem] = element()


class ClipGroups(BaseSesxModel, tag="clipGroups"):
    groups: list[ClipGroup] = element(default_factory=list)
