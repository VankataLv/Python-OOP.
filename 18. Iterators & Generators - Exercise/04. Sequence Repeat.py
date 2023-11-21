class sequence_repeat:
    def __init__(self, string_to_repeat: str, times_to_repeat: int):
        self.string_to_repeat = string_to_repeat
        self.times_to_repeat = times_to_repeat
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.times_to_repeat:
            raise StopIteration()
        index = self.string_to_repeat[self.iterations % len(self.string_to_repeat)]
        self.iterations += 1
        return index

