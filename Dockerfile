# FROM python:3.8-alpine
FROM python:3.9-slim

MAINTAINER golden_slime@hotmail.com

# musl-dev
# RUN apk add --update --no-cache cmake g++ make zlib-dev jpeg-dev py3-numpy py3-scipy 

# ENV PYTHONPATH=/usr/lib/python3.8/site-packages

RUN apt-get update -y && \
    apt-get install -y xvfb && \
    apt-get install -y python3-opengl

# atari-py
RUN pip3 install pygame gym  pyvirtualdisplay tensorboard torch==1.12.0+cpu torchvision==0.13.0+cpu  -f https://download.pytorch.org/whl/cpu/torch_stable.html # torchaudio==0.10.0+cpu

RUN pip install matplotlib pyglet
# RUN apt-get install -y tk-dev
RUN apt-get install -y python3-tk
# RUN apt-get install -y x11-utils

RUN pip3 install gym[atari,accept-rom-license]  #==0.21.0
# for more game enviroments 
#   https://towardsdatascience.com/how-to-render-openai-gym-on-windows-65767ab52ae2
# RUN apt-get install -y cmake && \
#     apt-get install -y zlib1g zlib1g-dev

# disable pygame sound
ENV SDL_VIDEODRIVER dummy

# change work directory
WORKDIR /opt/work

ENTRYPOINT ["python"]
# CMD ["python"]


