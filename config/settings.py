import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    # Environment
    environment: str = os.getenv("ENVIRONMENT", "qa")

    # API
    base_url: str = os.getenv("BASE_URL", "http://localhost:8000")
    timeout: int = int(os.getenv("TIMEOUT", "30"))

    # Database
    db_host: str = os.getenv("DB_HOST", "localhost")
    db_port: int = int(os.getenv("DB_PORT", "5432"))
    db_name: str = os.getenv("DB_NAME", "ecommerce")
    db_user: str = os.getenv("DB_USER", "admin")
    db_password: str = os.getenv("DB_PASSWORD", "admin")


settings = Settings()
