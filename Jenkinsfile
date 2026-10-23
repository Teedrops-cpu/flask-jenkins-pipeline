pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements-dev.txt
                '''
            }
        }
        stage('Test') {
            steps {
                sh './venv/bin/pytest -v'
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                    mkdir -p dist
                    tar -czf dist/flask-app.tar.gz app.py requirements.txt
                '''
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }
    }

    post {
        success { echo 'Pipeline succeeded' }
        failure { echo 'Pipeline failed, check the stage logs' }
    }
}
