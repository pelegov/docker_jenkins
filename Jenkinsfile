pipeline {
    agent any
    environment {
    registry = "pelegov/dockercompose"
    registryCredential = "docker_hub_pelegov"
    dockerImage = ''
    }
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
                        sh 'nohup python3 rest_app.py &'
                    }
                }
            }
        stage('run back_end_testing') {
            steps {
                script {
                        sh 'nohup python3 backend_testing.py &'
                    }
                }
            }
        stage('run clean_environment') {
            steps {
                script {
                        sh 'python3 clean_environment.py'
                    }
                }
            }
        stage('run build_and_push_image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    docker.withRegistry('', registryCredential) {
                    dockerImage.push()
                    }
                }
            }   
        }
        stage('start container') {
            steps {
                script {
                    sh 'docker compose up -d --build'
                    sh 'docker compose ps'
                }    
            }
        }
        stage('test container') {
            steps {
                script {
                    sh 'python3 docker_test.py'
                }
            }
        }
    }
    post {
        always {
            sh 'docker compose down'
            sh 'docker ps'
        }
    }
}
