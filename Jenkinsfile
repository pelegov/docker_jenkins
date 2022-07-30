pipeline {
  environment {
  registry = "pelegov/getuser"
  registrycredential = 'docker_hub_pelegov'
  dockerimage = ''
}
  agent any
  stages {
    stage('git_connect') {
        steps {
        script {
             properties([pipelinetriggers([pollscm('h/30 * * * *')])])
            }
            git branch: 'main', url:'https://github.com/pelegov/docker_jenkins'
        }
    }
    stage('build and push image') {
      steps {
        script {
           echo "test"
           dockerimage = docker.build registry + ":$build_number"
           docker.withregistry('', registrycredential) {
           dockerimage.push()
        }
      }
    }
    }
    post {
    always {
      echo $dockerimage
      sh "docker rmi $registry:$build_number"
}
}
}
}
