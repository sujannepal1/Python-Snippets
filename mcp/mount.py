# Example: Importing a subserver
from typing import Literal
from fastmcp import FastMCP
import asyncio

main = FastMCP(name="Main")
sub = FastMCP(name="Sub")


@sub.tool()
def hello() -> str:
    return "hi"


# Mount directly
main.mount("sub", sub)
