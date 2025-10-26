# Customer Lapse Prediction — Databricks + GitHub Action

Production-ready template for a Customer Lapse Prediction project using **Databricks**, **MLflow**, **Unity Catalog**, **Databricks Asset Bundles (DAB)**, and **GitHub Actions**.

## Prerequisites
- Databricks workspace (Unity Catalog enabled)
- Service principal or user PAT saved as `DATABRICKS_TOKEN`
- Repo secrets:
  - `DATABRICKS_HOST`
  - `DATABRICKS_TOKEN`
  - `UC_CATALOG` (e.g., `main`)
  - `UC_SCHEMA_DEV` (e.g., `lapse_dev`)
  - `UC_SCHEMA_PROD` (e.g., `lapse_prod`)

## Quick Start
```bash
# local (optional)
pyenv install 3.10 -s && pyenv local 3.10
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pre-commit install
```

- Create repo from this template and set GitHub Actions secrets.
- Open PR → CI lints & tests. Merge to `main` → auto deploys to DEV and runs training.
- To promote to PROD, run the **Deploy PROD** workflow manually.

## Next Steps
1. Replace dummy loader with your Unity Catalog sources.
2. Add a feature pipeline (DLT or notebook) to materialize `customer_lapse_features`.
3. Schedule batch inference writing `customer_lapse_predictions`.
4. (Optional) Add Model Serving endpoint for online scoring.
