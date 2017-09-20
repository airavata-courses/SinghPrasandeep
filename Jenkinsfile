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
			sh 'sudo docker ps -q --filter "name=msn" | grep -q . && sudo docker stop msn && sudo docker rm -fv msn'
		}
		def c = docker.image('singhprasandeep/node-dockerized').run('-p 3000:3000 --name msn')
	}
}
