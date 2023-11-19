class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.items_dict = list(dict_obj.items())
        self.cur_i = 0
        self.key_to_print = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_i >= len(self.items_dict):
            raise StopIteration()
        self.key_to_print = self.cur_i
        self.cur_i += 1
        return self.items_dict[self.key_to_print]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
