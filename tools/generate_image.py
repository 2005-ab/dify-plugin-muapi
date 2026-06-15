from collections.abc import Generator
from typing import Any
import os

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from muapi import MuAPI


class GenerateImageTool(Tool):
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

        result = client.images.generate(
            prompt=tool_parameters["prompt"],
            model=tool_parameters.get(
                "model",
                "flux-dev"
            ),
            width=int(
                tool_parameters.get(
                    "width",
                    1024
                )
            ),
            height=int(
                tool_parameters.get(
                    "height",
                    1024
                )
            ),
            num_images=int(
                tool_parameters.get(
                    "num_images",
                    1
                )
            ),
        )

        if result.get("images"):
            yield self.create_image_message(
                result["images"][0]
            )

        yield self.create_json_message(
            result
        )