import gym

env = gym.make("CartPole-v0")
env.reset()
while True:
    env.render()
    # env.step(env.action_space.sample())  # take a random action
env.close()
