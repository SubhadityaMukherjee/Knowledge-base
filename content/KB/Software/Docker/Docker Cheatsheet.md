---
toc: true
title: Docker Cheatsheet
tags:
  - cheatsheets
date modified: Tuesday 16th January 2024, Tue
date created: Tuesday 16th January 2024, Tue
---

# Docker Cheatsheet


## Minimal Workflow
```
docker init
docker compose up --build
docker compose up --build -d #run_in_background
docker compose down #stop
```

## Managing Containers
|                                  Name                                  |                                       Command                                       |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
|                          Starting Containers                           |                            docker container start nginx                             |
|                          Stopping Containers                           |                             docker container stop nginx                             |
|                         Restarting Containers                          |                           docker container restart nginx                            |
|                           Pausing Containers                           |                            docker container pause nginx                             |
|                          Unpausing Containers                          |                           docker container unpause nginx                            |
|                          Blocking a Container                          |                             docker container wait nginx                             |
|                       Sending SIGKILL Containers                       |                             docker container kill nginx                             |
|                         Sending another signal                         |                         docker container kill -s HUP nginx                          |
|                  Connecting to an Existing Container                   |                            docker container attach nginx                            |
|                          Check the Containers                          |                                      docker ps                                      |
|                     To see all running containers                      |                                 docker container ls                                 |
|                             Container Logs                             |                                docker logs infinite                                 |
|                       ‘tail -f’ Containers’ Logs                       |                          docker container logs infinite -f                          |
|                         Inspecting Containers                          |                          docker container inspect infinite                          |
|                   Inspecting Containers for certain                    | docker container inspect –format ‘{{ .NetworkSettings.IPAddress }}’ $(docker ps -q) |
|                           Containers Events                            |                            docker system events infinite                            |
|                     docker system events infinite                      |                           docker container port infinite                            |
|                           Running Processes                            |                            docker container top infinite                            |
|                        Container Resource Usage                        |                           docker container stats infinite                           |
| Inspecting changes to files or directories on a container’s filesystem |                           docker container diff infinite                            

## Manage Images
| Name | Command |
| ---- | ---- |
| Listing Images | docker image ls |
| Building Images | docker build. |
| From a Remote GIT Repository | docker build github.com/creack/docker-firefox |
| Instead of Specifying a Context, You Can Pass a Single Dockerfile in the URL or Pipe the File in via STDIN | docker build – < Dockerfile |
| Building and Tagging | docker build -t eon/infinite. |
| Building a Dockerfile while Specifying the Build Context | docker build -f myOtherDockerfile. |
| Building from a Remote Dockerfile URI | curl example.com/remote/Dockerfile\|docker build -f – . |
| Removing an Image | docker image rm nginx |
| Loading a Tarred Repository from a File or the Standard Input Stream | docker image load < ubuntu.tar.gz |
| Saving an Image to a Tar Archive | docker image save busybox > ubuntu.tar |
| Showing the History of an Image | docker image history |
| Creating an Image From a Container | docker container commit nginx |
| Tagging an Image | docker image tag nginx eon01/nginx |
| Pushing an Image | docker image push eon01/nginx |

## Removing Images
| Name | Command |
| ---- | ---- |
| Removing a Running Container | docker container rm nginx |
| Removing a Container and its Volume | docker container rm -v nginx |
| Removing all Exited Containers | docker container rm $(docker container ls -a -f status=exited -q) |
| Removing All Stopped Containers | docker container rm `docker container ls -a -q` |
| Removing a Docker Image | docker image rm nginx |
| Removing Dangling Images | docker image rm $(docker image ls -f dangling=true -q) |
| Removing all Images | docker image rm $(docker image ls -a -q) |
| Removing all Untagged Images | docker image rm -f $(docker image ls \|grep “^”\|awk “{print $3}”) |
| Stopping & Removing all Containers | docker container stop $(docker container ls -a -q) && docker container rm $(docker container ls -a -q) |
| Removing Dangling Volumes | docker volume rm $(docker volume ls -f dangling=true -q) |
| Removing all unused (containers, images, networks and volumes) | docker system prune -f |
| Clean all | docker system prune -a |

## Dockerfile Commands
|  Command   |                                           Description                                            |                    Example                    |
|------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------|
|    FROM    |                              Specifies the base image for the build                              |              FROM ubuntu:latest               |
|    RUN     |                    Executes a command inside the container during build time                     | RUN apt-get update && apt-get install -y curl |
|    CMD     |                  Specifies the default command to run when the container starts                  |             CMD [“npm”, “start”]              |
|   EXPOSE   |          Informs Docker that the container listens on specific network ports at runtime          |                 EXPOSE 80/tcp                 |
|    ENV     |                         Sets environment variables inside the container                          |            ENV NODE_ENV=production            |
|    COPY    |              Copies files or directories from the build context into the container               |           COPY app.js /usr/src/app/           |
|    ADD     |      Similar to COPY but supports additional features like URL retrieval and decompression       | ADD https://example.com/file.tar.gz /usr/src/ |
|  WORKDIR   |                      Sets the working directory for subsequent instructions                      |             WORKDIR /usr/src/app              |
|    ARG     | Defines variables that users can pass at build-time to the builder with the docker build command |                ARG VERSION=1.0                |
| ENTRYPOINT |                          Configures a container to run as an executable                          |        ENTRYPOINT [“python”, “app.py”]        |
|   VOLUME   |                    Creates a mount point and assigns it to a specified volume                    |                 VOLUME /data                  |
|    USER    |                        Sets the user or UID to use when running the image                        |                 USER appuser                  |
|   LABEL    |                     Adds metadata to an image in the form of key-value pairs                     |   LABEL version=”1.0″ maintainer=”John Doe    |
|  ONBUILD   |         Configures commands to run when the image is used as the base for another build          |            ONBUILD ADD . /app/src             |

## Volume Commands
|    Command     |                 Description                  |           Example            |
|----------------|----------------------------------------------|------------------------------|
| volume create  |            Creates a named volume            | docker volume create mydata  |
|   volume ls    |         Lists the available volumes          |       docker volume ls       |
| volume inspect | Displays detailed information about a volume | docker volume inspect mydata |
|   volume rm    |         Removes one or more volumes          |   docker volume rm mydata    |
|  volume prune  |          Removes all unused volumes          |     docker volume prune      |
