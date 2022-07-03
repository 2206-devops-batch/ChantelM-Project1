pipeline {
    agent {label "linuxmain"}
    options {
        skipDefaultCheckout()      // Don't checkout automatically
    }
    stages {
        stage('Testing PR') {
            when {
                branch 'PR-*'
                changeRequest target: 'development'
            }
            agent { label 'linuxtest' }
            steps {
                checkout scm
                sh 'cd src/client'
                sh 'ls'
                // sh 'pip install -r requirements.txt'
                // sh 'pytest tests/'
            }
        }
        stage('Clone and Build Docker image') {
            when {
                branch 'development'
            }
            agent { label 'linuxbuild' }
            steps {
                checkout scm
                echo 'ansible playbook ansi/build-flask.yml'
                echo 'if successful, git merge with production for next trigger'
            }
        }
        stage('Deploying Docker') {
            when {
                branch 'production'
            }
            agent { label 'linuxdeploy' }
            steps {
                checkout scm
                echo 'ansible playbook ansi/deploy-flask.yml'
                echo 'merge with master if successful'
            }
        }
    }
}

