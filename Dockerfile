FROM python:latest

WORKDIR app/

COPY requirements.txt .

COPY . .

RUN python -m pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000

