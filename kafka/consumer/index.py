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

    k="messages:"
    for message in consumer:
        print(message.value)
        k+=message.value

    return k

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8080)