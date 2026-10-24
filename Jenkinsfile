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
                sh './venv/bin/pytest -v --junitxml=test-results.xml'
            }
        }
        stage('Deploy') {
            steps {
                withCredentials([string(credentialsId: 'app-api-key', variable: 'APP_API_KEY')]) {
                    sh '''
                        echo "Deploying with key: $APP_API_KEY"
                        mkdir -p dist
                        tar -czf dist/flask-app.tar.gz app.py requirements.txt
                    '''
                }
                archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'test-results.xml'
        }
        success { echo 'Pipeline succeeded' }
        failure { echo 'Pipeline failed, check the stage logs' }
    }
}
