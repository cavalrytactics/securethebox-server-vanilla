FROM python:3.7-buster

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

# Install Python Requirements
RUN apt-get update -y && apt-get upgrade -y

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

# Start securethebox-server service deployed to Google Cloud Run
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 main:app