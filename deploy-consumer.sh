#!/bin/bash

virtualenv venv

source venv/bin/activate
pip install pika
pip install names

curl https://raw.githubusercontent.com/powellchristoph/mesos-test/master/consumer.py > consumer.py

python consumer.py
