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
docker run --name gym --rm -it -v `pwd`:/opt/work/ \
    -e DISPLAY=${your-ip}:0 -v /tmp/.X11-unix:/tmp/.X11-unix \
    mebusy/gym <your>.py
```

## Run Tensorboard

suppose your pytorch training workdir named `results`, run following script under same directory of `results`.

```bash
docker run --name tensorboard --rm -it -v `pwd`:/opt/work/ \
    -e DISPLAY=${your-ip}:0 -v /tmp/.X11-unix:/tmp/.X11-unix \
    -p 6006:6006 \
    --entrypoint tensorboard  \
    mebusy/gym  --bind_all --logdir /opt/work/results
```
 
Now you can check training process via `http://localhost:6006/`




