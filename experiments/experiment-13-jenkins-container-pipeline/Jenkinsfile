pipeline {
    agent { label 'python-docker' }

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        IMAGE_NAME = 'campus-tasks-api'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Install and test') {
            steps {
                dir('experiments/experiment-12-flask-api-kubernetes') {
                    sh 'python -m pip install --disable-pip-version-check -r requirements.txt'
                    sh 'python -m unittest -v'
                }
            }
        }

        stage('Build container') {
            steps {
                sh 'docker build --pull -t ${IMAGE_NAME}:${IMAGE_TAG} experiments/experiment-12-flask-api-kubernetes'
            }
        }

        stage('Publish to GHCR') {
            when { branch 'main' }
            steps {
                withCredentials([usernamePassword(credentialsId: 'ghcr-md-aslam-31', usernameVariable: 'REGISTRY_USER', passwordVariable: 'REGISTRY_TOKEN')]) {
                    sh '''
                        echo "$REGISTRY_TOKEN" | docker login ghcr.io -u "$REGISTRY_USER" --password-stdin
                        docker tag "$IMAGE_NAME:$IMAGE_TAG" "ghcr.io/md-aslam-31/csa1020_software_engineering/$IMAGE_NAME:$IMAGE_TAG"
                        docker push "ghcr.io/md-aslam-31/csa1020_software_engineering/$IMAGE_NAME:$IMAGE_TAG"
                        docker logout ghcr.io
                    '''
                }
            }
        }

        stage('Deployment gate') {
            when { branch 'main' }
            steps {
                echo 'Image publication is the end of this lab pipeline. Add a protected deployment target before enabling cloud rollout.'
            }
        }
    }

    post {
        always {
            sh 'docker image prune -f --filter "label=se-experiment-13" || true'
        }
    }
}
