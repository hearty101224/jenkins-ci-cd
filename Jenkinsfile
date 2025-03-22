pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-token',
                    url: 'https://github.com/hearty101224/jenkins-ci-cd.git'
            }
        }

        stage('Build') {
            steps {
                echo "Building the application..."
                bat 'python app.py'  // Print output in Jenkins Console
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest discover || echo "Tests failed, but continuing..."'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying the application..."
            }
        }
    }
}
