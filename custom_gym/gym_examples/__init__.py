from gym.envs.registration import register

register(
    id="gym_examples/GridWorld-v0",  # used by gym.make()
    entry_point="gym_examples.envs:GridWorldEnv",  # path to the env `CLASS`
)


# register more
# register(
#     id="gym_examples/MyEnv-v0",
#     entry_point="gym_examples.envs:MyEnv",
# )
