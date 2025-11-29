## Variable-length arguments

def soma(*values):
    return sum(values)

soma(1, 2, 3, 4, 5)


def soma(*args):
    result = 0
    for arg in args:
        result = result + arg
    return result

soma(1, 2, 3, 4, 5)


def math_calculation(arg1=1, arg2=1, *args):
    result = 0
    for arg in args:
        result += arg
    result = result * arg1 * arg2
    return result

math_calculation(2, 3, 1, 2, 3, 4, 5)


## Named variable-length arguments (Keyword arguments - **kwargs)

def named_argument(**kwargs):
    print(kwargs)

named_argument(name="Yukio", age=38, state="SP")


def named_argument(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

