import gym
import sys

import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt

# plt.plot([1, 2, 3])
# plt.show()

env = gym.make("CartPole-v1")
observation = env.reset()

im = None
for i in range(1000):
    plt.figure(3)
    plt.clf()
    img = env.render(mode='rgb_array')
    # plt.axis('off')
    if i==0:
        im = plt.imshow(img)
        # plt.show()
    else:
        im.set_array(img)

    # display.clear_output(wait=True)
    action = env.action_space.sample() # your agent here (this takes random actions)
    observation, reward, done, info = env.step(action)

    if done:
        observation = env.reset()

plt.show()
env.close()

if True:
    sys.exit(1)

from pyvirtualdisplay import Display
display = Display(visible=0, size=(1400, 900))
display.start()


