import random
from typing import Iterable, List


def generate_random_set(n: int) -> List[int]:
    return random.sample(range(10 ** 9), n)


def sets_generator(n: int) -> Iterable[List[int]]:
    last_number = 1
    last_size = 0
    while last_size < n:
        last_size += 1
        yield list(range(last_number, last_number + last_size))
        last_number += last_size
