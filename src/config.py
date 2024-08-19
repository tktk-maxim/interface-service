import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    user_service_host: str
    user_service_port: str

    run_test: bool

    task_service_host: str
    task_service_port: str

    auth_jwt_key: str
    auth_jwt_algorithm: str
    auth_jwt_expire_minutes: int

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')


settings = Settings()
