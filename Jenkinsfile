pipeline {
    agent any
    stages {
        stage('git_connect') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git branch: 'main', url: 'https://github.com/pelegov/docker_jenkins.git'
            }
        }
        stage('run rest_api_app') {
            steps {
                script {
                        sh 'nohup python3 rest_app.py &'
                    }
                }
            }
        }
    } 
