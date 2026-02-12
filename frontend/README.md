# Frontend

Modern web UI for clinical treatment outcome prediction.

## Features

- Premium dark-mode design with glassmorphism effects
- All categorical inputs as dropdowns (populated from CSV values)
- Animated SVG circle gauge for prediction display (0–10 scale)
- Non-clinical disclaimer prominently displayed
- Responsive layout

## Serving

```bash
# Via Docker (recommended)
docker compose -f infra/docker/docker-compose.yml up frontend

# Or use any static file server
cd frontend && python -m http.server 8080
```

Access at: `http://localhost:8080`
