from typing import Callable, Iterable, TypeVar

T = TypeVar('T')


def min_count(m: Iterable[T], h: Callable[[T], float], k: int, b=0) -> float:
    t = [1.0 for _ in range(k)]
    for x in m:
        hx = h(int(x), b)
        if hx < t[k - 1] and hx not in t:
            t[k - 1] = hx
            t.sort()
    if t[k - 1] == 1.0:
        n = sum(y != 1.0 for y in t)
    else:
        n = (k - 1) / t[k - 1]
    return n
