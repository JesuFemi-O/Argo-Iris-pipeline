FROM python:3.9

COPY ./requirements.txt app/requirements.txt

# instead of mounting volumes, create these folders in your base image
# that way I don't have to always dump everything in /tmp folder
# or I can create within temp without doing anything.
# in this example I used /tmp for everything
# i can also decide to do tmp/data/*.csv next time I guess..
# RUN mkdir /data

# RUN mkdir /metrics

# RUN mkdir /models

WORKDIR /app

RUN pip install -r requirements.txt