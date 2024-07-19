pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building docker..'
            }
        }
        stage('Run') {
            steps {
                echo 'Running Docker and mount Scores.txt(score 1 - 1000)..'
            }
        }
        stage('Test') {
            steps {
                echo 'python -m tests.e2e..'
            }
        }
        stage('Finalize') {
            steps {
                echo 'Terminate container and push to docker hub....'
            }
        }
    }
}