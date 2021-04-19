# analyze-that-bff

## Install virtualenv
py -m pip install --user virtualenv

## Create virtual environment
py -m venv env

## Activate virtual environment
.\env\scripts\activate.bat

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

alembic revision -m "create_main_tables"

alembic upgrade head