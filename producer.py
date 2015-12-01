import os
import logging
import logging.handlers
from random import randint
from time import sleep

import pika

r_server = os.getenv('RABBITMQ_SERVER', 'localhost')
interval = os.getenv('TEST_INTERVAL', 2)
logserver = os.getenv('SYSLOG_SERVER', 'localhost')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address=(logserver, 514))
formatter = logging.Formatter('MESOS-PRODUCER %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info('Producer is starting!')

connection = pika.BlockingConnection(pika.ConnectionParameters(host=r_server))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

num = 0

while True:
    num += 1
    message = "Job #{}: {}".format(num, randint(1,10))
    logger.info(message)
    channel.basic_publish(exchange='',
            routing_key='task_queue', body=message,
            properties=pika.BasicProperties(delivery_mode=2,)
            )
    sleep(interval)

connection.close()
