# FROM python:3.8-alpine
FROM python:3.8-slim

MAINTAINER golden_slime@hotmail.com

# musl-dev
# RUN apk add --update --no-cache cmake g++ make zlib-dev jpeg-dev py3-numpy py3-scipy 

# ENV PYTHONPATH=/usr/lib/python3.8/site-packages

RUN pip3 install gym atari-py  pyglet
# RUN pip3 install gym[all]

# change work directory
WORKDIR /opt/work

# ENTRYPOINT ["python3"]
CMD ["bash"]


