import matplotlib.pyplot as plt

class Dashboard:
    def __init__(self):
        self.rewards = []

    def update(self, reward):
        self.rewards.append(reward)

    def show(self):
        plt.clf()
        plt.plot(self.rewards)
        plt.title("Traffic Congestion Over Time")
        plt.xlabel("Steps")
        plt.ylabel("Reward")
        plt.pause(0.01)