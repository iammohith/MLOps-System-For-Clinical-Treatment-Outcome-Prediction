# Infrastructure (Containerization & Orchestration)

Standardized manifests for local development and edge deployment. All artifacts here are verified via dry-runs in the `make validate` protocol.

## 🐳 Docker (Local Development)

Located in `docker/`, we use a segmented Compose architecture.

### Quick Commands

```bash
# Full stack build & launch
docker compose -f infra/docker/docker-compose.yml up --build

# Individual layer launch
docker compose -f infra/docker/docker-compose.yml up inference-api
```

## ☸️ Kubernetes (Local Deployment)

Located in `k8s/`, designed for use with `kind` or `minikube`.

### Verification Logic

We prioritize dry-run validation to ensure manifest integrity without requiring a live node.

```bash
kubectl apply --dry-run=client -f infra/k8s/
```

### Component Roles

* **namespace.yaml**: Isolates the system in the `mlops` namespace.
* **inference-deployment.yaml**: Scales the FastAPI pod.
* **prometheus-configmap.yaml**: Authoritative scraping config.

## ⚠️ Known Networking Limitations

In Docker Compose, the API service name is `inference-api`. If you are running components outside of the Docker network (e.g., bare-metal API), you MUST update `monitoring/prometheus.yml` to target `localhost:8000`.
