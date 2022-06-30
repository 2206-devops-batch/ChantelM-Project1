pipeline {
    agent any
    
    stages {
        // https://www.jenkins.io/doc/book/pipeline/syntax/#steps TODO: add steps for pull request trigger
        stage('Testing PR and Aprroved') {
            steps {
                echo '${ghprbCommentBody}'
            }
    }
}