#!/usr/bin/python

import CloudStack

api = 'http://example.com:8080/client/api'
apikey = 'API KEY'
secret = 'API SECRET'

cloudstack = CloudStack.Client(api, apikey, secret)

vms = cloudstack.listVirtualMachines()

for vm in vms:
    print "%s %s %s" % (vm['id'], vm['name'], vm['state'])
