pipeline {
    agent any

    stages {

        stage('Check Workspace') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }

                stage('Build Docker Image') {
            steps {
                sh 'docker bilt -t hello-python .'
                sh 'minikube image load hello-python'
            }
        }



        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml --validate=false'
                sh 'kubectl apply -f service.yml --validate=false'
                sh 'kubectl rollout restart deployment/hello-python'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'kubectl get deployments'
                sh 'kubectl get pods'
                sh 'kubectl get services'
            }
        }
    }
}
