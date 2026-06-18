from collections.abc import Generator
from typing import Any
import os

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from muapi import MuAPI


class ImageToVideoTool(Tool):
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

        result = client.videos.from_image(
            image=tool_parameters["image"],
            prompt=tool_parameters["prompt"],
            model=tool_parameters.get(
                "model",
                "kling-std"
            ),
            duration=int(
                tool_parameters.get(
                    "duration",
                    5
                )
            ),
            aspect_ratio=tool_parameters.get(
                "aspect_ratio",
                "16:9"
            ),
        )

        video_url = None

        if isinstance(result, dict):
            video_url = result.get("video") or result.get("url") or result.get("output")

            if not video_url and result.get("videos"):
                video_url = result["videos"][0]

        if video_url:
            yield self.create_link_message(video_url)

        yield self.create_json_message(
            result if isinstance(result, dict) else {"result": str(result)}
        )
