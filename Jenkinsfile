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
        always {
            sh 'docker stop $(docker ps -aq)'
            sh 'docker rm $(docker ps -aq)'
            sh 'docker rmi -f oryehezkel/wog'
        }
    }
}