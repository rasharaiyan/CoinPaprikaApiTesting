pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run API Tests') {
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'deactivate || true'
            sh 'rm -rf venv'
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed. Check console output for details.'
        }
    }
}
