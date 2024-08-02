import strawberry
from strawberry.types import Info

from .dependencies import auth_user_check_self_info, auth_user_issue_jwt
from .schemas import UserSchema, TokenInfo


@strawberry.type
class Mutation:
    @strawberry.mutation
    def login(self, login: str, password: str) -> TokenInfo:
        return auth_user_issue_jwt(login, password)
