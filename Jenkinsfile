node {
	def app
	stage('Clone repository') {
		checkout scm
	}

	stage('Build image') {
  		sh 'docker stop gateway || true && docker rm gateway || true'
        	app = docker.build("singhprasandeep/gateway-dockerized")
    	}
  	stage('Deploy'){
        	def c = docker.image('singhprasandeep/gateway-dockerized').run('-p 8000:8000 --name gateway')
    	}
	
}
