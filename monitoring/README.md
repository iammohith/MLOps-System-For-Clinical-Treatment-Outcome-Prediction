# Monitoring & Observability

Live telemetry stack for tracking clinical prediction throughput and quality.

## 📊 Instrumentation

The Inference Service exports metrics in Prometheus format at `/metrics`.

### Key SLIs (Service Level Indicators)

* `api_request_total`: Request rate per endpoint and status.
* `api_request_duration_seconds`: Response latency (p50/p95/p99 histograms).
* `api_prediction_total`: Count of successful outcome inferences.
* `api_prediction_errors_total`: Count of failures (model missing, data skew).

## 🎛️ Dashboards

Import `monitoring/grafana/dashboards/api_dashboard.json` into Grafana to visualize:

1. **System Health**: API availability status.
2. **Model version**: Current active model ID (`model_info`).
3. **Error Rates**: Real-time failure alerts.

## 🏃 Running

```bash
# Part of the Docker Compose stack
docker compose -f infra/docker/docker-compose.yml up prometheus grafana
```

**Access**:

* Prometheus: <http://localhost:9090>
* Grafana: <http://localhost:3000> (`admin` / `mlops2024`)
