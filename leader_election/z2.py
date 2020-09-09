import math
import random

SAMPLES = 10000

def _probabilities(m):
    return [0.5**i for i in range(1, m + 1)]


def simulate_one_round(m, n):
    probabilities = _probabilities(m)
    for i in range(len(probabilities)):
        signals = 0
        for _ in range(n):
            if random.random() < probabilities[i]:
                signals += 1
        if signals == 1:
            return 1
    return 0


def calculate_lambda(m, n):
    successes = 0
    for _ in range(SAMPLES):
        successes += simulate_one_round(m, n)
    print(successes / SAMPLES)


def main():
    m = math.ceil(math.log2(64))
    print("u = 64, m = " + str(m))
    print("n = 2")
    calculate_lambda(m, 2)
    print("n = 25")
    calculate_lambda(m, 25)
    print("n = 60")
    calculate_lambda(m, 60)
    print("n = 64")
    calculate_lambda(m, 64)
    m = math.ceil(math.log2(256))
    print("u = 256, m = " + str(m))
    print("n = 2")
    calculate_lambda(m, 2)
    print("n = 25")
    calculate_lambda(m, 25)
    print("n = 100")
    calculate_lambda(m, 100)
    print("n = 200")
    calculate_lambda(m, 200)
    print("n = 256")
    calculate_lambda(m, 256)
    m = math.ceil(math.log2(10000))
    print("u = 10000, m = " + str(m))
    print("n = 2")
    calculate_lambda(m, 2)
    print("n = 25")
    calculate_lambda(m, 25)
    print("n = 100")
    calculate_lambda(m, 100)
    print("n = 500")
    calculate_lambda(m, 500)
    print("n = 800")
    calculate_lambda(m, 800)
    

if __name__ == "__main__":
    main()

