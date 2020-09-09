import random
import sys


def simulate(number_of_stations, samples):
    beep_probability = 1 / number_of_stations
    simulation_results = []
    for _ in range(samples):
        signals = 0
        first_single_slot = 0
        while signals != 1:
            signals = 0
            first_single_slot += 1
            for _ in range(number_of_stations):
                if random.random() < beep_probability:
                    signals += 1
        simulation_results.append(first_single_slot)
    return simulation_results


def simulation_average(simulation_results):
    return sum(simulation_results) / len(simulation_results)


def main():
    if len(sys.argv) >= 3:
        number_of_stations = int(sys.argv[1])
        samples = int(sys.argv[2])
    else:
        number_of_stations = 1000
        samples = 10000
    print(simulation_average(simulate(number_of_stations, samples)))


if __name__ == "__main__":
    main()
