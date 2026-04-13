from env.traffic_env import TrafficEnv
from stable_baselines3 import DQN

env = TrafficEnv()

model = DQN(
    "MlpPolicy",
    env,
    learning_rate=0.0005,
    buffer_size=50000,
    learning_starts=1000,
    batch_size=32,
    gamma=0.99,
    verbose=1
)

model.learn(total_timesteps=100000)
model.save("models/traffic_dqn")