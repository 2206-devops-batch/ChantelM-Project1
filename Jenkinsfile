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
                echo 'testing all through ssh with username'
                // sh """
                //     git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'
                //     git fetch --all
                //     git switch production
                //     git pull --rebase origin development
                //     git push
                //     git push --set-upstream origin production
                // """
                sshagent(credentials : ['59cf2e5d-df64-4dd8-8556-f16441112899']) {
                    sh "git config remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'"
                    sh 'git fetch --all'
                    sh "git remote set-url origin https://${gh_user}:${gh_pass}@github.com/2206-devops-batch/ChantelM-Project1.git"
                    sh 'git checkout production'
                    sh 'git merge development'
                    sh 'git push origin production'
                }
                // dir("src/client/ansi") {
                //     sh 'cp /home/ubuntu/ansible.cfg ansible.cfg'
                //     sh 'cp /home/ubuntu/inventory inventory'
                //     sh 'ls'
                //     echo 'ansible playbook build-flask.yml'
                // }
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
