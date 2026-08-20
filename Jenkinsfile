pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker build -t python-devops-automation .'
            }
        }

        stage('Run Application') {
            steps {
                bat 'docker run --rm python-devops-automation'
            }
        }
    }

    post {
        success {
            echo 'BUILD SUCCESSFUL - Python DevOps project completed!'
        }

        failure {
            echo 'BUILD FAILED - Please check the console output.'
        }
    }
}