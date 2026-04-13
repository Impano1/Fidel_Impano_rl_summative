import gymnasium as gym
from gymnasium import spaces
import numpy as np
from environment.rendering import render_env

class TrafficEnv(gym.Env):
    def __init__(self):
        super(TrafficEnv, self).__init__()

        self.action_space = spaces.Discrete(3)

        self.observation_space = spaces.Box(
            low=0, high=100, shape=(6,), dtype=np.float32
        )

        self.reset()

    def reset(self, seed=None, options=None):
        self.cars = np.random.randint(0, 10, size=4)
        self.light = 0
        self.time = 0
        return self._get_obs(), {}

    def _get_obs(self):
        return np.array([
            self.cars[0], self.cars[1],
            self.cars[2], self.cars[3],
            self.light,
            self.time
        ], dtype=np.float32)

    def step(self, action):
        prev_light = self.light
        self.light = action

        arrivals = np.random.randint(0, 3, size=4)
        self.cars += arrivals

        cars_passed = 0

        if self.light == 0:
            cars_passed = min(self.cars[0], 3) + min(self.cars[1], 3)
            self.cars[0] -= min(self.cars[0], 3)
            self.cars[1] -= min(self.cars[1], 3)

        elif self.light == 1:
            cars_passed = min(self.cars[2], 3) + min(self.cars[3], 3)
            self.cars[2] -= min(self.cars[2], 3)
            self.cars[3] -= min(self.cars[3], 3)

        reward = -np.sum(self.cars) + (cars_passed * 2)

        if prev_light != action:
            reward -= 1

        self.time += 1
        done = self.time >= 200

        return self._get_obs(), reward, done, False, {}

    def render(self):
        render_env(self.cars, self.light)