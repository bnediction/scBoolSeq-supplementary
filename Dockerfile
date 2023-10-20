FROM colomoto/colomoto-docker:2023-10-01

ARG IMAGE_NAME
ENV DOCKER_IMAGE=$IMAGE_NAME

USER root

RUN conda install -y \
        plotnine \
        umap-learn \
        scanpy \
        scboolseq==2.0\
    && conda clean -y --all && rm -rf /opt/conda/pkgs

RUN rm -rf /notebook/*
COPY --chown=user:user . /notebook/

USER user
