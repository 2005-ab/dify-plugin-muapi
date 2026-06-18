from collections.abc import Generator
from typing import Any
import os

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from muapi import MuAPI


class RemixAudioTool(Tool):
    def _invoke(
        self,
        tool_parameters: dict[str, Any],
    ) -> Generator[ToolInvokeMessage]:

        api_key = self.runtime.credentials.get(
            "muapi_api_key"
        )

        if not api_key:
            yield self.create_json_message(
                {
                    "error": "Missing MuAPI API key"
                }
            )
            return

        os.environ["MUAPI_API_KEY"] = api_key

        client = MuAPI()

        result = client.audio.remix(
            song_id=tool_parameters["song_id"],
            prompt=tool_parameters.get(
                "prompt",
                ""
            ),
            title=tool_parameters.get(
                "title",
                ""
            ),
            tags=tool_parameters.get(
                "tags",
                ""
            ),
        )

        audio_url = None

        if isinstance(result, dict):
            audio_url = (
                result.get("audio")
                or result.get("audio_url")
                or result.get("url")
                or result.get("output")
            )

        if audio_url:
            yield self.create_link_message(
                audio_url
            )

        yield self.create_json_message(
            result if isinstance(result, dict)
            else {"result": str(result)}
        )