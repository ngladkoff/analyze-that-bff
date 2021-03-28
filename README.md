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