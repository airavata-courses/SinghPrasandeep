node {
	def app

	stage('Clone Repository') {
		checkout scm
	}

	stage('Build Image') {
		sh 'docker stop msn || true && docker rm msn || true'
		app = docker.build("singhprasandeep/node-dockerized")
	}
	
	stage('Deploy') {
		def c = docker.image('singhprasandeep/node-dockerized').run('-p 3000:3000 --name msn')
	}
}
