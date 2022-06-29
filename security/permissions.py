import typing
# from myauth import authenticate_header, authenticate_query_param

from starlette.requests import Request
from starlette.websockets import WebSocket
from strawberry.permission import BasePermission
from strawberry.types import Info

from security.jwt import verify_current_user


def get_token_without_bearer(token_with_bearer: str):
    return token_with_bearer[7:]


class IsAuthenticated(BasePermission):
    message = "User is not authenticated"

    # This method can also be async!
    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        request: typing.Union[Request, WebSocket] = info.context["request"]

        if "Authorization" in request.headers:
            return verify_current_user(
                get_token_without_bearer(request.headers["Authorization"]))

        if "auth" in request.query_params:
            return verify_current_user(
                get_token_without_bearer(request.headers["auth"]))

        return False
