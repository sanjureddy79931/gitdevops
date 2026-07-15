pipeline{
    agent any
    
    stages{
        stage("Check Workspace"){
            steps{
                sh'pwd'
                sh'ls -a'
            }
        }
        stage("Build"){
            steps{
                sh'docker build -t hello-python .'
            }
        }
        stage("Run"){
            steps{
                sh'docker run hello-python'
            }
        }
    }
}
