import os
from flask import Flask
import sys
from kafka import KafkaConsumer

ip=sys.argv[1]

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
application = Flask(__name__)

@application.route("/")
def hello():
    consumer = KafkaConsumer(bootstrap_servers=ip,
                             auto_offset_reset='earliest',
                             consumer_timeout_ms=1000)
    consumer.subscribe(['test'])

    k="old messages:\n"
    b="new messages:\n"
    for message in consumer:
        print(message.value)
        k+=message.value+"\n"
        b=message.value
    c=k+"\n"+b


    return c

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8080)
