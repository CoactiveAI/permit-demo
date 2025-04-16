from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str

    # Permit settings
    PERMIT_PROJECT: str = "default"
    PERMIT_PDP_URL: str = "http://0.0.0.0:7766"
    PERMIT_SDK_KEY: str = ""
    PERMIT_ORG_ID: str = ""

    class Config:
        # Assuming your environment variables are defined in a .env file
        env_file = ".env"
        env_file_encoding = "utf-8"
