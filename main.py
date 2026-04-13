import pygame
from stable_baselines3 import DQN
from env.traffic_env import TrafficEnv
from visualization.simulator import Simulator
from dashboard.dashboard import Dashboard

env = TrafficEnv()
model = DQN.load("models/traffic_dqn")

sim = Simulator()
dash = Dashboard()

state, _ = env.reset()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    action, _ = model.predict(state)
    state, reward, _, _, _ = env.step(action)

    sim.spawn_cars(state)
    sim.update_cars()
    sim.draw(env.light_state)

    dash.update(reward)
    dash.show()

pygame.quit()