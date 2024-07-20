# Demo DevOps Python Application

This repository contains a simple Django application that demonstrates various DevOps practices. The application is deployed on a Kubernetes cluster using Helm and GitHub Actions for CI/CD pipelines.

## Table of Contents
- [Architecture](#architecture)
- [Tools](#Tools)
- [Setup Instructions](#setup-instructions)
- [CI/CD Pipelines](#ci-cd-pipelines)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Contributing](#contributing)
- [License](#license)

## Architecture

The Django API is deployed on a DigitalOcean Kubernetes cluster with the following components:
- **Deployment**: The API is deployed with 2 replicas, managed by a Horizontal Pod Autoscaler (HPA) that can scale up to 3 replicas.
- **Service Account**: A basic service account is used to follow security standards.
- **LoadBalancer**: Exposes the API to the world, accessible via the domain [`api.algova.dev`](https://api.algova.dev). It may take about 1 minute.
- **DNS and SSL**: Managed using Route53 and Let's Encrypt. The domain [`api.algova.dev`](https://api.algova.dev) points to the LoadBalancer with automatic SSL certificate renewal.
- **Static Files**: Served from an S3 bucket with proper ACL configurations.

![Architecture Diagram](https://lucid.app/publicSegments/view/216cc460-6c9f-46c7-bf47-b84b90ca15e5/image.png)

## Tools
The following tools were used to develop this project:
- Django: Python library used to power the backend.
- Helm: Used to manage Kubernetes deployments in an organized and clean manner.
- Kubernetes: Where our API is deployed, providing scalability and security.
- Docker: Our API is containerized for easy deployment in any environment.
- Github Actions: Used to deploy our API and to test our PRs before merging.
- Pylint: Keeps our code following high standards.
- Pytest: Ensures proper testing of our API to avoid downtimes.
- Trivy: Keeps us alert to vulnerabilities in our Docker images.

## Setup Instructions
The project was divided according to the task to be performed:
**In all cases, we must clone the repo**
    ```bash
    git clone https://github.com/Adriana618/devops-deemo.git
    cd devops-deemo
    ```
# Develop:
You must have Minikube, Docker, and Helm installed.
    ```bash
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip docker.io kubectl minikube
    pip3 install -r requirements/dev.txt
    ```
# Test:
You must have Minikube, Docker, and Helm installed.
    ```bash
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip docker.io kubectl minikube
    pip3 install -r requirements/test.txt
    ```
# Deploy:
You must have a Kubernetes cluster with 2 nodes with 1CPU and 2GB of memory at a minimum.

After having the necessary setup for each stage, proceed to fill in the Helm values.yaml file or overwrite the variables at the time of installing the app.
- DJANGO_SECRET_KEY
- DATABASE_NAME='db.sqlite3'
- DJANGO_ALLOWED_HOSTS
- AWS_STORAGE_BUCKET_NAME
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION

2. **Dockerize the Application**:
    - Dockerfile located at <a href="https://github.com/Adriana618/devops-deemo/blob/master/docker-conf/Dockerfile-django-api" target="_blank">docker-conf/Dockerfile-django-api</a>

## CI/CD Pipelines

[CI/CD Diagram](https://lucid.app/publicSegments/view/3f074f38-a519-47aa-adca-604faf1ecc18/image.png)

### Deploy API
This GitHub Action deploys commits merged into the `master` branch to a Kubernetes cluster on DigitalOcean.

See the file <a href="https://github.com/Adriana618/devops-deemo/blob/master/.github/workflows/deploy-api.yml" target="_blank">.github/workflows/deploy-api.yml</a>

### Test PR
This GitHub Action tests pull requests by running static code analysis, code coverage, and vulnerability scans.

See the file <a href="https://github.com/Adriana618/devops-deemo/blob/master/.github/workflows/deploy-pr.yml" target="_blank">.github/workflows/deploy-pr.yml</a>

## Kubernetes Deployment

### Deployment Configuration
See the file <a href="https://github.com/Adriana618/devops-deemo/blob/master/devops-deemo/templates/api/api-deployment.yaml" target="_blank">devops-deemo/templates/api/api-deployment.yaml</a>

### Service Configuration
See the file <a href="https://github.com/Adriana618/devops-deemo/blob/master/devops-deemo/templates/api/api-services.yaml" target="_blank">devops-deemo/templates/api/api-services.yaml</a>

### Secrets
See the files <a href="https://github.com/Adriana618/devops-deemo/blob/master/devops-deemo/templates/api/api-secrets.yaml" target="_blank">devops-deemo/templates/api/api-secrets.yaml</a>

## Contributing

Please follow the <a href="https://github.com/Adriana618/devops-deemo/blob/master/CONTRIBUTING.md" target="_blank">contribution guidelines</a> to propose improvements or report issues.

## License

This project is licensed under the MIT License - see the <a href="https://github.com/Adriana618/devops-deemo/blob/master/LICENSE" target="_blank">LICENSE</a> file for details.