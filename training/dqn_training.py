import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from stable_baselines3 import DQN
from environment.custom_env import TrafficEnv

env = TrafficEnv()

model = DQN(
    "MlpPolicy",
    env,
    learning_rate=0.0005,
    gamma=0.99,
    buffer_size=10000,
    batch_size=64,
    verbose=1
)

model.learn(total_timesteps=50000)

model.save("models/dqn/traffic_dqn")

print("DQN Training Complete")