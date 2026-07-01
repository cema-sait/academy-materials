---
name: Service Delivery and Production Considerations
dependsOn: [docker_containerization.introduction_to_docker.03_building_your_own_images]
tags: [docker, security, production, containerization]
learningOutcomes:
  - Understand image layers and caching
  - Apply container security practices
  - Manage container resources and cleanup
---

# Service Delivery and Production Considerations

## Image layers and caching

Inspect image layers:

``` bash
docker history <image>
```

Build multi-platform images:

``` bash
docker buildx build --platform linux/amd64,linux/arm64 .
```

## Security and scanning

Recommended practices:

-   Keep base images updated.
-   Pin image versions.
-   Avoid running containers as root.
-   Remove unnecessary capabilities.

Scan images:

``` bash
docker scout <image>
```

## Operational tools

Copy files:

``` bash
docker cp
```

Manage storage and networks:

``` bash
docker volume ls
docker network ls
```

Cleanup:

``` bash
docker system prune
docker image prune
```

## Hands-on exercise

::::challenge{id=docker_non_root_image title="Run an image as a non-root user"}

Modify an application image to run as a non-root user and verify it
still works.

:::solution
One valid approach is:

1. Add a non-root user in the Dockerfile (for example using `RUN adduser` on Alpine-based images).
2. Set `USER <username>` near the end of the Dockerfile.
3. Rebuild and run the image.
4. Confirm the runtime user with a command such as `docker exec -it <container> id`.

The container should remain functional while avoiding root execution.
:::

::::
