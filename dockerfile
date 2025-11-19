FROM ghcr.io/prefix-dev/pixi:latest
WORKDIR /
RUN apt-get update && \
    apt-get install -y wget
RUN mkdir -p /opt/varkit/reference/
COPY src /opt/varkit/src
COPY pixi.toml /opt/varkit/
COPY wslconfig/wsl-distribution.conf wslconfig/wsl.conf wslconfig/oobe.sh /etc/
RUN chmod +x /etc/oobe.sh
RUN chmod 644 /etc/wsl-distribution.conf


    