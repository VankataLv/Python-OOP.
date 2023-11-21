def get_primes(numbers: list):
    for cur_num in numbers:
        if cur_num < 2:
            continue
        for smaller_num in range(2, cur_num):
            if cur_num % smaller_num == 0:
                break
        else:
            yield cur_num





