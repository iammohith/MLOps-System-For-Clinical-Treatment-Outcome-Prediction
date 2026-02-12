# Web Frontend

A modern, glassmorphic UI for interacting with clinical predictions.

## ✨ Features

* **Zero Placeholders**: Dropdowns for Condition, Drug, and Side Effects are populated dynamically via the API's `/dropdown-values` endpoint (synchronized with `params.yaml`).
* **Visual Feedback**: Result score (0–10) is rendered on an animated SVG circle gauge.
* **Production Honest**: Prominently displays the clinical disclaimer to ensure safe usage context.

## 🏃 Serving

```bash
# Option A: Python static server (Fast)
cd frontend && python -m http.server 8080

# Option B: Dockerize
docker build -t mlops-frontend -f infra/docker/Dockerfile.frontend .
docker run -p 8080:80 mlops-frontend
```

**Access**: <http://localhost:8080>
