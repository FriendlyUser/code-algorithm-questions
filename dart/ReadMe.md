Create Docker Compose File to bind files lol.

```sh
docker run -d \
  -it \
  --name devtest \
  --mount type=bind,source="$(pwd)"/target,target=/dart \
  google/dart
```

```bat 
docker run -d -it --name devtest --mount type=bind,source="$(pwd)"/target,target=/dart google/dart
```
Use `docker ps -a` to find all the active docker images.
