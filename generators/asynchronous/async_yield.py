import asyncio


class Ticker:
    def __init__(self, delay, to) -> None:
        self.delay = delay
        self.initial = 0
        self.to = to

    def __aiter__(self):
        return self

    async def __anext__(self):
        i = self.initial
        if i >= self.to:
            raise StopAsyncIteration

        self.initial += 1
        if i:
            await asyncio.sleep(self.delay)
        return i


# the above is same as:


async def ticker(delay, to):
    for i in range(to):
        yield i
        await asyncio.sleep(delay=delay)


async def getfunc():
    yield 1
    yield 2


gen = getfunc()


async def print_func():
    assert gen.__aiter__() is gen
    print(gen)
    assert await gen.__anext__() == 1
    assert await gen.__anext__() == 2

    try:
        await gen.__anext__()
    except StopAsyncIteration:
        print("Raised Asyncio iteration")


asyncio.run(print_func())
