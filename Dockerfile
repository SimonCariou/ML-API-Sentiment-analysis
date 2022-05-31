FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y

WORKDIR /home/api

COPY ./app/requirements.txt /home/api/requirements.txt

RUN pip3 install -r /home/api/requirements.txt

COPY app/ /home/api/app

EXPOSE 8000

CMD ["uvicorn", "app.main:api", "--port", "8000"]