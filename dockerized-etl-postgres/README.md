
# dockerized-etl-postgres

**Purpose:** Demonstrates a Dockerized ETL pipeline that ingests sample cohort CSV, performs cleaning/transforms and loads data into PostgreSQL. Useful to showcase Data Curation, ETL, Docker and PostgreSQL skills for clinical research roles.

**Quickstart**
1. Clone the repo.
2. `docker-compose up --build`
3. `docker-compose exec etl python etl/main.py` to run the ETL.
4. Open `notebooks/analysis.ipynb` (Jupyter) to explore loaded data.

**What this shows:** reproducible ETL, Docker, PostgreSQL, simple QA, tests, and CI workflow example.
