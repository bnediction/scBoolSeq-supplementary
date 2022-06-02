FROM colomoto/colomoto-docker:2022-05-01

ARG IMAGE_NAME
ENV DOCKER_IMAGE=$IMAGE_NAME

USER root

RUN conda install -y plotnine

RUN conda install -y scboolseq==0.8.3

RUN rm -rf /notebook/*
COPY --chown=user:user models /notebook/models/
COPY --chown=user:user 1*.ipynb 2*.ipynb *.csv V*.ipynb /notebook/

USER user
