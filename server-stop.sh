#!/bin/bash

pid="$(pgrep -f 5000)"
if [ ${#pid} -ge 1 ]; then 
  kill ${pid}
  echo "Sprintreporter killed"
else
  echo "Sprintreporter is not running"
fi
