FROM python:2
RUN pip install kafka
RUN pip install Flask
RUN pip install gunicorn

ARG ip=10.128.1.245:9092
ENV  ipa=$ip
COPY . /
EXPOSE 8080
CMD python /index.py $ipa
