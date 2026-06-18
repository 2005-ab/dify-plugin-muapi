import os

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from muapi import MuAPI


class MuapiProvider(ToolProvider):

    def validate_credentials(
        self,
        credentials: dict,
    ) -> None:

        try:
            api_key = credentials.get(
                "muapi_api_key"
            )

            if not api_key:
                raise ValueError(
                    "MuAPI API key is required"
                )

            os.environ["MUAPI_API_KEY"] = api_key

            client = MuAPI()

            client.accounts.balance()

        except Exception as e:
            raise ToolProviderCredentialValidationError(
                f"MuAPI credential validation failed: {str(e)}"
            )