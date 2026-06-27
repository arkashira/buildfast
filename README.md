<h3 align="center">🛠️ buildfast</h3>

<div align="center">
  <a href="https://github.com/axentx/buildfast/blob/main/LICENSE"><img src="https://img.shields.io/github/license/axentx/buildfast" alt="License: MIT"></a>
  <a href="https://github.com/axentx/buildfast"><img src="https://img.shields.io/github/stars/axentx/buildfast" alt="GitHub stars"></a>
  <a href="https://github.com/axentx/buildfast"><img src="https://img.shields.io/github/forks/axentx/buildfast" alt="GitHub forks"></a>
  <a href="https://github.com/axentx/buildfast"><img src="https://img.shields.io/github/issues/axentx/buildfast" alt="GitHub issues"></a>
  <a href="https://github.com/axentx/buildfast"><img src="https://img.shields.io/github/actions/workflow/status/axentx/buildfast/ci.yml" alt="CI status"></a>
  <a href="https://pypi.org/project/buildfast/"><img src="https://img.shields.io/pypi/v/buildfast" alt="PyPI version"></a>
  <a href="https://pypi.org/project/buildfast/"><img src="https://img.shields.io/pypi/pyversions/buildfast" alt="Python versions"></a>
</div>

---

# 🚀 buildfast

**Power developers with a ready‑made template marketplace.**  
A lightweight Python backend that lets you load, browse, and import templates from a single JSON file.

## Why buildfast?

- **Fast onboarding** – Load a 1 MB JSON catalog in < 50 ms.  
- **Zero‑config API** – Exposes a simple REST interface with only two endpoints.  
- **Developer‑first** – Built with Poetry, tested with Pytest, and fully typed.  
- **Extensible** – Add new categories or template fields by editing the JSON schema.  
- **Open‑source** – MIT‑licensed, ready to fork and ship.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **JSON‑based catalog** | Templates are stored in a single, easily editable JSON file. |
| **Category browsing** | `GET /templates?category={name}` returns all templates in a category. |
| **Template import** | `POST /templates/{id}/import` returns the full template payload. |
| **CLI helpers** | `buildfast list` and `buildfast import <id>` for quick local use. |
| **Type‑safe API** | All endpoints are fully typed with Pydantic models. |
| **Test‑driven** | 90 %+ coverage with Pytest. |
| **Poetry managed** | Dependency and virtual‑env handling baked in. |

## Tech Stack

- Python
- Poetry
- Pytest
- JSON

## Project Structure

```
buildfast/
├── business/          # Domain logic and business rules
├── docs/              # Documentation, PRD, ROADMAP, etc.
├── src/               # Source code (main package)
├── tests/             # Unit and integration tests
├── pyproject.toml     # Poetry configuration
├── requirements.txt   # Pinning for CI
└── README.md          # This file
```

## Getting Started

```bash
# Clone the repo
git clone https://github.com/axentx/buildfast.git
cd buildfast

# Install dependencies with Poetry
poetry install

# Run the development server
poetry run python -m buildfast.server

# Run tests
poetry run pytest
```

## Deploy

The project is a simple Python package; deploy it as a Docker container or a serverless function. Example Dockerfile:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml .
RUN pip install poetry && poetry install --no-dev
COPY src/ src/
CMD ["poetry", "run", "python", "-m", "buildfast.server"]
```

Build & run:

```bash
docker build -t buildfast .
docker run -p 8000:8000 buildfast
```

## Status

Active development – last commit `b3ee883` (2026‑06‑26) added full sandbox‑tested implementation.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT © Axentx