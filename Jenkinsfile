pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
                bat 'C:\\Users\\rasha\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m tests.test_runner'

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