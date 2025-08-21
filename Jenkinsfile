pipeline {
  // IMPORTANT: The label here must match your agent's label in Jenkins
  agent { label 'docker-agent' }

  environment {
    IMAGE = "password_generator:${env.BUILD_NUMBER}"
    CONTAINER_NAME = "password_generator"
    PORT = "5000"
  }

  stages {
    stage('Checkout') {
      steps {
        // Pulls the same branch Jenkins is building from your GitHub repo
        checkout scm
      }
    }

    stage('Build image') {
      steps {
        // Builds Docker image from your repo's Dockerfile
        sh "docker build -t ${IMAGE} ."
      }
    }

    stage('Stop old container') {
      steps {
        // Stops & removes any previous container (ignore error if not present)
        sh "docker rm -f ${CONTAINER_NAME} || true"
      }
    }

    stage('Run container') {
      steps {
        // Starts your Flask app at http://localhost:5000
        sh "docker run -d -p ${PORT}:${PORT} --name ${CONTAINER_NAME} ${IMAGE}"
      }
    }
  }

  post {
    success {
      echo "Deployed ${IMAGE} -> http://localhost:${PORT}"
    }
    failure {
      echo "Pipeline failed"
    }
  }
}
