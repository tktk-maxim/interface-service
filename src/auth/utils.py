from jwt import encode, decode
from config import settings


def encode_jwt(
    payload: dict,
    key: str = settings.auth_jwt_key,
    algorithm: str = settings.auth_jwt_algorithm,
) -> str:
    to_encode = payload.copy()
    encoded = encode(
        to_encode,
        key,
        algorithm=algorithm,
    )
    return encoded


def decode_jwt(
    token: str,
    key: str = settings.auth_jwt_key,
    algorithm: str = settings.auth_jwt_algorithm,
) -> dict:
    decoded = decode(
        token,
        key,
        algorithms=[algorithm],
    )
    return decoded

