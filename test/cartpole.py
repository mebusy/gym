import gym
# import matplotlib
# matplotlib.use('tkagg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation

env = gym.make("CartPole-v1")
observation = env.reset()


fig = plt.gcf()
im = plt.imshow(env.render('rgb_array'), animated=True) # only call this once


def animate(frame):
    im.set_array(env.render('rgb_array'))
    
    # env.render( mode='rgb_array'  )
    # env.render()
    action = env.action_space.sample() # your agent here (this takes random actions)
    observation, reward, done, info = env.step(action)

    if done:
        observation = env.reset()

# frames=None -> def animate( frame = itertools.count )
anim = animation.FuncAnimation(fig, animate, frames=None, interval=50, blit=False)
plt.show()

env.close()



