#!/bin/bash

cleanup() {
    rm -rf venv
}
trap cleanup EXIT

virtualenv venv
./venv/bin/python ./venv/bin/pip install pika

curl https://raw.githubusercontent.com/powellchristoph/mesos-test/master/producer.py > producer.py
