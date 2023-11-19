def squares(n):
    cur_iteration = 1
    while cur_iteration != n + 1:
        yield cur_iteration ** 2
        cur_iteration += 1


print(list(squares(5)))
