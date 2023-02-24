FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY src /code/
COPY cnn_model /code/

RUN pip install uvicorn fastapi

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
