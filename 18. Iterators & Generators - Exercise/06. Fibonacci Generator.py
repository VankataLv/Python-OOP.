def fibonacci():
    cur_num = 1
    last_num = 0


    yield last_num
    yield cur_num

    while True:
        next_num = last_num + cur_num
        yield next_num
        last_num, cur_num = cur_num, next_num



generator = fibonacci()
for i in range(5):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))