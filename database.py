from sqlalchemy import URL, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from config.settings import settings


DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.db_user,
    password=settings.db_password,
    host=settings.db_host,
    port=settings.db_port,
    database=settings.db_name,
)

engine = create_engine(
    DATABASE_URL,
    echo=False
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
