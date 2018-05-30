# Usage with Docker

## Build the image
```sh
docker build -t the_bass/pytorch .
```

## Run bash
```sh
docker run -it --rm \
    -w /app \
    -v `pwd`:/app \
    the_bass/pytorch \
    bash
```
