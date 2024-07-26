pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }
        stage('Run') {
            steps {
                sh 'docker compose up -d'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install selenium'
                sh '.venv/bin/python ./tests/e2e.py http://localhost:8777'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker compose down'
                sh 'docker push oryehezkel/wog'
            }
        }
    }
    post {
        failure {
            sh 'docker stop $(docker ps -aq) || true'
            sh 'docker rm $(docker ps -aq) || true'
        }
        cleanup {
            sh 'docker compose down || true'
            sh 'docker rmi -f oryehezkel/wog || true'
            sh 'docker system prune -af || true'
        }
    }
}
