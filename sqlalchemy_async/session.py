# goal is to create a DB session connection that is reusable for all project

import contextvars

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

profiling_context = contextvars.ContextVar("profiling")

engine = create_async_engine(
    config.database_url.unicode_string(),
    pool_size=db_config.pool_size,
    max_overflow=db_config.max_overflow,
    pool_pre_ping=db_config.pool_pre_ping,
)

SessionLocal = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)
