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
			sh 'sudo docker ps -q --filter "name=msp" | grep -q . && sudo docker stop msp && sudo docker rm -fv msp'
		}
		def c = docker.image('singhprasandeep/python-dockerized').run('-p 5000:5000 --name msp')
	}
}
