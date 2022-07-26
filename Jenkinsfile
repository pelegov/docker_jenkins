pipeline {
  environment {
  registry = "https://github.com/pelegov/docker_jenkins"
  registryCredential = 'docker_hub_pelegov'
  dockerImage = ''
}
  agent any
  stages {
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