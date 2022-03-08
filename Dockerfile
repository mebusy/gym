# FROM python:3.8-alpine
FROM python:3.9-slim

MAINTAINER golden_slime@hotmail.com

# musl-dev
# RUN apk add --update --no-cache cmake g++ make zlib-dev jpeg-dev py3-numpy py3-scipy 

# ENV PYTHONPATH=/usr/lib/python3.8/site-packages

# RUN apt-get update && apt-get install python3-opengl

RUN pip3 install gym atari-py tensorboard torch==1.10.0+cpu torchvision==0.11.1+cpu  -f https://download.pytorch.org/whl/cpu/torch_stable.html # torchaudio==0.10.0+cpu

# RUN pip3 install gym[all]

# change work directory
WORKDIR /opt/work

ENTRYPOINT ["python"]
# CMD ["python"]


