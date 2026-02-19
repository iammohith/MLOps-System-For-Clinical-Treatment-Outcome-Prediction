# 📊 Monitoring & Observability

<div align="center">

![Prometheus](https://img.shields.io/badge/Metrics-Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Visuals-Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)

**Glass-box monitoring for Model Health and System Performance.**

[⬅️ Back to Root](../README.md)

> [!TIP]
> **For Managers & Auditors**: These dashboards are available at `http://localhost:3000` when running the main system via Docker.

</div>

---

## 1. Stack Overview

We use the standard cloud-native monitoring stack:

*   **Prometheus**: Scrapes metrics from `inference-api:8000/metrics` every **15 seconds**.
*   **Grafana**: Visualizes these metrics in a pre-configured dashboard.

---

## 2. Access

| Service | URL | Credentials |
| :--- | :--- | :--- |
| **Grafana** | `http://localhost:3000` | User: `admin` / Pass: `changeme` |
| **Prometheus** | `http://localhost:9090` | None (Internal access only recommended) |

---

## 3. Configuration

### Prometheus (`monitoring/prometheus.yml`)

*   **Scrape Interval**: 15s (Global default).
*   **Data Retention**: 7 Days (Configured in `docker-compose.yml`).
*   **Targets**: `['inference-api:8000']`.

### Grafana Provisioning

Grafana is completely **stateless** and **auto-provisioned** via code:
1.  **Datasource**: `monitoring/grafana/provisioning/datasources/datasources.yml` automatically connects to Prometheus.
2.  **Dashboards**: `monitoring/grafana/provisioning/dashboards/` loads JSON definitions from disk.

---

## 4. Dashboards

The **Clinical Prediction API Dashboard** provides the following panels:

![Grafana Dashboard](../Grafana%20Dashboard.png)

### System Health
*   **API Health Status**: UP/DOWN indicator.
*   **Model Version**: Displays the active SHA-256 model hash.

### Performance
*   **Request Latency**: P50, P95, and P99 histograms to track user experience.
*   **Request Rate**: Throughput (Requests Per Second) broken down by endpoint.
*   **Error Rate**: Percentage of 5xx/4xx responses.

### Business Metrics
*   **Total Predictions**: Count of clinical inferences served.
*   **Prediction Distribution**: (Future) Histogram of predicted scores to detect drift.

---

## 5. Troubleshooting "No Data"

If your dashboard shows "No Data":

1.  **Check Liveness**: Ensure `inference-api` is running (`docker ps`).
2.  **Check Scrape Status**: Go to `http://localhost:9090/targets` and verify the API target is **UP**.
3.  **Generate Load**: The dashboard requires traffic. Run a few predictions via the Web UI to generate data points.
