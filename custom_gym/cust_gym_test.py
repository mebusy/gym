import gym
import gym_examples

env = gym.make("gym_examples/GridWorld-v0", render_mode="human")

print(env.reset())

# env.render()
while True:
    ob, *info = env.step(env.action_space.sample())  # take a random action
    # print(ob, info)
    env.render()
