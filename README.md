# mlops
MLOps GitHub Repository: A centralized hub for implementing Machine Learning Operations (MLOps) practices, including CI/CD pipelines, model versioning, monitoring, and deployment automation.  Purpose: Streamline the end-to-end machine learning lifecycle, ensuring scalable, reproducible, and efficient model development, deployment and monitoring

Initialized repo using 
* pip install poetry black pre-commit
* poetry init/update if needed
* touch .pre-commit-config.yaml
    add following content inside
  """
  repos:
  - repo: https://github.com/psf/black
    rev: 23.12.1  # Check Black's latest version and update if needed
    hooks:
      - id: black
   """
* run "pre-commit install" to activate black as pre-commit
* test pre commit with black using
  """
  git add .
  git commit -m "Test pre-commit with Black"
  """
