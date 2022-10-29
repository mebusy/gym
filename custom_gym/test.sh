#!/bin/sh

set -e

docker run --name gym --rm -it -v `pwd`:/opt/work/ \
    -e DISPLAY=$DISPLAY \
    mebusy/gym ./cust_gym_test.py
