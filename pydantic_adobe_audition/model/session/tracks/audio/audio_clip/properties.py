from pydantic_xml import attr

from pydantic_adobe_audition.common import BaseSesxModel


class AudioClipProperties(BaseSesxModel, tag="properties"):
    properties: str = attr(name="properties")

    @property
    def properties_dict(self) -> dict:
        import json

        return json.loads(self.properties.replace("&quot;", '"'))
