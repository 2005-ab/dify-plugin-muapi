from collections.abc import Generator
from typing import Any
import os

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from muapi import MuAPI


class EditImageTool(Tool):
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

        kwargs = {
            "image": tool_parameters["image"],
            "prompt": tool_parameters["prompt"],
            "model": tool_parameters.get(
                "model",
                "flux-kontext-dev"
            ),
        }

        aspect_ratio = tool_parameters.get("aspect_ratio")
        if aspect_ratio:
            kwargs["aspect_ratio"] = aspect_ratio

        result = client.images.edit(**kwargs)

        if isinstance(result, dict) and result.get("images"):
            yield self.create_image_message(
                result["images"][0]
            )

        yield self.create_json_message(
            result if isinstance(result, dict) else {"result": str(result)}
        )
