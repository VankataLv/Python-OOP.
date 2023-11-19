class vowels:
    VOWELS = ("a", "i", "u", "y", "e", "o")

    def __init__(self, text):
        self.text = text
        self.found_vowels = [char for char in self.text if char.lower() in self.VOWELS]
        self.next_i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_i == len(self.found_vowels):
            raise StopIteration()
        i = self.next_i
        self.next_i += 1
        return self.found_vowels[i]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
