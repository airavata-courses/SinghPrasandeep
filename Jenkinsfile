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
			sh 'sudo docker stop gateway'
			sh 'sudo docker rm gateway'
		}
		def c = docker.image('singhprasandeep/gateway-dockerized').run('-p 8000:8000 --name gateway')
	}
}
