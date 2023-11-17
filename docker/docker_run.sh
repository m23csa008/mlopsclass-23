# Build the docker file 
sudo docker build -t digits:v1 -f ./docker/Dockerfile .
# Create out volume
sudo docker volume create trainmach
# Mount our volume to models directory (where train data is stored)
sudo docker run -v trainmach:/digits/models digits:v1

