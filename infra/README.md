# Infrastructure

Docker and Kubernetes configuration for the MLOps system.

## Docker

```bash
# Build and run all services
cd infra/docker
docker compose up --build

# Individual services
docker compose up inference-api
docker compose up frontend
docker compose up prometheus
docker compose up grafana
```

### Services & Ports

| Service | Port | Image |
|---------|------|-------|
| Inference API | 8000 | mlops-inference-api |
| Frontend | 8080 | mlops-frontend |
| Prometheus | 9090 | prom/prometheus:v2.49.1 |
| Grafana | 3000 | grafana/grafana:10.3.1 |

## Kubernetes

```bash
# Apply all manifests
kubectl apply -f infra/k8s/

# Dry-run validation
kubectl apply --dry-run=client -f infra/k8s/

# Check status
kubectl get all -n mlops
```

### NodePort Mapping

| Service | NodePort |
|---------|----------|
| Inference API | 30800 |
| Frontend | 30880 |
| Prometheus | 30909 |
| Grafana | 30300 |
