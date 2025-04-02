from pydantic import SecretStr
from pydantic_settings import BaseSettings


class AppConfig(BaseSettings):
    """
    Unified configuration class using Pydantic BaseSettings.
    """

    # Common settings
    ENV: str = "prod"  # Default to "dev" environment
    DEBUG: bool = False

    SOURCE_URL: str
    SOURCE_API_KEY: SecretStr = SecretStr("default-secret-key")
    SOURCE_API_SECRET: SecretStr = SecretStr("default-secret")

    DESTINATION_URL: str
    DESTINATION_API_KEY: SecretStr
    DESTINATION_API_SECRET: SecretStr

    class Config:
        env_file = ".env"  # Load local environment variables from a .env file (for development)
