import httpx
from authlib.jose import JsonWebToken

class OIDCClient:
    def __init__(self, issuer: str, client_id: str):
        self.issuer = issuer
        self.client_id = client_id
        self.jwt = JsonWebToken(['RS256', 'RS512'])
        self.jwks = {}

    async def get_jwks(self) -> dict:
        if self.jwks:
            return self.jwks
        async with httpx.AsyncClient() as client:
            metadata_r = await client.get(f'{self.issuer}/.well-known/openid-configuration')
            metadata_r.raise_for_status()
            metadata = metadata_r.json()
            jwks_r = await client.get(f'{metadata.get('jwks_uri')}')
            jwks_r.raise_for_status()
            jwks = jwks_r.json()
            self.jwks = jwks
            return jwks


    async def validate_token(self, token: str) -> dict:
        jwks = await self.get_jwks()
        try:
            options = {
                "iss": {"essential": True, "values": [self.issuer]},
                "azp": {"essential": True, "values": [self.client_id]}
            }
            claims = self.jwt.decode(token, jwks, claims_options=options)
            claims.validate()
            return claims
        except Exception as e:
            print(f"Token validation failed: {e}")
            raise e
    