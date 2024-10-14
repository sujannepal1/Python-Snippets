import dis
import time
from random import SystemRandom
from typing import Iterator
from rich.progress import track


def expensive_operation():
    time.sleep(0.2)
    return SystemRandom().random()


def get_results(how_many: int) -> list[float]:
    result = []
    for i in range(how_many):
        result.append(expensive_operation())

    return result


# here we returned iterator
def gen_results(how_many: int) -> Iterator[float]:
    for i in range(how_many):
        yield expensive_operation()


for num in track(gen_results(how_many=5)):
    print(f"{num:.2f}")


dis.dis(gen_results.__code__)
