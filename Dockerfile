FROM colomoto/colomoto-docker:2024-06-01

ARG IMAGE_NAME
ENV DOCKER_IMAGE=$IMAGE_NAME

USER root

RUN rm -rf /notebook/*
COPY --chown=user:user . /notebook/

RUN pip install -r requirements.txt


USER user
