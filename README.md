# Some example sensu-plugins

## Sensu checks

* check-ping.sh - Will ping to other nodes written in /etc/sensu/plugins/ping_nodes_list 
* check-ps.sh - Will check if the list of processes written in /etc/sensu/plugins/process_list are running
* nova-api.py - Will check if OpenStack nova API is in working condition

## Sensu Handler 

* nagios-snmp.py - Forward sensu events as nagios-notify-mib traps (needs netsnmp utils installed on the sensu-server node)
