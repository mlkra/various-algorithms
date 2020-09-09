import math
import sys
from statistics import mean, variance

import matplotlib.pyplot as plt
import numpy as np

import simulator1 as s1
import simulator2 as s2

NUMBER_OF_STATIONS = 1000
SAMPLES = 10000

MAX_NUMBER_OF_STATIONS = 1024
SAMPLES2 = 10000


def generate_histograms():
    data1 = s1.simulate(NUMBER_OF_STATIONS, SAMPLES)
    # print(data1)
    plt.hist(data1, bins=range(1, max(data1) + 1))
    plt.title(str(NUMBER_OF_STATIONS) + " stations")

    plt.figure()

    data2 = s2.simulate(2, MAX_NUMBER_OF_STATIONS, SAMPLES2)
    plt.hist(data2, bins=range(1, max(data2) + 1))
    plt.title("No more than " + str(MAX_NUMBER_OF_STATIONS)
              + " stations, 2 stations")

    plt.figure()

    number_of_stations = round(MAX_NUMBER_OF_STATIONS / 2) 
    data3 = s2.simulate(number_of_stations, MAX_NUMBER_OF_STATIONS, SAMPLES2)
    plt.hist(data3, bins=range(1, max(data3) + 1))
    # plt.hist(data3)
    plt.title("No more than " + str(MAX_NUMBER_OF_STATIONS) + " stations, "
              + str(number_of_stations) + " stations")

    plt.figure()

    data4 = s2.simulate(
        MAX_NUMBER_OF_STATIONS, MAX_NUMBER_OF_STATIONS, SAMPLES2)
    plt.hist(data4, bins="auto")
    plt.title("No more than " + str(MAX_NUMBER_OF_STATIONS) + " stations, "
              + str(MAX_NUMBER_OF_STATIONS) + " stations")


def calculate_e_and_var():
    data = s1.simulate(NUMBER_OF_STATIONS, SAMPLES)
    print(str(NUMBER_OF_STATIONS) + " stations: " + str(mean(data)) + " "
          + str(variance(data)))

    data = s2.simulate(2, MAX_NUMBER_OF_STATIONS, SAMPLES2)
    print(str(2) + " stations, " + str(MAX_NUMBER_OF_STATIONS) + " max: "
          + str(mean(data)) + " " + str(variance(data)))

    number_of_stations = round(MAX_NUMBER_OF_STATIONS / 2)
    data = s2.simulate(number_of_stations, MAX_NUMBER_OF_STATIONS, SAMPLES2)
    print(str(number_of_stations) + " stations, " + str(MAX_NUMBER_OF_STATIONS)
          + " max: " + str(mean(data)) + " " + str(variance(data)))

    data = s2.simulate(MAX_NUMBER_OF_STATIONS, MAX_NUMBER_OF_STATIONS,
                       SAMPLES2)
    m = mean(data)
    print(str(MAX_NUMBER_OF_STATIONS) + " stations, "
          + str(MAX_NUMBER_OF_STATIONS) + " max: " + str(m) + " "
          + str(variance(data, m)))


def main():
    if len(sys.argv) >= 2:
        option = sys.argv[1]
    else:
        option = "a"
    
    if option == "a":
        generate_histograms()
        plt.show()
    elif option == "b":
        calculate_e_and_var()


if __name__ == "__main__":
    main()
