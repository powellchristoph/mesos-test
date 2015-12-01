import os
import logging
import logging.handlers
from time import sleep

import pika
import names

logserver = os.getenv('SYSLOG_SERVER', 'localhost')
r_server = os.getenv('RABBITMQ_SERVER', 'localhost')

slave_name = names.get_first_name().upper()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address=(logserver, 514))
formatter = logging.Formatter('MESOS-SLAVE-{} %(levelname)s %(message)s'.format(slave_name))
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Slave-{} is starting!".format(slave_name))

connection = pika.BlockingConnection(pika.ConnectionParameters(host=r_server))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
        #Job #3: 10
        job = body.split(':')[0]
        sleep_time = float(body.split(':')[1].strip())
        logger.info("Claiming {}, working for {} seconds.".format(job, sleep_time))
        sleep(sleep_time)
        ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,queue='task_queue')
channel.start_consuming()
