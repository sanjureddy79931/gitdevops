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
                sh 'docker build --no-cache -t hello-python .'
                sh 'minikube image load hello-python'
            }
        }



        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl delete job hello-python --ignore-not-found=true'
                sh 'kubectl delete pod -l job-name=hello-python --ignore-not-found=true'
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
                sh 'kubectl wait --for=condition=complete job/hello-python --timeout=60s'
                sh 'kubectl logs -l job-name=hello-python'
            }
        }
    }
}
