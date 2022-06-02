#!/usr/bin/env sh
IMG="pinellolab/stream:1.0"
docker pull "${IMG}"
(sleep 3; xdg-open "http://127.0.0.1:8989")&
docker run --rm --entrypoint /usr/bin/env -v "$PWD:/data" -w /data -p 8989:8888 -it \
    "${IMG}" jupyter notebook --ip 0.0.0.0 --port 8888 --no-browser --allow-root \
    --NotebookApp.token=
