# scBoolSeq notebooks

These notebooks demonstrate [scBoolSeq](https://github.com/bnediction/scBoolSeq) for scRNA-Seq binarization and synthetic generation from Boolean dynamical models.

The notebooks can be visualized and downloaded at https://nbviewer.org/github/bnediction/scBoolSeq-supplementary.

Their execution require scBoolSeq installed (see https://github.com/bnediction/scBoolSeq#installation) and Python packages listed in the file `requirements.txt`. Alternatively, they can be executed interactively within the [Docker](https://docs.docker.com/get-docker/) image `bnediction/scboolseq:v1`, with the following command:
```sh
sudo python -m pip install -U colomoto-docker
colomoto-docker --image bnediction/scboolseq -V v1
```

:warning: The notebooks `3.X - STREAM - ...` and `Variable Gene Selection ...` must be executed within a STREAM environment (which is not included in the above mentioned Docker image).
They can be be executed within the STREAM Docker distribution:
```sh
docker run --rm --entrypoint /usr/bin/env -v "$PWD/../:/data" -w /data -p 8989:8888 -it \
    pinellolab/stream:1.0 jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser --allow-root \
    --NotebookApp.token=
```
Then go to http://127.0.0.1:8989

