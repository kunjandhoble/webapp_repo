pipeline {
    agent { docker { image 'python:2.6.7' } }
    stages {
        stage('build') {
            steps {
                bat 'python --version'
            }
        }
    }
}