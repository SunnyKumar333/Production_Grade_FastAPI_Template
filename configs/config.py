from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    app_name: str = "FastAPI Template Application"
    
    # logsger setting 
    log_dir: str
    
    # database settings 
    database_host: str
    database_port: int
    database_user: str
    database_password: str
    database_name: str
    model_config = SettingsConfigDict(env_file=".env")
    
@lru_cache
def get_settings():
    return Settings()