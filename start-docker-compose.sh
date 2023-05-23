env=".env-non-dev"
docker_compose="docker-compose.yml"

cp -rf $env backend/$env
sudo docker-compose -f $docker_compose up