from gym.envs.registration import register

register(
    id="gym_examples/GridWorld-v0",
    entry_point="gym_examples.envs:GridWorldEnv",
)


# register more
# register(
#     id="gym_examples/MyEnv-v0",
#     entry_point="gym_examples.envs:MyEnv",
# )
