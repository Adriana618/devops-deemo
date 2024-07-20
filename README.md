# Demo DevOps Python Application

This repository contains a simple Django application that demonstrates various DevOps practices. The application is deployed on a Kubernetes cluster using Helm and GitHub Actions for CI/CD pipelines.

## Table of Contents
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
- [CI/CD Pipelines](#ci-cd-pipelines)
- [Kubernetes Deployment](#kubernetes-deployment)
- [Infrastructure as Code](#infrastructure-as-code)
- [Monitoring and Logging](#monitoring-and-logging)
- [Contributing](#contributing)
- [License](#license)

## Architecture

The Django API is deployed on a Kubernetes cluster with the following components:
- **Deployment**: The API is deployed with 2 replicas, managed by a Horizontal Pod Autoscaler (HPA) that can scale up to 3 replicas.
- **Service Account**: A basic service account is used to follow security standards.
- **LoadBalancer**: Exposes the API to the world, accessible via the domain `https://api.algova.dev`.
- **DNS and SSL**: Managed using Route53 and Let's Encrypt. The domain `api.algova.dev` points to the LoadBalancer with automatic SSL certificate renewal.
- **Static Files**: Served from an S3 bucket with proper ACL configurations.

![Architecture Diagram](path/to/architecture-diagram.png)

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Adriana618/devops-deemo.git
    cd devops-deemo
    ```

2. **Install Dependencies**:
    ```bash
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip docker.io kubectl minikube
    pip3 install -r requirements.txt
    ```

3. **Dockerize the Application**:
    - Dockerfile located at <a href="https://github.com/Adriana618/devops-deemo/blob/master/docker-conf/Dockerfile-django-api" target="_blank">docker-conf/Dockerfile-django-api</a>

## CI/CD Pipelines

### Deploy API
This GitHub Action deploys commits merged into the `master` branch to a Kubernetes cluster on DigitalOcean.

See the file <a href="https://github.com/Adriana618/devops-deemo/blob/master/.github/workflows/deploy.yml" target="_blank">.github/workflows/deploy.yml</a>

### Test PR
This GitHub Action tests pull requests by running static code analysis, code coverage, and vulnerability scans.

See the file <a href="https://github.com/Adriana618/devops-deemo/blob/master/.github/workflows/test-pr.yml" target="_blank">.github/workflows/test-pr.yml</a>

## Kubernetes Deployment

### Deployment Configuration
See the file <a href="https://github.com/Adriana618/devops-deemo/blob/master/k8s/deployment.yaml" target="_blank">k8s/deployment.yaml</a>

### Service Configuration
See the file <a href="https://github.com/Adriana618/devops-deemo/blob/master/k8s/service.yaml" target="_blank">k8s/service.yaml</a>

### ConfigMap and Secrets
See the files <a href="https://github.com/Adriana618/devops-deemo/blob/master/k8s/configmap.yaml" target="_blank">k8s/configmap.yaml</a> and <a href="https://github.com/Adriana618/devops-deemo/blob/master/k8s/secret.yaml" target="_blank">k8s/secret.yaml</a>

### Ingress Configuration
See the file <a href="https://github.com/Adriana618/devops-deemo/blob/master/k8s/ingress.yaml" target="_blank">k8s/ingress.yaml</a>

## Infrastructure as Code

Using Terraform, the infrastructure is provisioned on AWS:

See the file <a href="https://github.com/Adriana618/devops-deemo/blob/master/terraform/main.tf" target="_blank">terraform/main.tf</a>

## Monitoring and Logging

The application is monitored using Prometheus and Grafana, with logs centralized in the ELK stack.

## Contributing

Please follow the <a href="https://github.com/Adriana618/devops-deemo/blob/master/CONTRIBUTING.md" target="_blank">contribution guidelines</a> to propose improvements or report issues.

## License

This project is licensed under the MIT License - see the <a href="https://github.com/Adriana618/devops-deemo/blob/master/LICENSE" target="_blank">LICENSE</a> file for details.