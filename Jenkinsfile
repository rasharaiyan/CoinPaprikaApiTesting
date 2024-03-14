pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def customImage = docker.build("my-python-app:test")
                    customImage.push()
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image("my-python-app:test").inside {
                        sh "python -m tests.test_runner"
                    }
                }
            }
        }
    }
}
