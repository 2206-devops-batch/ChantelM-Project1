properties([pipelineTriggers([githubPush()])])

pipeline {
    agent any
    
    stages {

        stage('Testing Pushes trigger with github-webhook') {
            steps {
                sh 'printenv'
            }
        }
    }
}