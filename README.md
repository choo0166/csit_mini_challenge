# csit_mini_challenge
REST API built with Flask for CSIT Mini Challenge July 2023

## Setup
Build image with Dockerfile:
```sh
docker build -t csit_mini_challenge:v001 .
```

Run image:
```sh
docker run -it -p 127.0.0.1:8080:8080 csit_mini_challenge:v001
```

Test API:

Navigate to `127.0.0.1:8080`.
