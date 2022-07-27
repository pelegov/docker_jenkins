pipeline {
  environment {
  registry = "pelegov/getuser"
  registryCredential = 'docker_hub_pelegov'
  dockerImage = ''
}
  agent any
  stages {
    stage('git_connect') {
        steps {
        script {
             properties([pipelineTriggers([pollSCM('H/30 * * * *')])])
            }
            git branch: 'main', url:'https://github.com/pelegov/docker_jenkins'
        }
    }
    stage('build and push image') {
      steps {
        script {
           dockerImage = docker.build registry + ":$BUILD_NUMBER"
           docker.withRegistry('', registryCredential) {
           dockerImage.push()
        }
      }
    }
    post {
    always {
      sh "docker rmi $registry:$BUILD_NUMBER"
}
}
}
}
}