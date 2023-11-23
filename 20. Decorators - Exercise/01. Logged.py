def logged(func):   # ако няма параметри, приема директно референция към функцията
    def wrapper(*args):
        return f"you called {func.__name__}" \
               f"({', '.join(str(arg) for arg in args)})\n" \
               f"it returned {func(*args)}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))

