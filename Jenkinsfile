pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                bat 'C:\Users\rasha\AppData\Local\pip install selenium requests'
            }
        }

        stage('Build') {
            steps {
                echo 'Building..'
                // Your build steps here
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                bat 'C:\Users\rasha\AppData\Local\Programs\Python\Python312\python.exe -m testing_layer.api_tests.password_tests_api'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying..'
                // Your deployment steps here
            }
        }
    }
}