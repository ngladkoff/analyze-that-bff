# analyze-that-bff

## Install virtualenv
<code>

py -m pip install --user virtualenv (win)
python3.9 -m pip install --user virtualenv (wsl)

</code>

## Create virtual environment
<code>

py -m venv venv (win)
python3.9 -m venv venv (wsl)

</code>

## Activate virtual environment
<code>

.\venv\scripts\activate (win)
source ./venv/bin/activate (wsl)

</code>

## Install requirements
<code>

pip install -r requirements.txt

</code>

## Run BFF debug
<code>

uvicorn main:app --reload

</code>

## Docker build image
<code>

docker build -t ngladkoff/analyze-that-bff .

</code>

## Docker run
<code>

docker run -it -p 8000:80 --rm --name analyze-bff ngladkoff/analyze-that-bff

</code>

# DATABASE MIGRATIONS

<code>

docker ps

copiar container_id

docker exec -it 15f32cd4335c bash

</code>

### Solo la primera vez o para una migracion
<code>

alembic revision -m "create_main_tables"

</code>

### Siempre para actualizar la base
<code>

alembic upgrade head

</code>

### Para hacer un downgrade
<code>

alembic downgrade base

</code>


## Conectar con la base de datos
<code>

docker-compose exec analyze_db psql -h localhost -U analyze_db_user --dbname=analyze

</code>

- \l -> lista all databases
- \d+ -> list all tables in the current database
- \c postgres -> connect to the postgres database
- \d cleanings -> describe the cleanings table and the associated columns

<code>

SELECT ... ; -> se ejecuta directo

</code>


# Ejecutar tests integración
<code>

docker ps

docker exec -it [CONTAINER_ID] bash

python -m pytest -v

</code>

