#!/bin/bash

docker run -d \
  -it \
  --name devtest \
  --mount type=bind,source="$(pwd)",target=/dart \
  google/dart:2.5