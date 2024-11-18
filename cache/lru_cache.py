import time
from functools import lru_cache


# This caches throughout
@lru_cache
def get_fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return get_fib(n - 1) + get_fib(n - 2)


start_time = time.time()

for i in range(60):
    print(i, " : ", get_fib(i))

end_time = time.time()

print((f"@lru_cache Execution Time: {end_time - start_time:.6f} seconds"))
