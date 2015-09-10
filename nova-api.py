#!/usr/bin/python

from novaclient import client
import sys

state=2
version=2
user=sys.argv[1]
password=sys.argv[2]
tenant=sys.argv[3]
url=sys.argv[4]

try:
  nova=client.Client(version,user,password,tenant,url)
# print nova.servers.list()
  print("OK - Nova API working fine")
  state=0
except:
  print("CRITICAL - Nova API down")

sys.exit(state)


