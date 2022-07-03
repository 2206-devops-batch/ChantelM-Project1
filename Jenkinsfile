pipeline {
    agent {label "linuxmain"}
    stages {
        stage('Cloning PR') {
            when {
                branch 'PR-*'
                changeRequest target: 'development'
            }
            agent { label 'linuxtest' }
            steps {
                dir("/src/client") {
                    sh "pwd"
                }
                echo 'cloning the pull request for testing'
                sh 'printenv'
            }
        }
        stage('Testing PR') {
            when {
                branch 'PR-*'
                changeRequest target: 'development'
            }
            agent { label 'linuxtest' }
            steps {
                dir("/src/client") {
                    sh "pwd"
                }
                echo 'pull request can now be tests'
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
