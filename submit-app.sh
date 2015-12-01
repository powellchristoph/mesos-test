#!/bin/bash

APP=$1
curl -X POST http://localhost:8080/v2/apps -d @${APP} -H "Content-type: application/json"
