class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.cur_iteration = 0

    def __iter__(self):
        return self

    def __next__(self):
        num_to_print = 0
        if self.cur_iteration >= self.count:
            raise StopIteration()
        num_to_print += self.step * self.cur_iteration
        self.cur_iteration += 1
        return num_to_print


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
