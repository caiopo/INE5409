FROM ubuntu

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y octave

VOLUME /algorithms
WORKDIR /algorithms


CMD ["octave"]
