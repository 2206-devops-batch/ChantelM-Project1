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
                    echo 'ansible playbook build-flask.yml'
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
                echo 'ansible playbook ansi/deploy-flask.yml'
                echo 'merge with master if successful'
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
