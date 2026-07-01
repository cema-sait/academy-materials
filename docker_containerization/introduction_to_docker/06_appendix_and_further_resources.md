---
name: Appendix and Further Resources
dependsOn: [docker_containerization.introduction_to_docker.05_multi-container_apps_with_docker_compose]
tags: [docker, containerization, kubernetes, podman, resources]
learningOutcomes:
- Understand key containerisation terminology
- Troubleshoot common Docker issues
- Prepare container images for offline environments
- Identify next steps beyond Docker
---

# Appendix and Further Resources

## Glossary

### Namespace

Linux namespaces partition system resources so groups of processes can
run in isolated environments.

Common namespaces include:

-   `PID` --- process isolation
-   `mount` --- filesystem isolation
-   `network` --- network interfaces and ports
-   `UTS` --- hostnames
-   `IPC` --- inter-process communication
-   `user` --- UID/GID mappings

Docker uses namespaces to provide each container with its own view of
the operating system.

### cgroup (control group)

A cgroup is a Linux kernel feature used to organise processes and
control resource usage.

Docker uses cgroups to manage:

-   CPU limits
-   Memory limits
-   I/O resources

### OCI (Open Container Initiative)

OCI defines standards for:

-   Container images
-   Container runtimes
-   Container distribution

These standards allow containers to run consistently across different
platforms.

### Buildx

Buildx extends Docker builds using the BuildKit backend.

It provides features such as:

-   Multi-platform builds
-   Improved caching
-   Advanced build workflows

Example:

``` bash
docker buildx build --platform linux/amd64,linux/arm64 .
```

### Registry

A registry stores and distributes container images.

Examples:

-   Docker Hub
-   Private registries

Images are organised using repositories and tags:

    registry/namespace/name:tag

### Tag

A tag identifies a specific version or variant of an image.

Example:

``` bash
ubuntu:22.04
```

If no tag is provided, Docker uses:

    latest

## Troubleshooting

### Port already in use

This occurs when a container attempts to bind to a host port already
used by another process.

Check running containers:

``` bash
docker ps
```

Stop conflicting containers:

``` bash
docker stop <container-id>
```

You can also identify host processes using:

``` bash
lsof -i :8080
```

### Permission denied when accessing Docker daemon

This usually means the current user cannot access the Docker socket.

Verify Docker status:

``` bash
docker info
```

A common fix on Linux is adding the user to the Docker group:

``` bash
sudo usermod -aG docker $USER
```

Log out and back in afterwards.

### Unsupported platform or architecture mismatch

Images are built for specific CPU architectures.

For example:

-   `linux/amd64`
-   `linux/arm64`

Specify a platform when required:

``` bash
docker run --platform=linux/arm64 <image>
```

## Offline preparation

### Export images

Save an image to a tar archive:

``` bash
docker save -o myapp.tar myapp:latest
```

Compress:

``` bash
docker save myapp:latest | gzip > myapp.tar.gz
```

### Import images

Load an image archive:

``` bash
docker load --input myapp.tar
```

### Local registry

Run a local registry:

``` bash
docker run -d -p 5000:5000 --name registry registry:2.7
```

Tag an image:

``` bash
docker tag ubuntu localhost:5000/ubuntu
```

Push:

``` bash
docker push localhost:5000/ubuntu
```

## Next steps

### Kubernetes

Kubernetes provides orchestration for container workloads.

It can:

-   Deploy containers
-   Replace failed workloads
-   Scale applications
-   Manage resources across clusters

Docker builds and runs containers, while Kubernetes coordinates them at
scale.

### Podman

Podman provides an alternative container workflow.

Podman supports:

-   Rootless containers
-   Pods
-   Docker-compatible commands

Example:

``` bash
podman pod create --name mypod
```

## Further learning

Recommended resources:

-   Docker official documentation: https://docs.docker.com/

-   Nigel Poulton's Docker Deep Dive for deeper coverage of:

    -   Container internals
    -   Networking
    -   Storage
    -   Image management

-   Kubernetes documentation: https://kubernetes.io/
