#! /bin/bash
set -e
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
docker build -t varkit "$SCRIPT_DIR"
docker rm varkit
docker run -t --name varkit varkit ls /
mkdir -p /mnt/c/temp/
docker export varkit > /mnt/c/temp/varkit.tar
## dockerContainerID=$(docker container ls -a | grep -i varkit | awk '{print $1}')
## docker export $dockerContainerID > /mnt/c/temp/varkit.tar
