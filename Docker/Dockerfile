FROM python:3.8-alpine

MAINTAINER golden_slime@hotmail.com

RUN apk add --update --no-cache musl-dev gcc zlib-dev jpeg-dev py3-numpy py3-scipy
ENV PYTHONPATH=/usr/lib/python3.8/site-packages

#  to solv 'include/python3.9/Python.h:11:10: fatal error: limits.h: No such file or directory'
# RUN apk add musl-dev gcc libffi-dev zlib-dev jpeg-dev cairo
RUN pip3 install gym

# change work directory
WORKDIR /opt/work

ENTRYPOINT ["python3"]


