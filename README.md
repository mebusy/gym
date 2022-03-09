# gym

docker gym environment

- python3.8
- numpy
- gym , so far , only [atari game] installed.
- pytorch
- tensorboard
  - docker run -p 6006:6006 ...
  - localhost:6006 to open tensorboard ?
- matplotlib


## Build Docker Image

```bash
$ docker build  -t dockergym:latest .
```

## Usage

```bash
$ docker run --rm  -v `pwd`:/opt/work/  dockergym <your>.py
```

Or just use **prebuilt** docker image

```bash
$ docker run --rm  -v `pwd`:/opt/work/  mebusy/gym  <your>.py
```

## GUI support

If you script is goinbg to render some GUI, e.g. gym's `env.render()`, you may need do some extra work.

On MacOSX, please follow this [guide](https://github.com/mebusy/notes/blob/master/dev_notes/docker_mac_gui_app.md)

And check the [cartpole example](./test/cartpole.py)

```bash
docker run --rm -it -v `pwd`:/opt/work/ -e DISPLAY=${your-ip}:0 -v /tmp/.X11-unix:/tmp/.X11-unix mebusy/gym <your>.py
 
```

