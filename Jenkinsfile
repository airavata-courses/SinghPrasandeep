pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                sh 'sudo docker run -d --hostname rabbitRabbit --name rabRabbit -p 15672:15672 -p 5672:5672 -p 5671:5671 rabbitmq:3-management
'
            }
        }
    }
}
