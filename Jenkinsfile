pipeline {
environment {
registry = "my-user/my-repo"
registryCredential = 'docker_hub'
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