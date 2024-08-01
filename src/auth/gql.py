import strawberry
from strawberry.types import Info

from .dependencies import auth_user_check_self_info, auth_user_issue_jwt
from .schemas import UserSchema, TokenInfo


@strawberry.type
class Mutation:
    @strawberry.mutation
    def login(self, login: str, password: str) -> TokenInfo:
        return auth_user_issue_jwt(login, password)

    @strawberry.mutation
    def protected(self, info: Info) -> str:
        auth_header = info.context["request"].headers.get("Authorization")
        if not auth_header:
            raise Exception("Authorization header missing")
        token = auth_header.split(" ")[1]
        user = auth_user_check_self_info(token=token)
        return f"Hello {user.login}! You have accessed a protected route."
