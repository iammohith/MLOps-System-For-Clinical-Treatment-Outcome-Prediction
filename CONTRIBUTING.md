# Contributing to Clinical Treatment Outcome Prediction

Thank you for your interest in contributing to this MLOps project! We welcome contributions from engineers, data scientists, and medical professionals.

## 🤝 How to Contribute

### 1. Reporting Bugs

- **Search existing issues** to avoid duplicates.
- **Open a new issue** describing the bug, including:
  - Steps to reproduce
  - Expected vs. actual behavior
  - Screenshots or logs (redact any sensitive info)

### 2. Suggesting Enhancements

- Open a **Feature Request** issue.
- Describe the medical or technical value of the enhancement.
- Provide examples or mockups if applicable.

### 3. Submitting Code Changes

1. **Fork** the repository.
2. Create a new branch: `git checkout -b feature/MyFeature`
3. Make your changes.
4. **Validate locally**:

    ```bash
    make validate
    ```

    *Ensure all checks pass before pushing.*
5. Commit your changes: `git commit -m "feat: Add new clinical parameter validation"`
6. Push to your fork and submit a **Pull Request**.

## 🛠️ Development Guidelines

### Coding Standards

- **Python**: Follow PEP 8. Type hints are mandatory.
- **JavaScript**: Use modern ES6+ syntax.
- **Documentation**: Update docstrings and READMEs for any logic changes.

### Zero-Trust Philosophy

By contributing, you agree to uphold the **Zero-Trust** architecture:

- **Never** remove input validation.
- **Never** hardcode secrets or IPs.
- **Always** validate data schemas via `params.yaml`.

## 🧪 Testing

- Add unit tests for new logic in `tests/` (if applicable).
- Run the full validation suite: `python validation/release_check.py`.

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.
