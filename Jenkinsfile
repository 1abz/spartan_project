pipeline {
agent any
environment {
IMAGE_NAME =
}


stages {
stage('Cloning the project from GitHub'){
steps {
git branch: 'main',
url: 'https://github.com/1abz/spartan_project.git'
}
}



stage('Build Docker Image') {
steps{
script {
DOCKER_IMAGE = docker.build '1abz/mongo_spartan'
}
}
}
stage("Push to Docker Hub"){
steps {
script {
docker.withRegistry('', 'docker_hub_cred'){
DOCKER_IMAGE.push()
}
}
}
}
}
}