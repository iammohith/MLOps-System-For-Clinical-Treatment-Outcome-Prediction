# Validation

Repository validation and quality gate checks.

## Usage

```bash
# Full validation
python validation/validate_repo.py

# Skip optional checks
python validation/validate_repo.py --skip-docker --skip-k8s --skip-api
```

## Checks Performed

1. **File existence** — All required files present
2. **YAML syntax** — All YAML files parse correctly
3. **Dockerfile sanity** — FROM and COPY instructions present
4. **Training smoke test** — Full pipeline runs end-to-end
5. **API startup test** — Health, predict, and schema rejection
6. **Docker build** — Docker CLI availability
7. **K8s dry-run** — All manifests pass `kubectl apply --dry-run=client`
