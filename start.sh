environment=dev
date=$(date '+%Y-%m-%d-%H-%M')

echo "creating docker image"
docker build -t spotter .

### Complete Deployment
echo "killing the running docker"
docker ps -a | egrep 'spotter' | awk '{print $1}'| xargs docker kill
docker ps -a | egrep 'spotter' | awk '{print $1}'| xargs docker rm


echo "running the Travel Api using docker"
docker run -d --restart=unless-stopped --name spotter-cn -p 8000:8000 spotter

echo "We are done !"
