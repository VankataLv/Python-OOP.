def possible_permutations(elements_to_permutate: list):
    if len(elements_to_permutate) <= 1:
        yield elements_to_permutate
    else:
        for iteration in range(len(elements_to_permutate)):
            for perm in possible_permutations(elements_to_permutate[:iteration] + elements_to_permutate[iteration + 1:]):
                yield [elements_to_permutate[iteration]] + perm

[print(n) for n in possible_permutations([1, 2, 3])]
