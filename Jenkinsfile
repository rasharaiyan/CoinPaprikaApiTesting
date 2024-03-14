pipeline {
    agent any

    environment {
        // Define the Docker image name
        IMAGE_NAME = 'tests'
        TAG = 'latest'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def customImage = docker.build("${IMAGE_NAME}:${TAG}")
                }
            }
        }

        stage('Run API Test') {
            steps {
                bat "docker run --name test_runner ${IMAGE_NAME}:${TAG} python test_runner.py"
                bat "docker rm api_test_runner"
            }
        }

         stage('Run Get Coin By ID') {
            steps {
                bat "docker run --name test_get_coin_by_id ${IMAGE_NAME}:${TAG} python test_get_coin_by_id.py"
                bat "docker rm test_get_coin_by_id"
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            bat "docker rmi ${IMAGE_NAME}:${TAG}"
 }
 }
}