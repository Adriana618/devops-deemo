# Demo DevOps Python Application

Este repositorio contiene una simple aplicación Django que demuestra varias prácticas de DevOps. La aplicación se despliega en un clúster de Kubernetes utilizando Helm y GitHub Actions para los pipelines de CI/CD.

## Table of Contents
- [Arquitectura](#arquitectura)
- [Instrucciones de Configuración](#instrucciones-de-configuración)
- [Pipelines de CI/CD](#pipelines-de-ci-cd)
- [Despliegue en Kubernetes](#despliegue-en-kubernetes)
- [Infraestructura como Código](#infraestructura-como-código)
- [Monitoreo y Logging](#monitoreo-y-logging)
- [Contribuyendo](#contribuyendo)
- [Licencia](#licencia)

## Arquitectura

La API de Django se despliega en un clúster de Kubernetes con los siguientes componentes:
- **Deployment**: La API se despliega con 2 réplicas, gestionadas por un Horizontal Pod Autoscaler (HPA) que puede escalar hasta 3 réplicas.
- **Service Account**: Se utiliza una cuenta de servicio básica para seguir los estándares de seguridad.
- **LoadBalancer**: Expone la API al mundo, accesible a través del dominio `https://api.algova.dev`.
- **DNS y SSL**: Gestionados utilizando Route53 y Let's Encrypt. El dominio `api.algova.dev` apunta al LoadBalancer con renovación automática de certificados SSL.
- **Archivos Estáticos**: Servidos desde un bucket de S3 con configuraciones ACL adecuadas.

![Diagrama de Arquitectura](path/to/architecture-diagram.png)

## Instrucciones de Configuración

1. **Clonar el Repositorio**:
    ```bash
    git clone https://github.com/Adriana618/devops-deemo.git
    cd devops-deemo
    ```

2. **Instalar Dependencias**:
    ```bash
    sudo apt-get update
    sudo apt-get install -y python3 python3-pip docker.io kubectl minikube
    pip3 install -r requirements.txt
    ```

3. **Dockerizar la Aplicación**:
    - Dockerfile ubicado en [`docker-conf/Dockerfile-django-api`](https://github.com/Adriana618/devops-deemo/blob/master/docker-conf/Dockerfile-django-api){:target="_blank"}

## Pipelines de CI/CD

### Deploy API
Este GitHub Action despliega los commits mergeados en la rama `master` a un clúster de Kubernetes en DigitalOcean.

Ver el archivo [`.github/workflows/deploy.yml`](https://github.com/Adriana618/devops-deemo/blob/master/.github/workflows/deploy.yml){:target="_blank"}

### Test PR
Este GitHub Action prueba las pull requests ejecutando análisis de código estático, cobertura de código y análisis de vulnerabilidades.

Ver el archivo [`.github/workflows/test-pr.yml`](https://github.com/Adriana618/devops-deemo/blob/master/.github/workflows/test-pr.yml){:target="_blank"}

## Despliegue en Kubernetes

### Configuración del Deployment
Ver el archivo [`k8s/deployment.yaml`](https://github.com/Adriana618/devops-deemo/blob/master/k8s/deployment.yaml){:target="_blank"}

### Configuración del Service
Ver el archivo [`k8s/service.yaml`](https://github.com/Adriana618/devops-deemo/blob/master/k8s/service.yaml){:target="_blank"}

### ConfigMap y Secrets
Ver los archivos [`k8s/configmap.yaml`](https://github.com/Adriana618/devops-deemo/blob/master/k8s/configmap.yaml){:target="_blank") y [`k8s/secret.yaml`](https://github.com/Adriana618/devops-deemo/blob/master/k8s/secret.yaml){:target="_blank"}

### Configuración de Ingress
Ver el archivo [`k8s/ingress.yaml`](https://github.com/Adriana618/devops-deemo/blob/master/k8s/ingress.yaml){:target="_blank"}

## Infraestructura como Código

Usando Terraform, la infraestructura se provisiona en AWS:

Ver el archivo [`terraform/main.tf`](https://github.com/Adriana618/devops-deemo/blob/master/terraform/main.tf){:target="_blank"}

## Monitoreo y Logging

La aplicación se monitorea usando Prometheus y Grafana, con logs centralizados en el stack ELK.

## Contribuyendo

Por favor, sigue las [directrices de contribución](CONTRIBUTING.md) para proponer mejoras o reportar problemas.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](https://github.com/Adriana618/devops-deemo/blob/master/LICENSE){:target="_blank"} para más detalles.