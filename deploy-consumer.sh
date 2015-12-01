#!/bin/bash

virtualenv venv
./venv/bin/python ./venv/bin/pip install pika
./venv/bin/python ./venv/bin/pip install names

curl https://raw.githubusercontent.com/powellchristoph/mesos-test/master/consumer.py > consumer.py
