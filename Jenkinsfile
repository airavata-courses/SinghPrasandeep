node {
	def app

	stage('Clone Repository') {
		checkout scm
	}

	stage('Build Image') {
		app = docker.build("singhprasandeep/node-dockerized")
	}
	
	stage('Deploy') {
		steps {
			sh 'sudo docker stop msn'
			sh 'sudo docker rm msn'
		}
		def c = docker.image('singhprasandeep/node-dockerized').run('-p 3000:3000 --name msn')
	}
}
