from functools import lru_cache
from utils import config
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine, async_sessionmaker


def get_database_url() -> str:
    settings = config.get_settings()
    return f"postgresql+asyncpg://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASE}"


DATABASE_URL = get_database_url()
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)

# Session maker for async sessions
async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency to get the async session
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
