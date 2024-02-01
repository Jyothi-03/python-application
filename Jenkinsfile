pipeline{
    agent any
    stages{
        stage('Version'){
            steps{
                sh 'python3 --version'
            }
        }
        stage('main'){
            steps{
                sh 'python3 main.py'
            }
        }
    }
}
