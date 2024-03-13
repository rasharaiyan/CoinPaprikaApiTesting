pipeline {
    agent any
    stages {
        // Other stages remain unchanged

        stage('Set up Python environment') {
            steps {
                bat 'python -m venv venv'                   // Create venv
                bat '.\\venv\\Scripts\\activate'            // Activate venv
                bat 'pip install -r requirements.txt'       // Install dependencies
            }
        }

        stage('Run API Tests') {
            steps {
                bat '.\\venv\\Scripts\\activate'            // Ensure venv is activated
                bat 'python -m unittest discover -s tests'  // Run tests
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
