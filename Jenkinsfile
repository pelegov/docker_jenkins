pipeline {
    agent any
    stages {
        stage('git_connect') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('H/30 * * * *')])])
                }
                git branch: 'main', url: 'https://github.com/pelegov/docker_jenkins.git'
            }
        }
        stage('run rest_api_app') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'start /min python3 rest_app.py'
                    } else {
                        sh 'nohup python3 rest_app.py &'
                    }
                }
            }
        }
    }
    environment {
    registry = "pelegov/dockercompose"
    registryCredential = "docker_hub_pelegov"
    dockerImage = ''
    }
}  
