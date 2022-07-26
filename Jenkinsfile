pipeline {
  environment {
  registry = "pelegov/docker_jenkins"
  registryCredential = 'docker_hub_pelegov'
  dockerImage = ''
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
      bat "docker rmi $registry:$BUILD_NUMBER"
}}}}