# Monitoring

Prometheus and Grafana configuration for observability.

## Components

| Component | Port | Description |
|-----------|------|-------------|
| Prometheus | 9090 | Metrics collection and storage |
| Grafana | 3000 | Dashboard visualization |

## Prometheus

Scrapes the inference API `/metrics` endpoint every 15 seconds.

### Tracked Metrics

- `api_request_total` — Request count by method/endpoint/status
- `api_prediction_total` — Total predictions served
- `api_prediction_errors_total` — Prediction error count
- `api_request_duration_seconds` — Latency distribution
- `model_info` — Model version metadata

## Grafana

### Dashboard Import

1. Open Grafana at `http://localhost:3000`
2. Login: `admin` / `mlops2024`
3. Add Prometheus data source: `http://prometheus:9090`
4. Import dashboard from `grafana/dashboards/api_dashboard.json`

## Model Monitoring

See `../docs/model_monitoring.md` for conceptual drift detection design.
