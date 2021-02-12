FROM python:3.8
MAINTAINER maddrum
ENV PYTHONUNBUFFERED 1
# add user to config
RUN useradd python_user
RUN apt-get update \
    &&  apt-get upgrade -y \
    #upgrade pip
    && pip install --upgrade pip \
    #install gunicorn
    && pip install gunicorn \
    #install mysql client
    && apt-get install python3-dev build-essential -y \
    #make dir
    && mkdir /usr/extreme_task
# copy requirements and install requirements
WORKDIR /usr/extreme_task
COPY ./requirements.txt /usr/extreme_task/requrements.txt
RUN pip install -r requrements.txt
# copy files
COPY . /usr/extreme_task/
#add privileges for non root user
RUN chown -R python_user /usr/extreme_task
# run as non root user
USER python_user
# migrate django
RUN python manage.py migrate
