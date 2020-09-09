import csv
from multiprocessing import Process

from hashfunctions import blake2s2, crc322, sha12, adler322
from hyperloglog import hyper_log_log
from setutils import sets_generator


def prepare_plot_data(b: int):
    with open("hll_results" + str(b) + ".csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["n", "n_hat / n"])
        gen = sets_generator(10000)
        for m_set in gen:
            n = len(m_set)
            writer.writerow([n, hyper_log_log(m_set, sha12, b) / n])


def a():
    b_values = range(4, 17)
    processes = []
    for b in b_values:
        processes.append(Process(target=prepare_plot_data, args=(b, )))
    for p in processes:
        p.start()
    for p in processes:
        p.join()


def main():
    a()


if __name__ == "__main__":
    main()
