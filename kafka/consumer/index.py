import os
from flask import Flask
import sys
from kafka import KafkaConsumer

server=sys.argv[1]

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }
application = Flask(__name__)

@application.route("/")
def hello():
    consumer = KafkaConsumer(bootstrap_servers=server,
                             auto_offset_reset='earliest',
                             consumer_timeout_ms=1000)
    consumer.subscribe(['test'])

    old_messages="old_messages:\n"
    new_messages="new_messages:\n"
    last_message="\n"
    for message in consumer:
        print(message.value)
        print '\n'
        old_messages+=message.value
        last_message=message.value
    new_messages="new_messages:\n"+last_message
    return_values=old_messages+"\n"+new_messages


    return return_values

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8080)
