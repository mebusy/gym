# gym

docker gym environment

- python3.8
- numpy
- gym , so far , only [atari game] installed.
- pytorch
- tensorboard
  - docker run -p 0.0.0.0:6006:6006 ...
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


