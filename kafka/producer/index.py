import os
from flask import Flask
import threading, logging, time
import sys

from kafka import  KafkaProducer

ip=sys.argv[1]

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
application = Flask(__name__)

@application.route("/")
def hello():
    
    producer = KafkaProducer(bootstrap_servers=ip)
    producer.send('test', b"producer message-hello")
    time.sleep(10)
  

    return "Message sent"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8080)
