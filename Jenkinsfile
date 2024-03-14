pipeline {
    agent any

    stages {
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'

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
                bat 'C:\\Users\\rasha\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m tests.test_get_coin_by_id'

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