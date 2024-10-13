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
        for value in generator_:
            print(value)

    # Print Syntax 2
    @classmethod
    def print_generated_object(cls):
        square_generator_ = cls.generator_object(3)
        print(square_generator_)  # return generator object
        for i in square_generator_:
            print(i)


SimpleGenerator.print_generate_value()
SimpleGenerator.print_generated_object()

# Note: The syntax of generator is same as tuple comprehension

# We can create tuple list from list comprehension as (if performance not an issue, if performance issue use generators):
# tuple([i * i for i in range(3)])
# or
# tuple(square_generator_)
