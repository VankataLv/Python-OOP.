# class iterator имплементира 2 дъндър метода:
# __iter__ и __next__
# ако ги няма той не знае какво да итерира

# генераторите се изчерпват след итериране
# ▪ Generators are a simple way of creating iterators
# ▪ A generator is a function that returns an object (iterator)
# ▪ This iterator can later be iterated over (one value at a time)

# --yield-- if a func contains yield it becomes a generator func
# difference with return is that yield pauses the func, return terminates it entirely

# ако използваме filter за да го ползваме повече от веднъж го приравняваме на list например
# result = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
# for i in result:
#     print(i)
# for i in result:
#     print(i)

