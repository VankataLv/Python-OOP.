class reverse_iter:
    def __init__(self, iterable_obj: iter):
        self.iterable_obj = iterable_obj
        self.cur_num = len(self.iterable_obj) - 1
        self.end_i = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_num <= self.end_i:
            raise StopIteration()
        index = self.cur_num
        self.cur_num -= 1
        return self.iterable_obj[index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
