# gym

docker gym environment

- Python 3.9-slim
- numpy
- gym , so far , only [atari game] installed.
- pytorch
    - tensorboard torch==1.12.0+cpu torchvision==0.13.0+cpu 
- tensorboard
  - docker run -p 6006:6006 ...
  - localhost:6006 to open tensorboard ?
- matplotlib


## Gym verison

gym version has been upgrade to 0.26.2 , if you want to 0.22.0,  use image `mebusy/gym:0.22` instead

## Build Docker Image

```bash
$ docker build  -t dockergym:latest .
```

## Usage

```bash
$ docker run --rm -it -v `pwd`:/opt/work/  dockergym <your>.py
```

Or just use **prebuilt** docker image

```bash
$ docker run --rm -it -v `pwd`:/opt/work/  mebusy/gym  <your>.py
```

## GUI support

If you script is goinbg to render some GUI, e.g. gym's `env.render()`, you may need do some extra work.

On MacOSX, please follow this [guide](https://github.com/mebusy/notes/blob/master/dev_notes/docker_mac_gui_app.md)

And check the [cartpole example](./test/cartpole.py)

```bash
# use xterm to enable GUI     -v /tmp/.X11-unix:/tmp/.X11-unix \
docker run --name gym --rm -it -v `pwd`:/opt/work/ \
    -e DISPLAY=${your-ip}:0 
    mebusy/gym <your>.py
```

## Run Tensorboard

suppose your pytorch training workdir named `results` (e.g. cs234), under the directory of `results`, 

run following script:

```bash
# use --entrypoint to override docker default entrypoint [python3]
# expose tensorboard port :6006
docker run --name tensorboard --rm -it -v `pwd`:/opt/work/ \
    -p 6006:6006 \
    --entrypoint tensorboard  \
    mebusy/gym  --bind_all --logdir /opt/work/results
```
 
Now you can check training process via `http://localhost:6006/`


# Install entire environment directly on MacOSX

<details>

```bah
pip3 install torch torchvision torchaudio
pip3 install pygame tensorboard matplotlib pyglet
pip3 install gym==0.22.0 'gym[accept-rom-license]'
```

</details>




