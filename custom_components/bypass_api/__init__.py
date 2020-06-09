from aiohttp.web import middleware
from homeassistant.auth.models import RefreshToken, User
from homeassistant.components.http import KEY_AUTHENTICATED


async def async_setup(hass, hass_config):
    @middleware
    async def auth_middleware(request, handler):
        # useful for rest api
        request[KEY_AUTHENTICATED] = True
        return await handler(request)

    async def async_validate_access_token(token: str):
        # useful for websocket api
        return refresh_token

    user = User(id=None, name=None, perm_lookup=None, is_active=True,
                is_owner=True)
    refresh_token = RefreshToken(user=user, client_id=None,
                                 access_token_expiration=None)

    hass.http.app.middlewares.append(auth_middleware)
    hass.auth.async_validate_access_token = async_validate_access_token

    return True
