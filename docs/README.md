# 📚 Documentation Hub

<div align="center">

![Documentation](https://img.shields.io/badge/Docs-Diátaxis-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Up_to_Date-green?style=for-the-badge)

**Central index for the MLOps System documentation.**

[⬅️ Back to Root](../README.md)

</div>

---

## 🧭 Navigation

| Component | Link | Description |
| :--- | :--- | :--- |
| **Data** | [README](../data/README.md) | Schema definitions, DVC tracking, and constraints. |
| **Pipelines** | [README](../pipelines/README.md) | The DAG (Ingest → Validate → Train → Evaluate). |
| **Training** | [README](../training/README.md) | Random Forest algorithm, hyperparameters, and logic. |
| **Models** | [README](../models/README.md) | Artifact versioning (`.joblib`) and serialization. |
| **Metrics** | [README](../metrics/README.md) | Performance reports (`scores.json`) and KPI definitions. |
| **Inference** | [README](../inference/README.md) | FastAPI service, endpoints, and schemas. |
| **Frontend** | [README](../frontend/README.md) | Web UI logic, DOM manipulation, and Nginx setup. |
| **Infrastructure** | [README](../infra/README.md) | Docker, Kubernetes manifests, and network topology. |
| **Monitoring** | [README](../monitoring/README.md) | Prometheus & Grafana stack configuration. |
| **Validation** | [README](../validation/README.md) | CI/CD gates and release checklists. |

---

## 📘 Documentation Standards

We follow the **Diátaxis Framework** for documentation structure:

1.  **Tutorials**: Step-by-step lessons (See `Root README > Installation`).
2.  **How-to Guides**: Problem-oriented steps (See `Usage Guide` in component READMEs).
3.  **Reference**: Technical descriptions (See `Configuration Tables`).
4.  **Explanation**: Understanding-oriented (See `System Context` diagrams).

### Tooling

*   **Mermaid.js**: For diagrams (Flowcharts, Sequence diagrams, ERDs).
*   **Markdown**: Standard GitHub Flavored Markdown (GFM).
*   **Shields.io**: For dynamic status badges.

---

## 🆕 Quick Start for Developers

If you are new to the codebase, we recommend reading in this order:

1.  **Root README**: High-level context.
2.  **Inference README**: Understanding the product interface.
3.  **Pipelines README**: Understanding how the model is built.
4.  **Infra README**: Understanding how it is deployed.

---

## 🤝 Contributing to Docs

*   Keep diagrams up to date with code changes.
*   Verify links before merging.
*   Use specific file paths (e.g., `infra/docker/Dockerfile.inference`) instead of vague references.
