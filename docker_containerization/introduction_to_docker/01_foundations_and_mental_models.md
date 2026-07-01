---
name: Foundations & Mental Models
dependsOn: [docker_containerization.introduction_to_docker.00_introduction]
tags: [docker, docker-compose, containerization, containers]
learningOutcomes:
  - Understand why containerisation is useful and how it differs from virtual machines
  - Understand core Docker concepts including images, containers, runtimes, registries and layers
  - Run and inspect Docker containers using basic CLI commands
---

# Foundations & Mental Models

The purpose of this module is to build the mental models required to
work effectively with containers.

By the end of this module, you should understand:

1.  Why containers exist and which problems they solve.
2.  How containers differ from traditional virtual machines.
3.  The relationship between images, containers, runtimes, and
    registries.
4.  How Docker packages applications into reproducible environments.

## Why containerisation?

Before containers, software environments were difficult to reproduce.
Developers often encountered the problem:

> "It works on my machine."

Containerisation addresses this by packaging applications together with
their dependencies into predictable, portable environments.

## Process isolation

Operating systems have long provided mechanisms to isolate processes.

On Unix/POSIX systems, process isolation allowed multiple applications
to run independently without interfering with each other.

## Filesystem isolation

`chroot` introduced early filesystem sandboxing by allowing processes to
see a restricted filesystem tree.

## Hardware virtualisation

Virtual machines provide strong isolation by running complete guest
operating systems.

Examples:

-   VMware
-   Hyper-V
-   VirtualBox

Virtual machines provide excellent isolation but require more resources
because each VM includes its own operating system.

## Kernel-level isolation

Linux introduced lightweight isolation primitives:

-   Namespaces isolate resources such as processes, networks, and
    filesystems.
-   cgroups control and limit resource usage such as CPU and memory.

## Containerisation and Docker

Docker combined these technologies into an easy-to-use developer
workflow.

Docker popularised:

-   A standard image format
-   Simple command-line tooling
-   Portable application packaging

Kubernetes later extended this model by providing large-scale container
orchestration.

## Core concepts

### Container

A container is a running instance of an image.

A container has:

-   Its own filesystem view
-   Its own process tree
-   Its own network configuration

### Image

An image is a read-only template used to create containers.

Images are built from layers:

    base image
        |
    application dependencies
        |
    application code

### Runtime

A container runtime executes container processes.

Examples:

-   `runc`
-   `containerd`

### Registry

A registry stores and distributes container images.

Examples:

-   Docker Hub
-   GitHub Container Registry

Images usually follow:

    registry/namespace/name:tag

# Hands-on exercises

## Running your first container

A container is created from an image. In this exercise, run a simple
Docker image and observe the container lifecycle.

::::challenge{id=docker_hello_world title="Run your first container"}

Run the Docker hello-world image:

``` bash
docker run hello-world
```

:::solution
Docker performs the following steps:

1.  Checks whether the image exists locally.
2.  Pulls the image from a registry if required.
3.  Creates a container from the image.
4.  Runs the container process.
5.  Stops the container after completion.

The container exits because the hello-world application only prints a
message and finishes.
:::

::::

## Running an interactive container

::::challenge{id=docker_alpine_shell title="Start an interactive Alpine container"}

Run an Alpine Linux container:

``` bash
docker pull alpine

docker run -it --rm alpine sh
```

Inside the container:

``` bash
ls
```

Exit:

``` bash
exit
```

:::solution
The `-it` flags provide an interactive terminal:

-   `-i` keeps stdin open.
-   `-t` allocates a terminal session.

The `--rm` flag removes the container automatically after it exits.
:::

::::

## Inspecting container information

::::challenge{id=docker_inspect title="Explore container configuration"}

Start a running NGINX container:

``` bash
docker run -d --name test-nginx nginx
```

Inspect the container:

``` bash
docker inspect test-nginx
```

Look for:

-   Filesystem information
-   Network configuration
-   Runtime settings

Remove the container:

``` bash
docker rm -f test-nginx
```

:::solution
`docker inspect` returns detailed JSON information about the container.

Important areas to explore:

-   `Mounts` shows storage configuration.
-   `NetworkSettings` shows networking details.
-   `Config` shows the image and command used.
:::

::::

## Wrapping up

You should now understand:

-   Why containerisation became necessary
-   How containers differ from virtual machines
-   The role of images, containers, runtimes, and registries
-   How to run and inspect Docker containers
