FROM python:3.11.2

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

WORKDIR /clothing_store/clothing_store

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /clothing_store

EXPOSE 8000

CMD ["python", "/clothing_store/clothing_store/manage.py", "runserver"]

