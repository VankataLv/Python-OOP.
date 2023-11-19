class custom_range:             # snake case because it imitates a function
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end          # end is inclusive

    def __iter__(self):
        return self             # итерирай през себе си

    def __next__(self):
        cur_num = self.start
        if cur_num - 1 == self.end:
            raise StopIteration()
        self.start += 1
        return cur_num


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
