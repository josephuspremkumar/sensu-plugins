#!/bin/python
     
import json
import subprocess
import sys
import logging
import commands
     
logging.basicConfig(filename='/tmp/sensu-nagios.log',level=logging.DEBUG)
     
json_string = sys.stdin.readline()

#json_string='{"id":"88096a16-381d-4e81-bc6e-9859d08cbc4d","client":{"name":"OSP-Director","address":"localhost","subscriptions":["test"],"version":"0.16.0","timestamp":1441352236},"check":{"command":"/etc/sensu/plugins/check-test.sh","interval":10,"handler":"default","subscribers":["test"],"name":"checktest","issued":1441352246,"executed":1441352246,"duration":0.01,"output":"WARNING - Hello there\n","status":1,"history":["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]},"occurrences":856,"action":"create"}'
     
parsed_json=json.loads(json_string.replace('\n',''))
     
client_name=parsed_json['client']['name']
event_string=parsed_json['check']['output']
status=parsed_json['check']['status']
     
logging.info('client_name: %s, event_string: %s, status: %d',client_name,event_string,status)
     
#command="/usr/bin/snmptrap -v 2c -c public 10.0.2.120 '' NAGIOS-NOTIFY-MIB::nHostNotify nHostName s "+"\""+client_name+"\""+" nHostOutput s "+"\""+event_string+"\""+" nHostStateID i "+str(status)

command="/usr/bin/snmptrap -v 2c -c public 10.0.2.120 '' NAGIOS-NOTIFY-MIB::nSvcEvent nSvcHostname s "+"\""+client_name+"\""+" nSvcOutput s "+"\""+event_string+"\""+" nSvcStateID i "+str(status)
     
commands.getoutput(command)
     
logging.info(command)
