---
name: Multi-container Apps with Docker Compose
dependsOn: [docker_containerization.introduction_to_docker.04_service_delivery_and_production_considerations]
tags: [docker, docker-compose, orchestration, containers]
learningOutcomes:
  - Understand Docker Compose fundamentals
  - Define multi-service applications
  - Manage application stacks
---

# Multi-container Apps with Docker Compose

## Compose fundamentals

A `compose.yml` file defines:

-   Services
-   Images or build contexts
-   Ports
-   Volumes
-   Networks
-   Dependencies

Example structure:

``` yaml
services:
  web:
    build: ./web
    ports:
      - "8080:80"
    depends_on:
      - redis

  redis:
    image: redis:latest
```

## Managing Compose applications

Start:

``` bash
docker compose up -d
```

View services:

``` bash
docker compose ps
```

Follow logs:

``` bash
docker compose logs -f
```

Stop:

``` bash
docker compose stop
```

Remove:

``` bash
docker compose down -v
```

## Hands-on exercise

::::challenge{id=docker_compose_multiservice title="Create and run a multi-service compose stack"}

Create your own `compose.yml` file for an application with multiple
services.

:::solution
A minimal successful outcome includes:

1. A `compose.yml` file with at least two services.
2. `docker compose up -d` starts all services.
3. `docker compose ps` shows services as running.
4. `docker compose down -v` tears down containers and volumes.

If one service depends on another, define `depends_on` to express startup order.
:::

::::
