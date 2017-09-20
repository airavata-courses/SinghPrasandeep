node {
	def app
	stage('Clone repository') {
		checkout scm
	}

	stage('Build Image') {
		app = docker.build("singhprasandeep/gateway-dockerized")
	}

	stage('Deploy') {
		steps {
			sh 'sudo docker ps -q --filter "name=gateway" | grep -q . && sudo docker stop gateway && sudo docker rm -fv gateway'
		}
		def c = docker.image('singhprasandeep/gateway-dockerized').run('-p 8000:8000 --name gateway')
	}
}
