pipeline {
    agent { label 'agent' }

    environment {
        IMAGE_NAME = 'srinivasulu2004/repo-1'
        VERSION = "${BUILD_NUMBER}"
    }

    stages {

        stage('Clone Repository') {
            steps {
                echo "Cloning source code..."
    
            }
        }

        stage('Run Tests') {
            steps {
                echo "Running unit tests..."
                sh '''
                echo "No tests found"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                sh '''
                    docker build -t $IMAGE_NAME:$VERSION .
                '''
            }
        }

         stage('Push Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub', url: '']) {
                    sh 'docker push $IMAGE_NAME:$VERSION'
                }
            }
        }

        stage('Deploy (Optional)') {
            steps {
                echo " Deploying container (Example)..."
                sh '''
                    docker run --name container1 -d -p 5000:5000 $IMAGE_NAME:$VERSION
                '''
            }
        }
    }
}
