import random

import matplotlib.pyplot as plt


class RealQueue:
    def __init__(self, limit: int, lm: float, mi: float):
        self.prev_state = 0
        self.currentState = 0
        self.t = 0
        self.limit = limit
        self.lm = lm
        self.mi = lm + mi
        self.mi2 = mi

    def advance_time(self):
        self.t += 1
        r = random.random()
        if self.currentState == 0:
            if r < self.lm:
                self.prev_state = self.currentState
                self.currentState = 1
        elif self.currentState == self.limit:
            if r < self.mi2:
                self.prev_state = self.currentState
                self.currentState -= 1
        else:
            if r < self.lm:
                self.prev_state = self.currentState
                self.currentState += 1
            elif r < self.mi:
                self.prev_state = self.currentState
                self.currentState -= 1


class StatRealQueue(RealQueue):
    def __init__(self, limit: int, lm: float, mi: float):
        RealQueue.__init__(self, limit, lm, mi)
        self.state_uniq_freq = {}
        self.state_uniq_freq[0] = 1
        self.state_freq = {}
        self.state_freq[0] = 1
        self.last_in_state = {}
        self.last_in_state[0] = 0
        self.duration_sum = {}
        self.duration_sum[0] = 0

    def advance_time(self):
        super().advance_time()
        if self.currentState in self.state_freq:
            self.state_freq[self.currentState] += 1
        else:
            self.state_freq[self.currentState] = 1
        if self.prev_state != self.currentState:
            if self.currentState in self.state_uniq_freq:
                self.state_uniq_freq[self.currentState] += 1
            else:
                self.state_uniq_freq[self.currentState] = 1
        if self.currentState in self.last_in_state:
            if self.currentState not in self.duration_sum:
                self.duration_sum[self.currentState] = 0
            self.duration_sum[self.currentState] += self.t - self.last_in_state[self.currentState]
        self.last_in_state[self.currentState] = self.t


if __name__ == "__main__":
    STEPS = 100000
    CAP = 100

    print("alpha = mi")
    q = StatRealQueue(CAP, 0.45, 0.45)
    for _ in range(STEPS):
        q.advance_time()
    for k in q.last_in_state.keys():
        if k in q.duration_sum.keys():
            q.duration_sum[k] += q.t - q.last_in_state[k]
    print(q.currentState)
    print(q.state_freq)
    print([(k, v / q.state_uniq_freq[k]) for k, v in q.duration_sum.items()])
    plt.figure()
    plt.scatter(q.state_freq.keys(), q.state_freq.values())
    plt.show()

    print("alpha < mi")
    q = StatRealQueue(CAP, 0.35, 0.6)
    for _ in range(STEPS):
        q.advance_time()
    for k in q.last_in_state.keys():
        if k in q.duration_sum.keys():
            q.duration_sum[k] += q.t - q.last_in_state[k]
    print(q.currentState)
    print(q.state_freq)
    print([(k, v / q.state_uniq_freq[k]) for k, v in q.duration_sum.items()])
    plt.figure()
    plt.scatter(q.state_freq.keys(), q.state_freq.values())
    plt.show()

    print("alpha > mi")
    q = StatRealQueue(CAP, 0.6, 0.35)
    for _ in range(STEPS):
        q.advance_time()
    for k in q.last_in_state.keys():
        if k in q.duration_sum.keys():
            q.duration_sum[k] += q.t - q.last_in_state[k]
    print(q.currentState)
    print(q.state_freq)
    print([(k, v / q.state_uniq_freq[k]) for k, v in q.duration_sum.items()])
    plt.figure()
    plt.scatter(q.state_freq.keys(), q.state_freq.values())
    plt.show()
