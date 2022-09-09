# Dockerfile for running the coroutines program on Alpine Linux using Python 3.8
# Author: Andrew Jarombek
# Date: 9/9/2022

FROM python:3.8-alpine

LABEL maintainer="andrew@jarombek.com" \
      version="1.0.0" \
      description="Dockerfile for the SaintsXCTF API for local development"

WORKDIR src
COPY . .

CMD ["-c", ". ./run.sh"]
ENTRYPOINT ["/bin/sh"]