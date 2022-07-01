properties([pipelineTriggers([githubPull()])])

pipeline {
    agent any
    
    stages {

        stage('Testing PR and Aprroved GitHub') {
            steps {
                sh 'printenv'
            }
        }
    }
}