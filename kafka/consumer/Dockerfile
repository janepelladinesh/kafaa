# Install  python to run the python script
FROM python:2

#install kafka ,flask ,gunicorn  libraries of python

RUN  pip install kafka && pip install Flask && pip install gunicorn
ARG service_name='apache-kafka'

# set the env virable ,which will be given while creating the application

ENV  service=$service_name
COPY . /
EXPOSE 8080

#run the python script

CMD python /index.py $service
