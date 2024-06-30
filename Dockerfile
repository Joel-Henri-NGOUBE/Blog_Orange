FROM python:latest

WORKDIR app/

COPY requirements.txt .

COPY . .

RUN python -m pip install -r requirements.txt

CMD ["gunicorn", "multilang_site.wsgi", "0.0.0.0:8000"]

EXPOSE 8000

