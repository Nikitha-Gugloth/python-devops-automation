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
                bat '"C:\\Users\\maruthi\\AppData\\Local\\Programs\\Docker\\Docker\\resources\\bin\\docker.exe" build -t python-devops-automation .'
            }
        }

        stage('Run Application') {
            steps {
                bat '"C:\\Users\\maruthi\\AppData\\Local\\Programs\\Docker\\Docker\\resources\\bin\\docker.exe" run --rm python-devops-automation'
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