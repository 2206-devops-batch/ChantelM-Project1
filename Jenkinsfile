pipeline {
    agent {label "linuxmain"}
    stages {
        stage('Test') {
            when {
                branch 'PR-*'
                changeRequest target: 'development'
            }
            agent { label 'linuxtest' }
            steps {
                echo 'run unittests here on intital pr to development'
                sh 'printenv'
            }
        }
        stage('Build') {
            when {
                branch 'development'
            }
            agent { label 'linuxbuild' }
            steps {
                echo 'testing build stage'
                echo 'ansible playbook build and push to docker hub here'
                echo 'if successful, git merge with production for next trigger'
            }
        }

        stage('Deploy') {
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
