from typing import Iterator


class SimpleGenerator:
    # Two different syntax for simple generators

    # Syntax 1
    @classmethod
    def generate_value(cls, how_many_times):
        value = 0
        while value < how_many_times:
            yield value
            value += 1

    # Syntax 2
    @classmethod
    def generator_object(cls, how_many_times):
        obj = (i * i for i in range(how_many_times))
        return obj

    # Print Syntax 1
    @classmethod
    def print_generate_value(cls):
        generator_ = cls.generate_value(3)
        print("Value for generate_value in print_generate_value")
        for value in generator_:
            print(value)

    # Print Syntax 2
    @classmethod
    def print_generated_object(cls):
        square_generator_ = cls.generator_object(3)
        # print(square_generator_)  # return generator object
        print("Value for generator_object in print_generated_object")
        for i in square_generator_:
            print(i)

    @classmethod
    def splat_operator_for_unpacking_generator(cls):
        # as of python 3.5
        print("Value for splat operator")
        print(*(x for x in range(10)))

    @classmethod
    def gen(cls, skip_even: bool = False) -> Iterator[int]:
        yield 1
        if not skip_even:
            yield 2
        yield 3

    @classmethod
    def print_gen(cls):
        print("Value for gen using print_gen")
        g = cls.gen(skip_even=True)
        print(next(g))
        print(next(g))
        try:
            print(next(g))
        except StopIteration:
            # todo add specific exception
            print("Only two value")


class_ = SimpleGenerator
class_.print_generate_value()
class_.print_generated_object()
class_.splat_operator_for_unpacking_generator()
class_.print_gen()

# Note: The syntax of generator is same as tuple comprehension

# We can create tuple list from list comprehension as (if performance not an issue, if performance issue use generators):
# tuple([i * i for i in range(3)])
# or
# tuple(square_generator_)
