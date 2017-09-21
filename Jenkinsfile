node {
	def app
	stage('Clone repository') {
		checkout scm
	}

	stage('Build Image') {
		sh 'docker stop msp || true && docker rm msp || true'
		app = docker.build("singhprasandeep/python-dockerized")
	}

	stage('Deploy') {
		def c = docker.image('singhprasandeep/python-dockerized').run('-p 5000:5000 --name msp')
	}
}
