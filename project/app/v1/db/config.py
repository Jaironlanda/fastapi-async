from curses import echo
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

load_dotenv()

ASYNC_SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL, echo=True, future=True)

Base = declarative_base()

async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
