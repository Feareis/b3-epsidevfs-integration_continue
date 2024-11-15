pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone the GitHub repository
                git 'https://github.com/Feareis/b3-epsidevfs-integration_continue.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Builds the Docker image with the specified name and version
                    docker.build('currency_converter:1.0')
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests using the created Docker image
                    docker.image('currency_converter:1.0').inside {
                        sh 'pytest'
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Runs the container in the background
                    docker.run('-d -p 5000:5000 currency_converter:1.0')
                }
            }
        }
    }
}
