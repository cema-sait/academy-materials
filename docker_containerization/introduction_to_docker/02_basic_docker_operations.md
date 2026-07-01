---
name: Basic Docker Operations
dependsOn: [docker_containerization.introduction_to_docker.01_foundations_and_mental_models]
tags: [docker, docker-compose, containerization, containers]
learningOutcomes:
    - Verify a Docker or Podman installation
    - Run, inspect, manage, and troubleshoot containers
    - Understand common Docker CLI operations

---

# Basic Docker Operations

## Installing and verifying your environment

-   Confirm that Docker or Podman is installed and running.

``` bash
docker info
```

-   List local images:

``` bash
docker images
```

-   Pull images:

``` bash
docker pull <name>:<tag>
```

-   List containers:

``` bash
docker ps -a
```

## Working with containers

Start an interactive Ubuntu container:

``` bash
docker run -it --name myubuntu ubuntu:latest bash
```

Detach without stopping:

    Ctrl+p Ctrl+q

Attach again:

``` bash
docker attach myubuntu
```

Stop and remove:

``` bash
docker stop myubuntu
docker rm myubuntu
```

Execute commands inside a running container:

``` bash
docker exec -it <container> <command>
```

Inspect containers and images:

``` bash
docker inspect <image_or_container>
docker history <image>
```

## Hands-on exercise

::::challenge{id=docker_nginx_lifecycle title="Run and inspect an NGINX container"}

Run an NGINX web server:

``` bash
docker run -d -p 8080:80 nginx:latest
```

Open:

    http://localhost:8080

View logs:

``` bash
docker logs <container>
```

Clean up:

``` bash
docker rm -f <container>
```

:::solution
You should verify three outcomes:

1. The container is reachable at `http://localhost:8080`.
2. `docker logs <container>` shows NGINX startup and request logs.
3. `docker rm -f <container>` removes the container cleanly.

You can discover the container id or name using `docker ps`.
:::

::::
