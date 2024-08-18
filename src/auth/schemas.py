import strawberry


@strawberry.type
class UserSchema:
    id: int
    first_name: str
    last_name: str
    middle_name: str | None = ""
    login: str
    password: str
    email: str
    subdivision_id: int
    leader: bool | None = False
    active: bool | None = True
    chat_id: int | None = None
    telegram_name: str


@strawberry.type
class TokenInfo:
    access_token: str
    token_type: str
