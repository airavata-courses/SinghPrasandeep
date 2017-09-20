node {
	def app
	stage('Clone repository') {
		checkout scm
	}

	stage('Build Image') {
		app = docker.build("singhprasandeep/python-dockerized")
	}

	stage('Deploy') {
		steps {
			sh 'sudo docker stop msp'
			sh 'sudo docker rm msp'
		}
		def c = docker.image('singhprasandeep/python-dockerized').run('-p 5000:5000 --name msp')
	}
}
