import csv
import random
from multiprocessing import Process
from typing import Iterable, List

from hashfunctions import adler32, blake2s, sha1, sha3_512
from mincount import min_count
from setutils import generate_random_set, sets_generator

SAMPLES = 100


def generate_multiset_from_set(m_set: List[int]):
    l = len(m_set)
    return m_set + random.choices(m_set, k=random.randint(l, 10 * l))


def a():
    gen = sets_generator(10000)
    for m_set in gen:
        multi_set = generate_multiset_from_set(m_set)
        assert min_count(m_set, blake2s, 100) == min_count(multi_set, blake2s, 100)
    print("Repetitions do not change estimation value.")


def prepare_plot_data(k: int):
    with open("results" + str(k) + ".csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["n", "n_hat / n"])
        gen = sets_generator(10000)
        for m_set in gen:
            n = len(m_set)
            writer.writerow([n, min_count(m_set, sha1, k) / n])


def b():
    k_values = [2, 3, 10, 100, 400]
    # k_values = [320]
    processes = []
    for k in k_values:
        processes.append(Process(target=prepare_plot_data, args=(k, )))
    for p in processes:
        p.start()
    for p in processes:
        p.join()


def find_k_upper_bound(n: int):
    prev_k = 0
    k = 2
    while True:
        successes = 0
        for _ in range(SAMPLES):
            m_set = generate_random_set(n)
            if abs(min_count(m_set, blake2s, k) / n - 1) < 0.1:
                successes += 1
        if successes / SAMPLES >= 0.95:
            return (prev_k, k)
        print(k)
        prev_k = k
        k *= 2


def c():
    n = 10000
    interval = find_k_upper_bound(n)
    while interval[1] - interval[0] > 1:
        k = interval[0] + ((interval[1] - interval[0]) // 2)
        successes = 0
        for _ in range(SAMPLES):
            m_set = generate_random_set(n)
            if abs((min_count(m_set, blake2s, k) / n) - 1) < 0.1:
                successes += 1
        if successes / SAMPLES >= 0.95:
            interval = (interval[0], k)
        else:
            interval = (k, interval[1])
    print(interval[1])
    return interval[1]


def main():
    # a()
    b()
    # c()


if __name__ == "__main__":
    main()
