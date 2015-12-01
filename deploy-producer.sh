#!/bin/bash

virtualenv venv
./venv/bin/python ./venv/bin/pip install pika

curl https://raw.githubusercontent.com/powellchristoph/mesos-test/master/producer.py > producer.py
