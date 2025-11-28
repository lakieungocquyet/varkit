docker build -t varkit .
docker run -t --name varkit varkit ls /
docker export varkit > /mnt/c/temp/varkit.tar
## dockerContainerID=$(docker container ls -a | grep -i varkit | awk '{print $1}')
## docker export $dockerContainerID > /mnt/c/temp/varkit.tar


