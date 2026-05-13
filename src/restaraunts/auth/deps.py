from typing import Annotated
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from .oidc import OIDCClient


bearer_token_schema = HTTPBearer()
oidc = OIDCClient(issuer="https://lemur-16.cloud-iam.com/auth/realms/my-fastapi-auth", client_id="fastapi-client")

async def get_valid_token(token: HTTPAuthorizationCredentials = Depends(bearer_token_schema)) -> str:
    _token = token.credentials
    await oidc.validate_token(_token)
    return _token
    

AuthTokenDep = Annotated[str, Depends(get_valid_token)]
