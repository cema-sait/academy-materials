---
name: Building Your Own Images
dependsOn: [docker_containerization.introduction_to_docker.02_basic_docker_operations]
tags: [docker, dockerfile, images, containerization]
learningOutcomes:
    - Understand Dockerfile instructions
    - Build custom container images
    - Apply Docker image best practices

---

# Building Your Own Images

## Understanding Dockerfiles

Common Dockerfile instructions:

-   `FROM` specifies the base image.
-   `WORKDIR` sets the working directory.
-   `COPY` and `ADD` copy files into the image.
-   `RUN` executes build-time commands.
-   `ENV` defines environment variables.
-   `EXPOSE` documents ports.
-   `CMD` and `ENTRYPOINT` define the default process.
-   `USER` controls which user runs the application.

## Building a simple application

Clone the sample repository:

``` bash
git clone https://github.com/nigelpoulton/psweb.git
```

Build an image:

``` bash
docker build -t psweb:latest .
```

Inspect:

``` bash
docker images
docker inspect psweb:latest
```

Run:

``` bash
docker run -d --name psweb -p 8080:8080 psweb:latest
```

## Multi-stage builds and best practices

-   Use multi-stage builds to reduce image size.
-   Add a `.dockerignore` file.
-   Remove unnecessary build dependencies.
-   Run applications as non-root users.

Example:

``` bash
docker build -t multi:client --target prod-client -f Dockerfile-final .
```
