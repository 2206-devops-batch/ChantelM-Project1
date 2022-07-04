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
                
                dir("ansi") {                
                    sh 'cp /home/ubuntu/env.py /home/ubuntu/workspace/p1-multi_development/src/client/utils/env.py'
                    sh 'cp /home/ubuntu/ansible.cfg ansible.cfg'
                    sh 'cp /home/ubuntu/inventory inventory'
                    sh 'cp /home/ubuntu/vault.yml vault.yml'
                    sh '/home/ubuntu/.local/bin/ansible-playbook -i inventory build-flask.yml --vault-password-file  /home/ubuntu/vpass.txt'
                    sh 'rm ansible.cfg inventory'
                }
                
                sshagent(credentials : ['59cf2e5d-df64-4dd8-8556-f16441112899']) {
                    sh "git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'"
                    sh 'git fetch --all'
                    sh "git remote set-url origin https://${gh_user}:${gh_pass}@github.com/2206-devops-batch/ChantelM-Project1.git"
                    sh 'git checkout production'
                    sh 'git merge development'
                    sh 'git push origin production --force'
                }
            }
        }
        stage('Deploy') {
            when {
                branch 'production'
            }
            agent { label 'linuxdeploy' }
            steps {
                checkout scm

                dir("ansi") {
                    sh 'cp /home/ubuntu/ansible.cfg ansible.cfg'
                    sh 'cp /home/ubuntu/inventory inventory'
                    sh 'cp /home/ubuntu/vault.yml vault.yml'
                    sh 'cp /home/ubuntu/p1.pem p1.pem'
                    sh 'chmod 400 p1.pem'
                    sh '/home/ubuntu/.local/bin/ansible-playbook -i inventory deploy-flask.yml --vault-password-file  /home/ubuntu/vpass.txt'
                    sh 'rm ansible.cfg inventory'
                    sh 'sudo rm p1.pem'
                }

                sshagent(credentials : ['59cf2e5d-df64-4dd8-8556-f16441112899']) {
                    sh "git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'"
                    sh 'git fetch --all'
                    sh "git remote set-url origin https://${gh_user}:${gh_pass}@github.com/2206-devops-batch/ChantelM-Project1.git"
                    sh 'git checkout master'
                    sh 'git merge production'
                    sh 'git push origin master --force'
                }
            }
        }
    }
}
