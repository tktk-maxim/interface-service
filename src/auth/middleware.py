import typing

from strawberry.permission import BasePermission
from strawberry.types import Info
from .dependencies import auth_user_check_self_info


class IsAuthenticated(BasePermission):
    message = "User is not Authenticated"

    def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        auth_header = info.context["request"].headers.get("Authorization")
        if not auth_header:
            raise Exception("Authorization header missing")
        token = auth_header.split(" ")[1]
        user = auth_user_check_self_info(token=token)
        return True if user else False
