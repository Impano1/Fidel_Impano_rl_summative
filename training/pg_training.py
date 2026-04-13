import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from stable_baselines3 import PPO, A2C
from environment.custom_env import TrafficEnv

env = TrafficEnv()

# ---------------- PPO ----------------
ppo = PPO(
    "MlpPolicy",
    env,
    learning_rate=0.0003,
    gamma=0.99,
    verbose=1
)

ppo.learn(total_timesteps=50000)
ppo.save("models/pg/traffic_ppo")

# ---------------- A2C ----------------
a2c = A2C(
    "MlpPolicy",
    env,
    learning_rate=0.0007,
    gamma=0.99,
    verbose=1
)

a2c.learn(total_timesteps=50000)
a2c.save("models/pg/traffic_a2c")

print("PG Training Complete")