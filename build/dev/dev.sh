#!/bin/sh

docker run -v $HOME:/root: -ti --network=host $@ /bin/bash
