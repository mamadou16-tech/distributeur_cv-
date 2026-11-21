"""Configuration centralisee. Toutes les valeurs sensibles viennent du .env."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Parametres applicatifs, charges depuis .env."""
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Base de donnees
    POSTGRES_USER: str = "cv_user"
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = "cv_distributor"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    DATABASE_URL: str = ""

    # Application
    APP_ENV: str = "development"
    DEBUG: bool = True
    UPLOAD_DIR: str = "../uploads"

    @property
    def sqlalchemy_url(self) -> str:
        """Construit l URL SQLAlchemy, ou utilise DATABASE_URL si definie."""
        if self.DATABASE_URL:
            return self.DATABASE_URL
        return (
            f"postgresql+psycopg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings = Settings()
