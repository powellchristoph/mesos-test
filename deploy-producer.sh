#!/bin/bash

cleanup() {
    rm -rf venv
}
trap cleanup EXIT

virtualenv venv
source venv/bin/activate
pip install pika

curl https://raw.githubusercontent.com/powellchristoph/mesos-test/master/producer.py > producer.py

python producer.py
