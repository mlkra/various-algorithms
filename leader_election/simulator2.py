import math
import random
import sys
import statistics

def _probabilities(max_number_of_stations):
    m = math.ceil(math.log2(max_number_of_stations))
    # print(m)
    p = [0.5**i for i in range(1, m + 1)]
    while True:
        for i in range(m):
            yield p[i]


def simulate(number_of_stations, max_number_of_stations, samples):
    simulation_results = []
    m = math.ceil(math.log2(max_number_of_stations))
    p = [0.5**i for i in range(1, m + 1)]
    for _ in range(samples):
        it = -1
        signals = 0
        first_single_slot = 0
        while signals != 1:
            it = (it + 1) % m
            signals = 0
            first_single_slot += 1
            # beep_probability = next(probabilities)
            # print(beep_probability)
            for _ in range(number_of_stations):
                if random.random() < p[it]:
                    signals += 1
        simulation_results.append(first_single_slot)
    return simulation_results


def simulation_average(simulation_results):
    return statistics.mean(simulation_results)


def main():
    if len(sys.argv) >= 4:
        number_of_stations = int(sys.argv[1])
        max_number_of_stations = int(sys.argv[2])
        samples = int(sys.argv[3])
    else:
        number_of_stations = 500
        max_number_of_stations = 1000
        samples = 100
    print(
        simulation_average(
            simulate(number_of_stations, max_number_of_stations, samples)))


if __name__ == "__main__":
    main()
