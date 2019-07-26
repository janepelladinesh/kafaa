FROM python:2
RUN pip install kafka
RUN pip install Flask
RUN pip install gunicorn

ARG ip='apache-kafka'
ENV  service=$ip
COPY . /
EXPOSE 8080
CMD python /index.py $service
