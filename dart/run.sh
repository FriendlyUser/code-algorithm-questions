#!/bin/bash

docker run -d \
  -it \
  --name dart_doc \
  --mount type=bind,source="$(pwd)",target=/dart \
  google/dart:2.5