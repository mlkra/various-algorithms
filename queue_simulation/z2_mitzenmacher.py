from dataclasses import dataclass, field
from heapq import heappush, heappop
from random import expovariate


@dataclass(order=True)
class Customer:
    priority: int
    has_arrived: bool = field(compare=False)
    arrival_time: float = field(compare=False)
    completion_time: float = field(compare=False)


class Simulation:
    def __init__(self, n: int, t: float, arrival_mean: float, uniform: bool):
        self.n = n
        self.max_t = t
        self.al = arrival_mean
        self.sl = 1
        self.customers_count = [0 for _ in range(n)]
        self.uniform = uniform

    def start(self):
        completed_customers = []
        for _ in range(self.n):
            pq = []
            q = []
            t = 0
            at = expovariate(self.al)
            heappush(pq, Customer(at, False, at, -1))
            while t < self.max_t:
                c: Customer = heappop(pq)
                t = c.priority
                if not c.has_arrived:
                    c.has_arrived = True
                    at = t + expovariate(self.al)
                    nc = Customer(at, False, at, -1)
                    heappush(pq, nc)
                    if not q:
                        if self.uniform:
                            c.completion_time = t + 1
                        else:
                            c.completion_time = t + expovariate(self.sl)
                        c.priority = c.completion_time
                        heappush(pq, c)
                        q.append(c)
                    else:
                        q.append(c)
                else:
                    q.pop(0)
                    completed_customers.append(c)
                    if q:
                        c = q[0]
                        c.has_arrived = True
                        if self.uniform:
                            c.completion_time = t + 1
                        else:
                            c.completion_time = t + expovariate(self.sl)
                        c.priority = c.completion_time
                        heappush(pq, c)
        # print(completed_customers)
        return sum([c.completion_time - c.arrival_time for c in completed_customers]) / len(completed_customers)


if __name__ == "__main__":
    print("lambda: 0.5")
    s = Simulation(100, 10000, 0.5, False)
    print(s.start())
    s = Simulation(100, 10000, 0.5, True)
    print(s.start())
    print("lambda: 0.8")
    s = Simulation(100, 10000, 0.8, False)
    print(s.start())
    s = Simulation(100, 10000, 0.8, True)
    print(s.start())
    print("lambda: 0.9")
    s = Simulation(100, 10000, 0.9, False)
    print(s.start())
    s = Simulation(100, 10000, 0.9, True)
    print(s.start())
    print("lambda: 0.99")
    s = Simulation(100, 10000, 0.99, False)
    print(s.start())
    s = Simulation(100, 10000, 0.99, True)
    print(s.start())
