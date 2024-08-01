import strawberry
from strawberry.types import Info

from fastapi import HTTPException, status
import httpx

from jwt.exceptions import InvalidTokenError

from .utils import decode_jwt, encode_jwt
from config import settings
from .schemas import UserSchema, TokenInfo


def get_user(login: str, password: str) -> UserSchema:
    client = httpx.Client()
    response = client.post(f"http://{settings.user_service_host}:{settings.user_service_port}/auth/entity/",
                           json={"login": login, "password": password})
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return UserSchema(**response.json())


def validate_auth_user(
        login: str,
        password: str,
) -> UserSchema:

    unauthorized_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid username or password",
    )

    if not (user := get_user(login, password)):
        raise unauthorized_exc

    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="user inactive",
        )

    return user


def get_current_token_payload(token: str) -> dict:
    try:
        payload = decode_jwt(
            token=token,
        )

    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token error: {e}",
        )
    return payload


def get_current_auth_user(token: str) -> UserSchema:

    payload: dict = get_current_token_payload(token)
    login: str | None = payload.get("login")
    password: str | None = payload.get("password")

    if user := get_user(login, password):
        return user
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="token invalid (user not found)",
    )


def get_current_active_auth_user(token: str) -> UserSchema:

    user: UserSchema = get_current_auth_user(token)

    if user.active:
        return user
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="user inactive",
    )


def auth_user_issue_jwt(
        login: str,
        password: str
) -> TokenInfo:

    user: UserSchema = validate_auth_user(login,password)

    jwt_payload = {
        "sub": user.login,
        "login": user.login,
        "password": user.password,
        "email": user.email,
    }

    token = encode_jwt(jwt_payload)
    tkn = TokenInfo(
        access_token=token,
        token_type="Bearer",
    )

    return tkn


def auth_user_check_self_info(token: str) -> UserSchema:
    user: UserSchema = get_current_active_auth_user(token)
    return user
