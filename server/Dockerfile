FROM ubuntu:latest 

RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

WORKDIR /app
COPY . .

ENV APP_HOST "0.0.0.0"
ENV APP_PORT 5000

EXPOSE 5000

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]