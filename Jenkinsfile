pipeline {
    agent {label "linuxmain"}
    options {
        skipDefaultCheckout()      // Don't checkout automatically
    }
    stages {
        stage('Test') {
            when {
                branch 'PR-*'
                changeRequest target: 'development'
            }
            agent { label 'linuxtest' }
            steps {
                checkout scm
                dir("src/client") {
                    sh 'pip install -r requirements.txt'
                }
                dir("src/client/tests") {
                    sh 'python3 -m pytest test_example.py'
                }
            }
        }
        stage('Build') {
            when {
                branch 'development'
            }
            agent { label 'linuxbuild' }
            steps {
                checkout scm
                dir("src/client/ansi") {
                    sh 'cp /home/ubuntu/ansible.cfg ansible.cfg'
                    sh 'cp /home/ubuntu/inventory inventory'
                    sh 'ls'
                    echo 'ansible playbook build-flask.yml'
                }
                sshagent (credentials: ['chamoo334-jenkins']) {
                    sh 'git push origin production'
                }
                echo 'if successful, git merge with production for next trigger'
            }
        }
        stage('Deploy') {
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
