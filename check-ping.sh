#!/bin/bash

nodes_list=""
failed_nodes_list=""
total_failed_nodes=0
error=0

for i in `cat /etc/sensu/plugins/ping_nodes_list`
do
 ping -c 1 $i >/dev/null 2>&1
 error=$?
 if [ $error -eq 0 ]; then
   nodes_list+=$i", "
 else
   failed_nodes_list+=$i", "
   total_failed_nodes+=1
 fi
done

if [ $total_failed_nodes -eq 0 ]; then
  if [ -z "$nodes_list" ]; then
    echo "OK - NO NODES CONFIGURED FOR PING TEST"
    exit 0
  fi
  echo "OK - Ping test sucessful to" $nodes_list
  exit 0
else
  echo "CRITICAL - ping test failed to" $failed_nodes_list
  exit 2
fi
