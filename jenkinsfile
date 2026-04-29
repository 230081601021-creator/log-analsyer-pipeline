pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/YOUR_USERNAME/log-analyzer-pipeline.git'
            }
        }

        stage('Run Log Analyzer') {
            steps {
                sh 'python3 analyzer.py'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.txt', fingerprint: true
            }
        }
    }
}
