from collections.abc import Generator
from typing import Any
import os

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from muapi import MuAPI


class UpscaleImageTool(Tool):
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

        result = client.enhance.upscale(
            image_url=tool_parameters["image"]
        )

        if isinstance(result, dict):
            image_url = None

            if result.get("images"):
                image_url = result["images"][0]
            elif result.get("outputs"):
                image_url = result["outputs"][0]

            if image_url:
                yield self.create_image_message(
                    image_url
                )

        yield self.create_json_message(
            result if isinstance(result, dict)
            else {"result": str(result)}
        )