pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
                bat 'C:\\Users\\rasha\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m api_tests.test_runner'

            }
        }
    }
}