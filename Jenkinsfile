pipeline {
    agent any

    environment {
        IMAGE_NAME = "sujalkarale39/assignment2"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/SRCEM-AIML/C39_SujalKarale_Assignment2.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }
        stage('Login to Docker Hub') {
            steps {
                withCredentials([string(credentialsId: 'docker-hub-password', variable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u sujalkarale39 --password-stdin'
                }
            }
        }
        stage('Push Image to Docker Hub') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }
    }
}