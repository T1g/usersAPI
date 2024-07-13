# Pull the image from Dockerhub
#FROM python:alpine3.19

FROM python:3.10.7

WORKDIR /user_app
# set up python environment variables

#ENV PYTHONDOWNWRITEBYTECODE 1
#ENV PYTHONNUNBUFFER 1
#ENV PYTHONUNBUFFERED=1

COPY . /user_app

# update and  install dependencies
#RUN pip install --upgrade pip
#COPY ./requirements.txt /api/requirements.txt
#RUN pip install -r /api/requirements.txt
RUN pip install -r requirements.txt

# copy project
#COPY . .

# Expose the port server is running on
EXPOSE 8000

CMD ["python","manage.py","runserver"]