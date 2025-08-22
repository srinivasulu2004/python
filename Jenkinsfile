pipeline {
    agent any
    environment {
        PRIVATE_IP = "172.31.78.222"
        IMAGE_NAME = "pythonapp"
        APP_PORT = "5000"
    }
 
    stages {
        stage('Clone GitHub Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/srinivasulu2004/python.git'
            }
        }
 
        stage('Build Docker Image') {
            steps {
                sh """
                    docker build -t ${IMAGE_NAME} .
                    docker save ${IMAGE_NAME} | gzip > ${IMAGE_NAME}.tar.gz
                """
            }
        }
 
        stage('Copy Docker Image to Private EC2') {
            steps {
                sh """
                    scp -o StrictHostKeyChecking=no -i ~/.ssh/id_ed25519 ${IMAGE_NAME}.tar.gz ubuntu@${PRIVATE_IP}:/home/ubuntu/
                """
            }
        }
 
        stage('Run Docker Image in Private EC2') {
            steps {
                sh """
                    ssh -o StrictHostKeyChecking=no -i ~/.ssh/id_ed25519 ubuntu@${PRIVATE_IP} '
                        docker load < /home/ubuntu/${IMAGE_NAME}.tar.gz &&
                        docker stop ${IMAGE_NAME} || true &&
                        docker rm ${IMAGE_NAME} || true &&
                        docker run -d --name ${IMAGE_NAME} -p ${APP_PORT}:${APP_PORT} ${IMAGE_NAME}
                    '
                """
            }
        }
    }
}


