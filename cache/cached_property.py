from functools import cached_property
import time


class Fibonacci:
    def __init__(self, n):
        self.n = n

    # This is only cached with per instance
    @cached_property
    def value(self) -> int:
        if self.n <= 1:
            return self.n
        else:
            return Fibonacci(self.n - 1).value + Fibonacci(self.n - 2).value


# Print Fibonacci numbers for 0 to 59
start_time = time.time()
for i in range(60):
    fib = Fibonacci(i)
    print(i, " : ", fib.value)
end_time = time.time()

print((f"@cached_property Execution Time: {end_time - start_time:.6f} seconds"))
