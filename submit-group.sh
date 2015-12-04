#!/bin/bash
APP=$1
GROUP=`basename $APP .json`
curl -X DELETE http://localhost:8080/v2/groups/$GROUP
sleep 5
curl -X POST http://localhost:8080/v2/groups -d @${APP} -H "Content-type: application/json"
