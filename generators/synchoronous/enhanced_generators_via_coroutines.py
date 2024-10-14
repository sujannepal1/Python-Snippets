import sys


def try_finally():
    try:
        yield 1
        yield 2
    # except GeneratorExit:
    #     print("Generator exited with break at the iterator side")
    finally:
        print(sys.exc_info())


# here we exhaust the generator fully

for i in try_finally():
    print(i)


def test_throw():
    print("Before")
    try:
        yield 1
    except Exception:
        print("Exception!")
    yield 2
    print("After")


for i in test_throw():
    print(i)
    break
