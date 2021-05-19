# analyze-that-bff

## Install virtualenv
py -m pip install --user virtualenv

## Create virtual environment
py -m venv venv

## Activate virtual environment
.\venv\scripts\activate.bat

## Install requirements
pip install -r requirements.txt

## Run BFF
uvicorn main:app --reload

## Docker build image
docker build -t ngladkoffglb/analyze-that-bff .

## Docker run
docker run -it -p 5000:80 --rm --name analyze-bff ngladkoffglb/analyze-that-bff

## DATABASE MIGRATIONS
docker ps

copiar container_id

docker exec -it 15f32cd4335c bash

-- solo la primera vez o para una migracion -- alembic revision -m "create_main_tables"

-- siempre para actualizar la base -- alembic upgrade head

-- para hacer un downgrade -- alembic downgrade base

## Conectar con la base de datos
docker-compose exec analyze_db psql -h localhost -U analyze_db_user --dbname=analyze

\l -> lista all databases
\d+ -> list all tables in the current database
\c postgres -> connect to the postgres database
\d cleanings -> describe the cleanings table and the associated columns

SELECT ... ; -> se ejecuta directo

# Ejecutar tests integración
docker ps
docker exec -it [CONTAINER_ID] bash

python -m pytest -v


