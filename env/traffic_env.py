import gymnasium as gym
from gymnasium import spaces
import numpy as np

class TrafficEnv(gym.Env):
    def __init__(self):
        super(TrafficEnv, self).__init__()

        self.observation_space = spaces.Box(low=0, high=50, shape=(4,), dtype=np.float32)
        self.action_space = spaces.Discrete(2)

        self.reset()

    def reset(self, seed=None, options=None):
        self.state = np.random.randint(0, 10, size=(4,))
        self.light_state = 0
        self.timer = 0
        return self.state.astype(np.float32), {}

    def step(self, action):
        self.timer += 1

        # Realistic traffic light cycle
        if self.timer % 20 == 0:
            self.light_state = (self.light_state + 1) % 4

        arrivals = np.random.poisson(2, size=4)
        self.state += arrivals

        if self.light_state == 0:
            self.state[0] = max(0, self.state[0] - 4)
            self.state[1] = max(0, self.state[1] - 4)

        elif self.light_state == 2:
            self.state[2] = max(0, self.state[2] - 4)
            self.state[3] = max(0, self.state[3] - 4)

        reward = -np.sum(self.state)

        return self.state.astype(np.float32), reward, False, False, {}