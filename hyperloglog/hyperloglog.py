import math
from typing import Callable, Iterable, TypeVar

T = TypeVar('T')


def get_a(b):
    if b == 4:
        a = 0.673
    elif b == 5:
        a = 0.697
    elif b == 6:
        a = 0.709
    else:
        a = 0.7213 / (1 + 1.079 / (2 ** b))
    return a


def hyper_log_log(m: Iterable[T], h: Callable[[T], float], b: int) -> float:
    mask = (1 << b) - 1
    n = 2 ** b
    M = []
    for _ in range(n):
        M.append(0)
    for v in m:
        x = h(v)
        j = x & mask
        w = x >> b
        M[j] = max(M[j], 32 - b - w.bit_length() + 1)
    z = get_a(b) * (n ** 2) * (1 / sum([2 ** (-x) for x in M]))
    if z <= (5 / 2) * n:
        c = M.count(0)
        if c != 0:
            z = n * math.log(n / c)
    elif z > (1 / 30) * (2 ** 32):
        z = - (2 ** 32) * math.log(1 - (z / (2 ** 32)))
    return z
