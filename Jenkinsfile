pipeline {
agent any

environment {
IMAGE_NAME = "1abz/mongo_spartan:1.0" + "$BUILD_NUMBER"
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
DOCKER_IMAGE = docker.build IMAGE_NAME
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