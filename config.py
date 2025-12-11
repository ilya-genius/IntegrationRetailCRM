from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    RETAILCRM_API_KEY: str
    RETAILCRM_API_URL: str
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
