from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


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

        except Exception as e:
            raise ToolProviderCredentialValidationError(
                str(e)
            )