import asyncio


async def awesomeness_generator(delay_in_sec, message) -> str:
    await asyncio.sleep(delay_in_sec)
    print(message + "Awesome")
    return "Good Message"


async def main() -> None:
    value = await asyncio.gather(
        awesomeness_generator(2, "hello"), awesomeness_generator(1, "World")
    )
    assert value == ["Good Message"] * 2


asyncio.run(main())
