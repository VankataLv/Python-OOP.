def genrange(start: int, end: int):
    cur_iteration = start
    while cur_iteration != end + 1:
        yield cur_iteration
        cur_iteration += 1

print(list(genrange(1, 10)))
