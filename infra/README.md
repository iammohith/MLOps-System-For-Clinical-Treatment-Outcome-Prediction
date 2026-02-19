# 🏗️ Infrastructure & Deployment

<div align="center">

![Docker](https://img.shields.io/badge/Docker-Compose_v2-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![K8s](https://img.shields.io/badge/Kubernetes-Manifests-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Prometheus](https://img.shields.io/badge/Observability-Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)

**Infrastructure as Code (IaC) for Local, Edge, and Production environments.**

[⬅️ Back to Root](../README.md)

</div>

---

## 1. Executive Overview

### Philosophy

The infrastructure is designed to be **platform-agnostic**. Whether running on a developer's laptop or a production Kubernetes cluster, the architecture remains consistent:
*   **Microservices** architecture (Frontend, Backend, Monitoring).
*   **Containerization** for isolation.
*   **Declarative** configuration.

---

## 2. Docker Compose (Local / Edge)

This is the primary method for local development and demonstration.

### Topology

| Service | Container Name | Port | Description |
| :--- | :--- | :--- | :--- |
| `inference-api` | `mlops-inference-api` | `8000` | The core Python prediction engine. |
| `frontend` | `mlops-frontend` | `8080` | Nginx serving the Web UI. |
| `prometheus` | `mlops-prometheus` | `9090` | Time-series metric collector. |
| `grafana` | `mlops-grafana` | `3000` | Visualization dashboards. |

### Network

All services communicate over the internal bridge network `mlops-network`.

### Usage

**Note**: The Compose file is located in `infra/docker/`.

```bash
# Start the stack
docker-compose -f infra/docker/docker-compose.yml up --build -d

# Stop the stack
docker-compose -f infra/docker/docker-compose.yml down
```

### Configuration

*   **Data Persistence**: Prometheus (`prometheus-data`) and Grafana (`grafana-data`) use named volumes.
*   **Grafana Admin**: Password defaults to `changeme` (Set via `GRAFANA_ADMIN_PASSWORD`).
*   **Retention**: Prometheus is configured to retain metrics for **7 days**.

---

## 3. Kubernetes (Production)

Manifests for a standard K8s deployment are provided in `infra/k8s/`.

### Inventory

*   `00-namespace.yaml`: Isolates resources in `mlops-system` namespace.
*   `01-deployment.yaml`: Replicas for Inference and Frontend.
*   `02-service.yaml`: ClusterIP and NodePort definitions.
*   `03-monitoring.yaml`: Prometheus/Grafana deployments.

### Deployment

```bash
kubectl apply -f infra/k8s/
```

### Scaling

The inference service is stateless and can be horizontally scaled:

```bash
kubectl scale deployment inference-api --replicas=3 -n mlops-system
```

---

## 4. Security Context

*   **Non-Root**: All Dockerfiles specify a non-root user (`appuser` id:1000 or `nginx`) to minimize container breakout risks.
*   **Read-Only Filesystem**: (Recommended) Production deployments should mount root as Read-Only.
