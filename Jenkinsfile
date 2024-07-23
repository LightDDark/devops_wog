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
                sh 'python -m venv .venv'
                sh '. .venv/bin/activate'
                sh 'pip install selenium'
                sh 'python ./tests/e2e.py'
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
            sh 'docker stop $(docker ps -q)'
            sh 'docker rm $(docker ps -a -q)'
        }
    }
}