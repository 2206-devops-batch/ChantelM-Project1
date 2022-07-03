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
            }
        }
        stage('Cloning for build Docker') {
            when {
                branch 'development'
            }
            agent { label 'linuxbuild' }
            steps {
                echo 'cloning for docker image build'
            }
        }
        stage('Building Docker images') {
            when {
                branch 'development'
            }
            agent { label 'linuxbuild' }
            steps {
                echo 'ansible playbook build and push to docker hub here'
                echo 'if successful, git merge with production for next trigger'
            }
        }

        stage('Deploying Docker') {
            when {
                branch 'production'
            }
            agent { label 'linuxdeploy' }
            steps {
                echo 'pull from docker hub and deploy'
                echo 'merge with master if successful'
            }
        }
    }
}

