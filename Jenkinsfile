pipeline {
    agent any
    
    triggers {
      pullRequestReview(reviewStates: ['pending', 'approved'])
    }

    stages {
        stage('Clone') {
            steps {
                sh 'printenv'
                if (env.CHANGE_ID){
                    echo 'pull request'
                    echo '${GITHUB_REVIEW_STATE}'
                }   
            }
        }
    }
}
