#!/bin/bash

pid="$(pgrep -f 9876)"
if [ ${#pid} -ge 1 ]; then 
  kill ${pid}
  echo "Sprintreporter killed"
else
  echo "Sprintreporter is not running"
fi
