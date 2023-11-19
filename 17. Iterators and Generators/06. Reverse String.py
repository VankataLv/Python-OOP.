def reverse_text(text: str):
    cur_i = -1
    while cur_i != -len(text) - 1:
        yield text[cur_i]
        cur_i -= 1


for char in reverse_text("step"):
    print(char, end='')
