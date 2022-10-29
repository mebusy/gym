import gym
import gym_examples

env = gym.make("gym_examples/GridWorld-v0")

print(env.reset())

# env.render()
while True:
    env.step(env.action_space.sample())  # take a random action
    # env.step(0)
    env.render()
