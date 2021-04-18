FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .