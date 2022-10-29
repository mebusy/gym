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


# https://www.gymlibrary.dev/content/environment_creation/#registering-envs

# Apart from id and entrypoint, you may pass the following additional keyword arguments to register:

# max_episode_steps | int | None | The maximum number of steps that an episode can consist of. If not None, a TimeLimit wrapper is added
# reward_threshold | float | None | The reward threshold before the task is considered solved
# nondeterministic | bool | False | Whether this environment is non-deterministic even after seeding
# order_enforce | bool | True | Whether to wrap the environment in an OrderEnforcing wrapper
# autoreset | bool | False | Whether to automatically reset the environment when done (AutoResetWrapper)
# kwargs | dict | {} | Additional keyword arguments to pass to the environment class
