pipeline {
    agent any
    environment {
    registry = "pelegov/dockercompose"
    registryCredential = "docker_hub_pelegov"
}
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
                    if (checkOs() == 'Windows') {
                        bat 'start /min python3 rest_app.py'
                    } else {
                        sh 'nohup python3 rest_app.py &'
                    }
                }
            }
        }
        stage('run back_end_testing') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python3 backend_testing.py'
                    } else {
                        sh 'python3 backend_testing.py'
                    }
                }
            }
        }
        stage('run clean_environment') {
            steps {
                script {
                    if (checkOs() == 'Windows') {
                        bat 'python3 clean_environment.py'
                    } else {
                        sh 'python3 clean_environment.py'
                    }
                }
            }
        }
        stage('run build_and_push_image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    docker.withRegistry('dockerfile', registryCredential) {
                    dockerImage.push()
                    }
                }
            }
        }
        stage('Prune Docker data') {
            steps {
                sh 'docker system prune -a --volumes -f'
            }
        }
        stage('start container') {
            steps {
                sh 'docker compose up -d --no-color --wait'
                sh 'docker compose ps'
            }
        }
        stage('run tests against the container') {
            steps {
                sh 'curl localhost:5000/param?query=demo | jq'
            }
        }
    }
    post {
        always {
            sh 'docker compose down'
            sh 'docker compose ps'
        }
    }
}
