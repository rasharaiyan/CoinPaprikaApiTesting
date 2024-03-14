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
    }


        stage('Test') {
            steps {
                script {
                    docker.run("my-python-app:test", "python -m tests.test_runner")
                }
            }
        }

}

