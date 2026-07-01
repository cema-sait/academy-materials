---
name: Introduction
dependsOn: [docker_containerization.introduction_to_docker]
tags: [docker, docker-compose, containerization]
learningOutcomes:
  - Understand Docker fundamentals
  - Install Docker Desktop or Podman Desktop and verify the installation
---

## Objectives

- Understand why containerisation matters and how it compares with virtual machines and other isolation techniques.
- Familiarise yourself with key concepts: containers, images, runtimes, registries, layers, and naming conventions.
- Gain hands-on experience with Docker commands and container operations.
- Learn to package your own applications into images using Dockerfiles and best practices.
- Explore multi-container orchestration using Docker Compose.
- Prepare for offline environments and next steps beyond this workshop.

## Pre-workshop setup

- Install Docker Desktop or Podman Desktop on your machine before arriving. For Windows, ensure WSL 2 is enabled; for Linux and macOS, follow the platform-specific instructions.
- Verify installation with `docker --version` or `podman --version`.
- Pull the following images ahead of time so they are available offline: `alpine`, `nginx`, `redis`, `busybox`, and the sample application image provided by the instructor.
- If internet access is unavailable during the workshop, use a local registry or share images over the workshop network.
- All illustrations are based on the following repository:  
  [Docker Deep Dive multi-container examples](https://github.com/nigelpoulton/ddd-book/tree/main/multi-container)

> The material for this workshop has been prepared based on *Docker Deep Dive: Zero to Docker in a Single Book* by Nigel Poulton. You can get a copy [here](https://leanpub.com/dockerdeepdive). An older version (2018) is available [here](https://ebooks.karbust.me/Technology/Docker%20Deep%20Dive%20-%20Nigel%20Poulton.pdf), but it may exclude recent additions to Docker.