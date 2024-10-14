import asyncio
from typing import IO

from aiohttp import ClientSession


async def download(url: str, file: IO[bytes]) -> None:
    async with ClientSession() as session:
        async with session.get(url) as response:
            file.write(await response.read())


async def get_one(url: str, path: str) -> None:
    with open(path, "wb") as f:
        await download(url, f)


async def yield_maybe():
    await asyncio.sleep(1)
    yield 1


loop = asyncio.get_event_loop()
loop.run_until_complete(yield_maybe)
