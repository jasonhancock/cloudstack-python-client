from BaseClient import BaseClient

class Client(BaseClient):
    def createNetworkOffering(self, args={}):
        '''
        Creates a network offering.

        args - A dictionary. The following are options for keys:
            displaytext - the display text of the network offering
            guestiptype - guest type of the network offering: Shared or Isolated
            name - the name of the network offering
            supportedservices - services supported by the network offering
            traffictype - the traffic type for the network offering. Supported type in
               current release is GUEST only
            availability - the availability of network offering. Default value is
               Optional
            conservemode - true if the network offering is IP conserve mode enabled
            networkrate - data transfer rate in megabits per second allowed
            servicecapabilitylist - desired service capabilities as part of network
               offering
            serviceofferingid - the service offering ID used by virtual router provider
            serviceproviderlist - provider to service mapping. If not specified, the
               provider for the service will be mapped to the default provider on the physical
               network
            specifyipranges - true if network offering supports specifying ip ranges;
               defaulted to false if not specified
            specifyvlan - true if network offering supports vlans
            tags - the tags for the network offering.
        '''
        if not 'displaytext' in args:
            raise RuntimeError("Missing required argument 'displaytext'")
        if not 'guestiptype' in args:
            raise RuntimeError("Missing required argument 'guestiptype'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'supportedservices' in args:
            raise RuntimeError("Missing required argument 'supportedservices'")
        if not 'traffictype' in args:
            raise RuntimeError("Missing required argument 'traffictype'")

        return self.request('createNetworkOffering', args)
 

    def updateNetworkOffering(self, args={}):
        '''
        Updates a network offering.

        args - A dictionary. The following are options for keys:
            availability - the availability of network offering. Default value is
               Required for Guest Virtual network offering; Optional for Guest Direct network
               offering
            displaytext - the display text of the network offering
            id - the id of the network offering
            name - the name of the network offering
            sortkey - sort key of the network offering, integer
            state - update state for the network offering
        '''

        return self.request('updateNetworkOffering', args)
 

    def deleteNetworkOffering(self, args={}):
        '''
        Deletes a network offering.

        args - A dictionary. The following are options for keys:
            id - the ID of the network offering
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteNetworkOffering', args)
 

    def listNetworkOfferings(self, args={}):
        '''
        Lists all available network offerings.

        args - A dictionary. The following are options for keys:
            availability - the availability of network offering. Default value is
               Required
            displaytext - list network offerings by display text
            guestiptype - list network offerings by guest type: Shared or Isolated
            id - list network offerings by id
            isdefault - true if need to list only default network offerings. Default
               value is false
            istagged - true if offering has tags specified
            keyword - List by keyword
            name - list network offerings by name
            networkid - the ID of the network. Pass this in if you want to see the
               available network offering that a network can be changed to.
            page - 
            pagesize - 
            sourcenatsupported - true if need to list only netwok offerings where source
               nat is supported, false otherwise
            specifyipranges - true if need to list only network offerings which support
               specifying ip ranges
            specifyvlan - the tags for the network offering.
            state - list network offerings by state
            supportedservices - list network offerings supporting certain services
            tags - list network offerings by tags
            traffictype - list by traffic type
            zoneid - list netowrk offerings available for network creation in specific
               zone
            page - Pagination
        '''

        return self.request('listNetworkOfferings', args)
 

    def createNetwork(self, args={}):
        '''
        Creates a network

        args - A dictionary. The following are options for keys:
            displaytext - the display text of the network
            name - the name of the network
            networkofferingid - the network offering id
            zoneid - the Zone ID for the network
            account - account who will own the network
            acltype - Access control type; supported values are account and domain. In
               3.0 all shared networks should have aclType=Domain, and all Isolated networks -
               Account. Account means that only the account owner can use the network, domain -
               all accouns in the domain can use the network
            domainid - domain ID of the account owning a network
            endip - the ending IP address in the network IP range. If not specified,
               will be defaulted to startIP
            gateway - the gateway of the network
            netmask - the netmask of the network
            networkdomain - network domain
            physicalnetworkid - the Physical Network ID the network belongs to
            projectid - an optional project for the ssh key
            startip - the beginning IP address in the network IP range
            subdomainaccess - Defines whether to allow subdomains to use networks
               dedicated to their parent domain(s). Should be used with aclType=Domain,
               defaulted to allow.subdomain.network.access global config if not specified
            vlan - the ID or VID of the network
        '''
        if not 'displaytext' in args:
            raise RuntimeError("Missing required argument 'displaytext'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'networkofferingid' in args:
            raise RuntimeError("Missing required argument 'networkofferingid'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('createNetwork', args)
 

    def deleteNetwork(self, args={}):
        '''
        Deletes a network

        args - A dictionary. The following are options for keys:
            id - the ID of the network
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteNetwork', args)
 

    def listNetworks(self, args={}):
        '''
        Lists all available networks.

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            acltype - list networks by ACL (access control list) type. Supported values
               are Account and Domain
            domainid - list only resources belonging to the domain specified
            id - list networks by id
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            issystem - true if network is system, false otherwise
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            page - 
            pagesize - 
            physicalnetworkid - list networks by physical network id
            projectid - list firewall rules by project
            restartrequired - list network offerings by restartRequired option
            specifyipranges - true if need to list only networks which support
               specifying ip ranges
            supportedservices - list network offerings supporting certain services
            traffictype - type of the traffic
            type - the type of the network. Supported values are: Isolated and Shared
            zoneid - the Zone ID of the network
            page - Pagination
        '''

        return self.request('listNetworks', args)
 

    def restartNetwork(self, args={}):
        '''
        Restarts the network; includes 1) restarting network elements - virtual routers,
        dhcp servers 2) reapplying all public ips 3) reapplying
        loadBalancing/portForwarding rules

        args - A dictionary. The following are options for keys:
            id - The id of the network to restart.
            cleanup - If cleanup old network elements
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('restartNetwork', args)
 

    def updateNetwork(self, args={}):
        '''
        Updates a network

        args - A dictionary. The following are options for keys:
            id - the ID of the network
            changecidr - Force update even if cidr type is different
            displaytext - the new display text for the network
            name - the new name for the network
            networkdomain - network domain
            networkofferingid - network offering ID
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateNetwork', args)
 

    def createPhysicalNetwork(self, args={}):
        '''
        Creates a physical network

        args - A dictionary. The following are options for keys:
            name - the name of the physical network
            zoneid - the Zone ID for the physical network
            broadcastdomainrange - the broadcast domain range for the physical
               network[Pod or Zone]. In Acton release it can be Zone only in Advance zone, and
               Pod in Basic
            domainid - domain ID of the account owning a physical network
            isolationmethods - the isolation method for the physical
               network[VLAN/L3/GRE]
            networkspeed - the speed for the physical network[1G/10G]
            tags - Tag the physical network
            vlan - the VLAN for the physical network
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('createPhysicalNetwork', args)
 

    def deletePhysicalNetwork(self, args={}):
        '''
        Deletes a Physical Network.

        args - A dictionary. The following are options for keys:
            id - the ID of the Physical network
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deletePhysicalNetwork', args)
 

    def listPhysicalNetworks(self, args={}):
        '''
        Lists physical networks

        args - A dictionary. The following are options for keys:
            id - list physical network by id
            keyword - List by keyword
            name - search by name
            page - 
            pagesize - 
            zoneid - the Zone ID for the physical network
            page - Pagination
        '''

        return self.request('listPhysicalNetworks', args)
 

    def updatePhysicalNetwork(self, args={}):
        '''
        Updates a physical network

        args - A dictionary. The following are options for keys:
            id - physical network id
            networkspeed - the speed for the physical network[1G/10G]
            state - Enabled/Disabled
            tags - Tag the physical network
            vlan - the VLAN for the physical network
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updatePhysicalNetwork', args)
 

    def listSupportedNetworkServices(self, args={}):
        '''
        Lists all network services provided by CloudStack or for the given Provider.

        args - A dictionary. The following are options for keys:
            keyword - List by keyword
            page - 
            pagesize - 
            provider - network service provider name
            service - network service name to list providers and capabilities of
            page - Pagination
        '''

        return self.request('listSupportedNetworkServices', args)
 

    def addNetworkServiceProvider(self, args={}):
        '''
        Adds a network serviceProvider to a physical network

        args - A dictionary. The following are options for keys:
            name - the name for the physical network service provider
            physicalnetworkid - the Physical Network ID to add the provider to
            destinationphysicalnetworkid - the destination Physical Network ID to bridge
               to
            servicelist - the list of services to be enabled for this physical network
               service provider
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'physicalnetworkid' in args:
            raise RuntimeError("Missing required argument 'physicalnetworkid'")

        return self.request('addNetworkServiceProvider', args)
 

    def deleteNetworkServiceProvider(self, args={}):
        '''
        Deletes a Network Service Provider.

        args - A dictionary. The following are options for keys:
            id - the ID of the network service provider
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteNetworkServiceProvider', args)
 

    def listNetworkServiceProviders(self, args={}):
        '''
        Lists network serviceproviders for a given physical network.

        args - A dictionary. The following are options for keys:
            keyword - List by keyword
            name - list providers by name
            page - 
            pagesize - 
            physicalnetworkid - the Physical Network ID
            state - list providers by state
            page - Pagination
        '''

        return self.request('listNetworkServiceProviders', args)
 

    def updateNetworkServiceProvider(self, args={}):
        '''
        Updates a network serviceProvider of a physical network

        args - A dictionary. The following are options for keys:
            id - network service provider id
            servicelist - the list of services to be enabled for this physical network
               service provider
            state - Enabled/Disabled/Shutdown the physical network service provider
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateNetworkServiceProvider', args)
 

    def createStorageNetworkIpRange(self, args={}):
        '''
        Creates a Storage network IP range.

        args - A dictionary. The following are options for keys:
            gateway - the gateway for storage network
            netmask - the netmask for storage network
            podid - UUID of pod where the ip range belongs to
            startip - the beginning IP address
            endip - the ending IP address
            vlan - Optional. The vlan the ip range sits on, default to Null when it is
               not specificed which means you network is not on any Vlan. This is mainly for
               Vmware as other hypervisors can directly reterive bridge from pyhsical network
               traffic type table
        '''
        if not 'gateway' in args:
            raise RuntimeError("Missing required argument 'gateway'")
        if not 'netmask' in args:
            raise RuntimeError("Missing required argument 'netmask'")
        if not 'podid' in args:
            raise RuntimeError("Missing required argument 'podid'")
        if not 'startip' in args:
            raise RuntimeError("Missing required argument 'startip'")

        return self.request('createStorageNetworkIpRange', args)
 

    def deleteStorageNetworkIpRange(self, args={}):
        '''
        Deletes a storage network IP Range.

        args - A dictionary. The following are options for keys:
            id - the uuid of the storage network ip range
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteStorageNetworkIpRange', args)
 

    def listStorageNetworkIpRange(self, args={}):
        '''
        List a storage network IP range.

        args - A dictionary. The following are options for keys:
            id - optional parameter. Storaget network IP range uuid, if specicied, using
               it to search the range.
            keyword - List by keyword
            page - 
            pagesize - 
            podid - optional parameter. Pod uuid, if specicied and range uuid is absent,
               using it to search the range.
            zoneid - optional parameter. Zone uuid, if specicied and both pod uuid and
               range uuid are absent, using it to search the range.
            page - Pagination
        '''

        return self.request('listStorageNetworkIpRange', args)
 

    def updateStorageNetworkIpRange(self, args={}):
        '''
        Update a Storage network IP range, only allowed when no IPs in this range have
        been allocated.

        args - A dictionary. The following are options for keys:
            id - UUID of storage network ip range
            endip - the ending IP address
            netmask - the netmask for storage network
            startip - the beginning IP address
            vlan - Optional. the vlan the ip range sits on
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateStorageNetworkIpRange', args)
 

    def addNetworkDevice(self, args={}):
        '''
        Adds a network device of one of the following types: ExternalDhcp,
        ExternalFirewall, ExternalLoadBalancer, PxeServer

        args - A dictionary. The following are options for keys:
            networkdeviceparameterlist - parameters for network device
            networkdevicetype - Network device type, now supports ExternalDhcp,
               PxeServer, NetscalerMPXLoadBalancer, NetscalerVPXLoadBalancer,
               NetscalerSDXLoadBalancer, F5BigIpLoadBalancer, JuniperSRXFirewall
        '''

        return self.request('addNetworkDevice', args)
 

    def listNetworkDevice(self, args={}):
        '''
        List network devices

        args - A dictionary. The following are options for keys:
            keyword - List by keyword
            networkdeviceparameterlist - parameters for network device
            networkdevicetype - Network device type, now supports ExternalDhcp,
               PxeServer, NetscalerMPXLoadBalancer, NetscalerVPXLoadBalancer,
               NetscalerSDXLoadBalancer, F5BigIpLoadBalancer, JuniperSRXFirewall
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listNetworkDevice', args)
 

    def deleteNetworkDevice(self, args={}):
        '''
        Deletes network device.

        args - A dictionary. The following are options for keys:
            id - Id of network device to delete
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteNetworkDevice', args)
 

    def listF5LoadBalancerNetworks(self, args={}):
        '''
        lists network that are using a F5 load balancer device

        args - A dictionary. The following are options for keys:
            lbdeviceid - f5 load balancer device ID
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''
        if not 'lbdeviceid' in args:
            raise RuntimeError("Missing required argument 'lbdeviceid'")

        return self.request('listF5LoadBalancerNetworks', args)
 

    def listSrxFirewallNetworks(self, args={}):
        '''
        lists network that are using SRX firewall device

        args - A dictionary. The following are options for keys:
            lbdeviceid - netscaler load balancer device ID
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''
        if not 'lbdeviceid' in args:
            raise RuntimeError("Missing required argument 'lbdeviceid'")

        return self.request('listSrxFirewallNetworks', args)
 

    def listNetscalerLoadBalancerNetworks(self, args={}):
        '''
        lists network that are using a netscaler load balancer device

        args - A dictionary. The following are options for keys:
            lbdeviceid - netscaler load balancer device ID
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''
        if not 'lbdeviceid' in args:
            raise RuntimeError("Missing required argument 'lbdeviceid'")

        return self.request('listNetscalerLoadBalancerNetworks', args)
 

    def createLoadBalancerRule(self, args={}):
        '''
        Creates a load balancer rule

        args - A dictionary. The following are options for keys:
            algorithm - load balancer algorithm (source, roundrobin, leastconn)
            name - name of the load balancer rule
            privateport - the private port of the private ip address/virtual machine
               where the network traffic will be load balanced to
            publicport - the public port from where the network traffic will be load
               balanced from
            account - the account associated with the load balancer. Must be used with
               the domainId parameter.
            cidrlist - the cidr list to forward traffic from
            description - the description of the load balancer rule
            domainid - the domain ID associated with the load balancer
            networkid - The guest network this rule will be created for
            openfirewall - if true, firewall rule for source/end pubic port is
               automatically created; if false - firewall rule has to be created explicitely.
               Has value true by default
            publicipid - public ip address id from where the network traffic will be
               load balanced from
            zoneid - zone where the load balancer is going to be created. This parameter
               is required when LB service provider is ElasticLoadBalancerVm
        '''
        if not 'algorithm' in args:
            raise RuntimeError("Missing required argument 'algorithm'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'privateport' in args:
            raise RuntimeError("Missing required argument 'privateport'")
        if not 'publicport' in args:
            raise RuntimeError("Missing required argument 'publicport'")

        return self.request('createLoadBalancerRule', args)
 

    def deleteLoadBalancerRule(self, args={}):
        '''
        Deletes a load balancer rule.

        args - A dictionary. The following are options for keys:
            id - the ID of the load balancer rule
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteLoadBalancerRule', args)
 

    def removeFromLoadBalancerRule(self, args={}):
        '''
        Removes a virtual machine or a list of virtual machines from a load balancer
        rule.

        args - A dictionary. The following are options for keys:
            id - The ID of the load balancer rule
            virtualmachineids - the list of IDs of the virtual machines that are being
               removed from the load balancer rule (i.e. virtualMachineIds=1,2,3)
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'virtualmachineids' in args:
            raise RuntimeError("Missing required argument 'virtualmachineids'")

        return self.request('removeFromLoadBalancerRule', args)
 

    def assignToLoadBalancerRule(self, args={}):
        '''
        Assigns virtual machine or a list of virtual machines to a load balancer rule.

        args - A dictionary. The following are options for keys:
            id - the ID of the load balancer rule
            virtualmachineids - the list of IDs of the virtual machine that are being
               assigned to the load balancer rule(i.e. virtualMachineIds=1,2,3)
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'virtualmachineids' in args:
            raise RuntimeError("Missing required argument 'virtualmachineids'")

        return self.request('assignToLoadBalancerRule', args)
 

    def createLBStickinessPolicy(self, args={}):
        '''
        Creates a Load Balancer stickiness policy

        args - A dictionary. The following are options for keys:
            lbruleid - the ID of the load balancer rule
            methodname - name of the LB Stickiness policy method, possible values can be
               obtained from ListNetworks API
            name - name of the LB Stickiness policy
            description - the description of the LB Stickiness policy
            param - param list. Example:
               param[0].name=cookiename&param[0].value=LBCookie
        '''
        if not 'lbruleid' in args:
            raise RuntimeError("Missing required argument 'lbruleid'")
        if not 'methodname' in args:
            raise RuntimeError("Missing required argument 'methodname'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('createLBStickinessPolicy', args)
 

    def deleteLBStickinessPolicy(self, args={}):
        '''
        Deletes a LB stickiness policy.

        args - A dictionary. The following are options for keys:
            id - the ID of the LB stickiness policy
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteLBStickinessPolicy', args)
 

    def listLoadBalancerRules(self, args={}):
        '''
        Lists load balancer rules.

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            id - the ID of the load balancer rule
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            name - the name of the load balancer rule
            page - 
            pagesize - 
            projectid - list firewall rules by project
            publicipid - the public IP address id of the load balancer rule
            virtualmachineid - the ID of the virtual machine of the load balancer rule
            zoneid - the availability zone ID
            page - Pagination
        '''

        return self.request('listLoadBalancerRules', args)
 

    def listLBStickinessPolicies(self, args={}):
        '''
        Lists LBStickiness policies.

        args - A dictionary. The following are options for keys:
            lbruleid - the ID of the load balancer rule
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''
        if not 'lbruleid' in args:
            raise RuntimeError("Missing required argument 'lbruleid'")

        return self.request('listLBStickinessPolicies', args)
 

    def listLoadBalancerRuleInstances(self, args={}):
        '''
        List all virtual machine instances that are assigned to a load balancer rule.

        args - A dictionary. The following are options for keys:
            id - the ID of the load balancer rule
            applied - true if listing all virtual machines currently applied to the load
               balancer rule; default is true
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('listLoadBalancerRuleInstances', args)
 

    def updateLoadBalancerRule(self, args={}):
        '''
        Updates load balancer

        args - A dictionary. The following are options for keys:
            id - the id of the load balancer rule to update
            algorithm - load balancer algorithm (source, roundrobin, leastconn)
            description - the description of the load balancer rule
            name - the name of the load balancer rule
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateLoadBalancerRule', args)
 

    def addF5LoadBalancer(self, args={}):
        '''
        Adds a F5 BigIP load balancer device

        args - A dictionary. The following are options for keys:
            networkdevicetype - supports only F5BigIpLoadBalancer
            password - Credentials to reach F5 BigIP load balancer device
            physicalnetworkid - the Physical Network ID
            url - URL of the F5 load balancer appliance.
            username - Credentials to reach F5 BigIP load balancer device
        '''
        if not 'networkdevicetype' in args:
            raise RuntimeError("Missing required argument 'networkdevicetype'")
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")
        if not 'physicalnetworkid' in args:
            raise RuntimeError("Missing required argument 'physicalnetworkid'")
        if not 'url' in args:
            raise RuntimeError("Missing required argument 'url'")
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")

        return self.request('addF5LoadBalancer', args)
 

    def configureF5LoadBalancer(self, args={}):
        '''
        configures a F5 load balancer device

        args - A dictionary. The following are options for keys:
            lbdeviceid - F5 load balancer device ID
            lbdevicecapacity - capacity of the device, Capacity will be interpreted as
               number of networks device can handle
        '''
        if not 'lbdeviceid' in args:
            raise RuntimeError("Missing required argument 'lbdeviceid'")

        return self.request('configureF5LoadBalancer', args)
 

    def deleteF5LoadBalancer(self, args={}):
        '''
        delete a F5 load balancer device

        args - A dictionary. The following are options for keys:
            lbdeviceid - netscaler load balancer device ID
        '''
        if not 'lbdeviceid' in args:
            raise RuntimeError("Missing required argument 'lbdeviceid'")

        return self.request('deleteF5LoadBalancer', args)
 

    def listF5LoadBalancers(self, args={}):
        '''
        lists F5 load balancer devices

        args - A dictionary. The following are options for keys:
            keyword - List by keyword
            lbdeviceid - f5 load balancer device ID
            page - 
            pagesize - 
            physicalnetworkid - the Physical Network ID
            page - Pagination
        '''

        return self.request('listF5LoadBalancers', args)
 

    def addNetscalerLoadBalancer(self, args={}):
        '''
        Adds a netscaler load balancer device

        args - A dictionary. The following are options for keys:
            networkdevicetype - Netscaler device type supports NetscalerMPXLoadBalancer,
               NetscalerVPXLoadBalancer, NetscalerSDXLoadBalancer
            password - Credentials to reach netscaler load balancer device
            physicalnetworkid - the Physical Network ID
            url - URL of the netscaler load balancer appliance.
            username - Credentials to reach netscaler load balancer device
        '''
        if not 'networkdevicetype' in args:
            raise RuntimeError("Missing required argument 'networkdevicetype'")
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")
        if not 'physicalnetworkid' in args:
            raise RuntimeError("Missing required argument 'physicalnetworkid'")
        if not 'url' in args:
            raise RuntimeError("Missing required argument 'url'")
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")

        return self.request('addNetscalerLoadBalancer', args)
 

    def deleteNetscalerLoadBalancer(self, args={}):
        '''
        delete a netscaler load balancer device

        args - A dictionary. The following are options for keys:
            lbdeviceid - netscaler load balancer device ID
        '''
        if not 'lbdeviceid' in args:
            raise RuntimeError("Missing required argument 'lbdeviceid'")

        return self.request('deleteNetscalerLoadBalancer', args)
 

    def configureNetscalerLoadBalancer(self, args={}):
        '''
        configures a netscaler load balancer device

        args - A dictionary. The following are options for keys:
            lbdeviceid - Netscaler load balancer device ID
            inline - true if netscaler load balancer is intended to be used in in-line
               with firewall, false if netscaler load balancer will side-by-side with firewall
            lbdevicecapacity - capacity of the device, Capacity will be interpreted as
               number of networks device can handle
            lbdevicededicated - true if this netscaler device to dedicated for a
               account, false if the netscaler device will be shared by multiple accounts
        '''
        if not 'lbdeviceid' in args:
            raise RuntimeError("Missing required argument 'lbdeviceid'")

        return self.request('configureNetscalerLoadBalancer', args)
 

    def listNetscalerLoadBalancers(self, args={}):
        '''
        lists netscaler load balancer devices

        args - A dictionary. The following are options for keys:
            keyword - List by keyword
            lbdeviceid - netscaler load balancer device ID
            page - 
            pagesize - 
            physicalnetworkid - the Physical Network ID
            page - Pagination
        '''

        return self.request('listNetscalerLoadBalancers', args)
 

    def deployVirtualMachine(self, args={}):
        '''
        Creates and automatically starts a virtual machine based on a service offering,
        disk offering, and template.

        args - A dictionary. The following are options for keys:
            serviceofferingid - the ID of the service offering for the virtual machine
            templateid - the ID of the template for the virtual machine
            zoneid - availability zone for the virtual machine
            account - an optional account for the virtual machine. Must be used with
               domainId.
            diskofferingid - the ID of the disk offering for the virtual machine. If the
               template is of ISO format, the diskOfferingId is for the root disk volume.
               Otherwise this parameter is used to indicate the offering for the data disk
               volume. If the templateId parameter passed is from a Template object, the
               diskOfferingId refers to a DATA Disk Volume created. If the templateId parameter
               passed is from an ISO object, the diskOfferingId refers to a ROOT Disk Volume
               created.
            displayname - an optional user generated name for the virtual machine
            domainid - an optional domainId for the virtual machine. If the account
               parameter is used, domainId must also be used.
            group - an optional group for the virtual machine
            hostid - destination Host ID to deploy the VM to - parameter available for
               root admin only
            hypervisor - the hypervisor on which to deploy the virtual machine
            ipaddress - the ip address for default vm's network
            iptonetworklist - ip to network mapping. Can't be specified with networkIds
               parameter. Example:
               iptonetworklist[0].ip=10.10.10.11&iptonetworklist[0].networkid=204 - requests to
               use ip 10.10.10.11 in network id=204
            keyboard - an optional keyboard device type for the virtual machine. valid
               value can be one of de,de-ch,es,fi,fr,fr-be,fr-ch,is,it,jp,nl-be,no,pt,uk,us
            keypair - name of the ssh key pair used to login to the virtual machine
            name - host name for the virtual machine
            networkids - list of network ids used by virtual machine. Can't be specified
               with ipToNetworkList parameter
            projectid - Deploy vm for the project
            securitygroupids - comma separated list of security groups id that going to
               be applied to the virtual machine. Should be passed only when vm is created from
               a zone with Basic Network support. Mutually exclusive with securitygroupnames
               parameter
            securitygroupnames - comma separated list of security groups names that
               going to be applied to the virtual machine. Should be passed only when vm is
               created from a zone with Basic Network support. Mutually exclusive with
               securitygroupids parameter
            size - the arbitrary size for the DATADISK volume. Mutually exclusive with
               diskOfferingId
            userdata - an optional binary data that can be sent to the virtual machine
               upon a successful deployment. This binary data must be base64 encoded before
               adding it to the request. Currently only HTTP GET is supported. Using HTTP GET
               (via querystring), you can send up to 2KB of data after base64 encoding.
        '''
        if not 'serviceofferingid' in args:
            raise RuntimeError("Missing required argument 'serviceofferingid'")
        if not 'templateid' in args:
            raise RuntimeError("Missing required argument 'templateid'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('deployVirtualMachine', args)
 

    def destroyVirtualMachine(self, args={}):
        '''
        Destroys a virtual machine. Once destroyed, only the administrator can recover
        it.

        args - A dictionary. The following are options for keys:
            id - The ID of the virtual machine
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('destroyVirtualMachine', args)
 

    def rebootVirtualMachine(self, args={}):
        '''
        Reboots a virtual machine.

        args - A dictionary. The following are options for keys:
            id - The ID of the virtual machine
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('rebootVirtualMachine', args)
 

    def startVirtualMachine(self, args={}):
        '''
        Starts a virtual machine.

        args - A dictionary. The following are options for keys:
            id - The ID of the virtual machine
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('startVirtualMachine', args)
 

    def stopVirtualMachine(self, args={}):
        '''
        Stops a virtual machine.

        args - A dictionary. The following are options for keys:
            id - The ID of the virtual machine
            forced - Force stop the VM.  The caller knows the VM is stopped.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('stopVirtualMachine', args)
 

    def resetPasswordForVirtualMachine(self, args={}):
        '''
        Resets the password for virtual machine. The virtual machine must be in a
        "Stopped" state and the template must already support this feature for this
        command to take effect. [async]

        args - A dictionary. The following are options for keys:
            id - The ID of the virtual machine
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('resetPasswordForVirtualMachine', args)
 

    def changeServiceForVirtualMachine(self, args={}):
        '''
        Changes the service offering for a virtual machine. The virtual machine must be
        in a "Stopped" state for this command to take effect.

        args - A dictionary. The following are options for keys:
            id - The ID of the virtual machine
            serviceofferingid - the service offering ID to apply to the virtual machine
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'serviceofferingid' in args:
            raise RuntimeError("Missing required argument 'serviceofferingid'")

        return self.request('changeServiceForVirtualMachine', args)
 

    def updateVirtualMachine(self, args={}):
        '''
        Updates parameters of a virtual machine.

        args - A dictionary. The following are options for keys:
            id - The ID of the virtual machine
            displayname - user generated name
            group - group of the virtual machine
            haenable - true if high-availability is enabled for the virtual machine,
               false otherwise
            ostypeid - the ID of the OS type that best represents this VM.
            userdata - an optional binary data that can be sent to the virtual machine
               upon a successful deployment. This binary data must be base64 encoded before
               adding it to the request. Currently only HTTP GET is supported. Using HTTP GET
               (via querystring), you can send up to 2KB of data after base64 encoding.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateVirtualMachine', args)
 

    def recoverVirtualMachine(self, args={}):
        '''
        Recovers a virtual machine.

        args - A dictionary. The following are options for keys:
            id - The ID of the virtual machine
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('recoverVirtualMachine', args)
 

    def listVirtualMachines(self, args={}):
        '''
        List the virtual machines owned by the account.

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            details - comma separated list of host details requested, value can be a
               list of [all, group, nics, stats, secgrp, tmpl, servoff, iso, volume, min]. If
               no parameter is passed in, the details will be defaulted to all
            domainid - list only resources belonging to the domain specified
            forvirtualnetwork - list by network type; true if need to list vms using
               Virtual Network, false otherwise
            groupid - the group ID
            hostid - the host ID
            hypervisor - the target hypervisor for the template
            id - the ID of the virtual machine
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            name - name of the virtual machine
            networkid - list by network id
            page - 
            pagesize - 
            podid - the pod ID
            projectid - list firewall rules by project
            state - state of the virtual machine
            storageid - the storage ID where vm's volumes belong to
            zoneid - the availability zone ID
            page - Pagination
        '''

        return self.request('listVirtualMachines', args)
 

    def getVMPassword(self, args={}):
        '''
        Returns an encrypted password for the VM

        args - A dictionary. The following are options for keys:
            id - The ID of the virtual machine
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('getVMPassword', args)
 

    def migrateVirtualMachine(self, args={}):
        '''
        Attempts Migration of a VM to a different host or Root volume of the vm to a
        different storage pool

        args - A dictionary. The following are options for keys:
            virtualmachineid - the ID of the virtual machine
            hostid - Destination Host ID to migrate VM to. Required for live migrating a
               VM from host to host
            storageid - Destination storage pool ID to migrate VM volumes to. Required
               for migrating the root disk volume
        '''
        if not 'virtualmachineid' in args:
            raise RuntimeError("Missing required argument 'virtualmachineid'")

        return self.request('migrateVirtualMachine', args)
 

    def assignVirtualMachine(self, args={}):
        '''
        Move a user VM to another user under same domain.

        args - A dictionary. The following are options for keys:
            account - account name of the new VM owner.
            domainid - domain id of the new VM owner.
            virtualmachineid - the vm ID of the user VM to be moved
            networkids - list of network ids that will be part of VM network after move
               in advanced network setting.
            securitygroupids - comma separated list of security groups id that going to
               be applied to the virtual machine. Should be passed only when vm is moved in a
               zone with Basic Network support.
        '''
        if not 'account' in args:
            raise RuntimeError("Missing required argument 'account'")
        if not 'domainid' in args:
            raise RuntimeError("Missing required argument 'domainid'")
        if not 'virtualmachineid' in args:
            raise RuntimeError("Missing required argument 'virtualmachineid'")

        return self.request('assignVirtualMachine', args)
 

    def restoreVirtualMachine(self, args={}):
        '''
        Restore a VM to original template or specific snapshot

        args - A dictionary. The following are options for keys:
            virtualmachineid - Virtual Machine ID
        '''
        if not 'virtualmachineid' in args:
            raise RuntimeError("Missing required argument 'virtualmachineid'")

        return self.request('restoreVirtualMachine', args)
 

    def addTrafficType(self, args={}):
        '''
        Adds traffic type to a physical network

        args - A dictionary. The following are options for keys:
            physicalnetworkid - the Physical Network ID
            traffictype - the trafficType to be added to the physical network
            kvmnetworklabel - The network name label of the physical device dedicated to
               this traffic on a KVM host
            vlan - The VLAN id to be used for Management traffic by VMware host
            vmwarenetworklabel - The network name label of the physical device dedicated
               to this traffic on a VMware host
            xennetworklabel - The network name label of the physical device dedicated to
               this traffic on a XenServer host
        '''
        if not 'physicalnetworkid' in args:
            raise RuntimeError("Missing required argument 'physicalnetworkid'")
        if not 'traffictype' in args:
            raise RuntimeError("Missing required argument 'traffictype'")

        return self.request('addTrafficType', args)
 

    def deleteTrafficType(self, args={}):
        '''
        Deletes traffic type of a physical network

        args - A dictionary. The following are options for keys:
            id - traffic type id
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteTrafficType', args)
 

    def listTrafficTypes(self, args={}):
        '''
        Lists traffic types of a given physical network.

        args - A dictionary. The following are options for keys:
            physicalnetworkid - the Physical Network ID
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''
        if not 'physicalnetworkid' in args:
            raise RuntimeError("Missing required argument 'physicalnetworkid'")

        return self.request('listTrafficTypes', args)
 

    def updateTrafficType(self, args={}):
        '''
        Updates traffic type of a physical network

        args - A dictionary. The following are options for keys:
            id - traffic type id
            kvmnetworklabel - The network name label of the physical device dedicated to
               this traffic on a KVM host
            vmwarenetworklabel - The network name label of the physical device dedicated
               to this traffic on a VMware host
            xennetworklabel - The network name label of the physical device dedicated to
               this traffic on a XenServer host
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateTrafficType', args)
 

    def listTrafficTypeImplementors(self, args={}):
        '''
        Lists implementors of implementor of a network traffic type or implementors of
        all network traffic types

        args - A dictionary. The following are options for keys:
            keyword - List by keyword
            page - 
            pagesize - 
            traffictype - Optional. The network traffic type, if specified, return its
               implementor. Otherwise, return all traffic types with their implementor
            page - Pagination
        '''

        return self.request('listTrafficTypeImplementors', args)
 

    def generateUsageRecords(self, args={}):
        '''
        Generates usage records. This will generate records only if there any records to
        be generated, i.e if the scheduled usage job was not run or failed

        args - A dictionary. The following are options for keys:
            enddate - End date range for usage record query. Use yyyy-MM-dd as the date
               format, e.g. startDate=2009-06-03.
            startdate - Start date range for usage record query. Use yyyy-MM-dd as the
               date format, e.g. startDate=2009-06-01.
            domainid - List events for the specified domain.
        '''
        if not 'enddate' in args:
            raise RuntimeError("Missing required argument 'enddate'")
        if not 'startdate' in args:
            raise RuntimeError("Missing required argument 'startdate'")

        return self.request('generateUsageRecords', args)
 

    def listUsageRecords(self, args={}):
        '''
        Lists usage records for accounts

        args - A dictionary. The following are options for keys:
            enddate - End date range for usage record query. Use yyyy-MM-dd as the date
               format, e.g. startDate=2009-06-03.
            startdate - Start date range for usage record query. Use yyyy-MM-dd as the
               date format, e.g. startDate=2009-06-01.
            account - List usage records for the specified user.
            accountid - List usage records for the specified account
            domainid - List usage records for the specified domain.
            keyword - List by keyword
            page - 
            pagesize - 
            projectid - List usage records for specified project
            type - List usage records for the specified usage type
            page - Pagination
        '''
        if not 'enddate' in args:
            raise RuntimeError("Missing required argument 'enddate'")
        if not 'startdate' in args:
            raise RuntimeError("Missing required argument 'startdate'")

        return self.request('listUsageRecords', args)
 

    def listUsageTypes(self, args={}):
        '''
        List Usage Types

        args - A dictionary. The following are options for keys:
            page - Pagination
        '''

        return self.request('listUsageTypes', args)
 

    def addTrafficMonitor(self, args={}):
        '''
        Adds Traffic Monitor Host for Direct Network Usage

        args - A dictionary. The following are options for keys:
            url - URL of the traffic monitor Host
            zoneid - Zone in which to add the external firewall appliance.
        '''
        if not 'url' in args:
            raise RuntimeError("Missing required argument 'url'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('addTrafficMonitor', args)
 

    def deleteTrafficMonitor(self, args={}):
        '''
        Deletes an traffic monitor host.

        args - A dictionary. The following are options for keys:
            id - Id of the Traffic Monitor Host.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteTrafficMonitor', args)
 

    def listTrafficMonitors(self, args={}):
        '''
        List traffic monitor Hosts.

        args - A dictionary. The following are options for keys:
            zoneid - zone Id
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('listTrafficMonitors', args)
 

    def attachVolume(self, args={}):
        '''
        Attaches a disk volume to a virtual machine.

        args - A dictionary. The following are options for keys:
            id - the ID of the disk volume
            virtualmachineid - the ID of the virtual machine
            deviceid - the ID of the device to map the volume to within the guest OS. If
               no deviceId is passed in, the next available deviceId will be chosen. Possible
               values for a Linux OS are:* 1 - /dev/xvdb* 2 - /dev/xvdc* 4 - /dev/xvde* 5 -
               /dev/xvdf* 6 - /dev/xvdg* 7 - /dev/xvdh* 8 - /dev/xvdi* 9 - /dev/xvdj
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'virtualmachineid' in args:
            raise RuntimeError("Missing required argument 'virtualmachineid'")

        return self.request('attachVolume', args)
 

    def detachVolume(self, args={}):
        '''
        Detaches a disk volume from a virtual machine.

        args - A dictionary. The following are options for keys:
            deviceid - the device ID on the virtual machine where volume is detached
               from
            id - the ID of the disk volume
            virtualmachineid - the ID of the virtual machine where the volume is
               detached from
        '''

        return self.request('detachVolume', args)
 

    def createVolume(self, args={}):
        '''
        Creates a disk volume from a disk offering. This disk volume must still be
        attached to a virtual machine to make use of it.

        args - A dictionary. The following are options for keys:
            name - the name of the disk volume
            account - the account associated with the disk volume. Must be used with the
               domainId parameter.
            diskofferingid - the ID of the disk offering. Either diskOfferingId or
               snapshotId must be passed in.
            domainid - the domain ID associated with the disk offering. If used with the
               account parameter returns the disk volume associated with the account for the
               specified domain.
            projectid - the project associated with the volume. Mutually exclusive with
               account parameter
            size - Arbitrary volume size
            snapshotid - the snapshot ID for the disk volume. Either diskOfferingId or
               snapshotId must be passed in.
            zoneid - the ID of the availability zone
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('createVolume', args)
 

    def deleteVolume(self, args={}):
        '''
        Deletes a detached disk volume.

        args - A dictionary. The following are options for keys:
            id - The ID of the disk volume
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteVolume', args)
 

    def listVolumes(self, args={}):
        '''
        Lists all volumes.

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            hostid - list volumes on specified host
            id - the ID of the disk volume
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            name - the name of the disk volume
            page - 
            pagesize - 
            podid - the pod id the disk volume belongs to
            projectid - list firewall rules by project
            type - the type of disk volume
            virtualmachineid - the ID of the virtual machine
            zoneid - the ID of the availability zone
            page - Pagination
        '''

        return self.request('listVolumes', args)
 

    def extractVolume(self, args={}):
        '''
        Extracts volume

        args - A dictionary. The following are options for keys:
            id - the ID of the volume
            mode - the mode of extraction - HTTP_DOWNLOAD or FTP_UPLOAD
            zoneid - the ID of the zone where the volume is located
            url - the url to which the volume would be extracted
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'mode' in args:
            raise RuntimeError("Missing required argument 'mode'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('extractVolume', args)
 

    def migrateVolume(self, args={}):
        '''
        Migrate volume

        args - A dictionary. The following are options for keys:
            storageid - destination storage pool ID to migrate the volume to
            volumeid - the ID of the volume
        '''
        if not 'storageid' in args:
            raise RuntimeError("Missing required argument 'storageid'")
        if not 'volumeid' in args:
            raise RuntimeError("Missing required argument 'volumeid'")

        return self.request('migrateVolume', args)
 

    def createVolumeOnFiler(self, args={}):
        '''
        Create a volume

        args - A dictionary. The following are options for keys:
            aggregatename - aggregate name.
            ipaddress - ip address.
            password - password.
            poolname - pool name.
            size - volume size.
            username - user name.
            volumename - volume name.
            snapshotpolicy - snapshot policy.
            snapshotreservation - snapshot reservation.
        '''
        if not 'aggregatename' in args:
            raise RuntimeError("Missing required argument 'aggregatename'")
        if not 'ipaddress' in args:
            raise RuntimeError("Missing required argument 'ipaddress'")
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")
        if not 'poolname' in args:
            raise RuntimeError("Missing required argument 'poolname'")
        if not 'size' in args:
            raise RuntimeError("Missing required argument 'size'")
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")
        if not 'volumename' in args:
            raise RuntimeError("Missing required argument 'volumename'")

        return self.request('createVolumeOnFiler', args)
 

    def destroyVolumeOnFiler(self, args={}):
        '''
        Destroy a Volume

        args - A dictionary. The following are options for keys:
            aggregatename - aggregate name.
            ipaddress - ip address.
            volumename - volume name.
        '''
        if not 'aggregatename' in args:
            raise RuntimeError("Missing required argument 'aggregatename'")
        if not 'ipaddress' in args:
            raise RuntimeError("Missing required argument 'ipaddress'")
        if not 'volumename' in args:
            raise RuntimeError("Missing required argument 'volumename'")

        return self.request('destroyVolumeOnFiler', args)
 

    def listVolumesOnFiler(self, args={}):
        '''
        List Volumes

        args - A dictionary. The following are options for keys:
            poolname - pool name.
            page - Pagination
        '''
        if not 'poolname' in args:
            raise RuntimeError("Missing required argument 'poolname'")

        return self.request('listVolumesOnFiler', args)
 

    def createUser(self, args={}):
        '''
        Creates a user for an account that already exists

        args - A dictionary. The following are options for keys:
            account - Creates the user under the specified account. If no account is
               specified, the username will be used as the account name.
            email - email
            firstname - firstname
            lastname - lastname
            password - Hashed password (Default is MD5). If you wish to use any other
               hashing algorithm, you would need to write a custom authentication adapter See
               Docs section.
            username - Unique username.
            domainid - Creates the user under the specified domain. Has to be
               accompanied with the account parameter
            timezone - Specifies a timezone for this command. For more information on
               the timezone parameter, see Time Zone Format.
        '''
        if not 'account' in args:
            raise RuntimeError("Missing required argument 'account'")
        if not 'email' in args:
            raise RuntimeError("Missing required argument 'email'")
        if not 'firstname' in args:
            raise RuntimeError("Missing required argument 'firstname'")
        if not 'lastname' in args:
            raise RuntimeError("Missing required argument 'lastname'")
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")

        return self.request('createUser', args)
 

    def deleteUser(self, args={}):
        '''
        Creates a user for an account

        args - A dictionary. The following are options for keys:
            id - Deletes a user
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteUser', args)
 

    def updateUser(self, args={}):
        '''
        Updates a user account

        args - A dictionary. The following are options for keys:
            id - User id
            email - email
            firstname - first name
            lastname - last name
            password - Hashed password (default is MD5). If you wish to use any other
               hasing algorithm, you would need to write a custom authentication adapter
            timezone - Specifies a timezone for this command. For more information on
               the timezone parameter, see Time Zone Format.
            userapikey - The API key for the user. Must be specified with userSecretKey
            username - Unique username
            usersecretkey - The secret key for the user. Must be specified with
               userApiKey
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateUser', args)
 

    def listUsers(self, args={}):
        '''
        Lists user accounts

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            accounttype - List users by account type. Valid types include admin,
               domain-admin, read-only-admin, or user.
            domainid - list only resources belonging to the domain specified
            id - List user by ID.
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            page - 
            pagesize - 
            state - List users by state of the user account.
            username - List user by the username
            page - Pagination
        '''

        return self.request('listUsers', args)
 

    def disableUser(self, args={}):
        '''
        Disables a user account

        args - A dictionary. The following are options for keys:
            id - Disables user by user ID.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('disableUser', args)
 

    def enableUser(self, args={}):
        '''
        Enables a user account

        args - A dictionary. The following are options for keys:
            id - Enables user by user ID.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('enableUser', args)
 

    def registerUserKeys(self, args={}):
        '''
        This command allows a user to register for the developer API, returning a secret
        key and an API key. This request is made through the integration API port, so it
        is a privileged command and must be made on behalf of a user. It is up to the
        implementer just how the username and password are entered, and then how that
        translates to an integration API request. Both secret key and API key should be
        returned to the user

        args - A dictionary. The following are options for keys:
            id - User id
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('registerUserKeys', args)
 

    def addVpnUser(self, args={}):
        '''
        Adds vpn users

        args - A dictionary. The following are options for keys:
            password - password for the username
            username - username for the vpn user
            account - an optional account for the vpn user. Must be used with domainId.
            domainid - an optional domainId for the vpn user. If the account parameter
               is used, domainId must also be used.
            projectid - add vpn user to the specific project
        '''
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")

        return self.request('addVpnUser', args)
 

    def removeVpnUser(self, args={}):
        '''
        Removes vpn user

        args - A dictionary. The following are options for keys:
            username - username for the vpn user
            account - an optional account for the vpn user. Must be used with domainId.
            domainid - an optional domainId for the vpn user. If the account parameter
               is used, domainId must also be used.
            projectid - remove vpn user from the project
        '''
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")

        return self.request('removeVpnUser', args)
 

    def listVpnUsers(self, args={}):
        '''
        Lists vpn users

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            id - the ID of the vpn user
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            page - 
            pagesize - 
            projectid - list firewall rules by project
            username - the username of the vpn user.
            page - Pagination
        '''

        return self.request('listVpnUsers', args)
 

    def createTemplate(self, args={}):
        '''
        Creates a template of a virtual machine. The virtual machine must be in a
        STOPPED state. A template created from this command is automatically designated
        as a private template visible to the account that created it.

        args - A dictionary. The following are options for keys:
            displaytext - the display text of the template. This is usually used for
               display purposes.
            name - the name of the template
            ostypeid - the ID of the OS Type that best represents the OS of this
               template.
            bits - 32 or 64 bit
            details - Template details in key/value pairs.
            isfeatured - true if this template is a featured template, false otherwise
            ispublic - true if this template is a public template, false otherwise
            passwordenabled - true if the template supports the password reset feature;
               default is false
            requireshvm - true if the template requres HVM, false otherwise
            snapshotid - the ID of the snapshot the template is being created from.
               Either this parameter, or volumeId has to be passed in
            templatetag - the tag for this template.
            url - Optional, only for baremetal hypervisor. The directory name where
               template stored on CIFS server
            virtualmachineid - Optional, VM ID. If this presents, it is going to create
               a baremetal template for VM this ID refers to. This is only for VM whose
               hypervisor type is BareMetal
            volumeid - the ID of the disk volume the template is being created from.
               Either this parameter, or snapshotId has to be passed in
        '''
        if not 'displaytext' in args:
            raise RuntimeError("Missing required argument 'displaytext'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'ostypeid' in args:
            raise RuntimeError("Missing required argument 'ostypeid'")

        return self.request('createTemplate', args)
 

    def registerTemplate(self, args={}):
        '''
        Registers an existing template into the Cloud.com cloud.

        args - A dictionary. The following are options for keys:
            displaytext - the display text of the template. This is usually used for
               display purposes.
            format - the format for the template. Possible values include QCOW2, RAW,
               and VHD.
            hypervisor - the target hypervisor for the template
            name - the name of the template
            ostypeid - the ID of the OS Type that best represents the OS of this
               template.
            url - the URL of where the template is hosted. Possible URL include http://
               and https://
            zoneid - the ID of the zone the template is to be hosted on
            account - an optional accountName. Must be used with domainId.
            bits - 32 or 64 bits support. 64 by default
            checksum - the MD5 checksum value of this template
            details - Template details in key/value pairs.
            domainid - an optional domainId. If the account parameter is used, domainId
               must also be used.
            isextractable - true if the template or its derivatives are extractable;
               default is false
            isfeatured - true if this template is a featured template, false otherwise
            ispublic - true if the template is available to all accounts; default is
               true
            passwordenabled - true if the template supports the password reset feature;
               default is false
            projectid - Register template for the project
            requireshvm - true if this template requires HVM
            sshkeyenabled - true if the template supports the sshkey upload feature;
               default is false
            templatetag - the tag for this template.
        '''
        if not 'displaytext' in args:
            raise RuntimeError("Missing required argument 'displaytext'")
        if not 'format' in args:
            raise RuntimeError("Missing required argument 'format'")
        if not 'hypervisor' in args:
            raise RuntimeError("Missing required argument 'hypervisor'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'ostypeid' in args:
            raise RuntimeError("Missing required argument 'ostypeid'")
        if not 'url' in args:
            raise RuntimeError("Missing required argument 'url'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('registerTemplate', args)
 

    def updateTemplate(self, args={}):
        '''
        Updates attributes of a template.

        args - A dictionary. The following are options for keys:
            id - the ID of the image file
            bootable - true if image is bootable, false otherwise
            displaytext - the display text of the image
            format - the format for the image
            name - the name of the image file
            ostypeid - the ID of the OS type that best represents the OS of this image.
            passwordenabled - true if the image supports the password reset feature;
               default is false
            sortkey - sort key of the template, integer
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateTemplate', args)
 

    def copyTemplate(self, args={}):
        '''
        Copies a template from one zone to another.

        args - A dictionary. The following are options for keys:
            id - Template ID.
            destzoneid - ID of the zone the template is being copied to.
            sourcezoneid - ID of the zone the template is currently hosted on.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'destzoneid' in args:
            raise RuntimeError("Missing required argument 'destzoneid'")
        if not 'sourcezoneid' in args:
            raise RuntimeError("Missing required argument 'sourcezoneid'")

        return self.request('copyTemplate', args)
 

    def deleteTemplate(self, args={}):
        '''
        Deletes a template from the system. All virtual machines using the deleted
        template will not be affected.

        args - A dictionary. The following are options for keys:
            id - the ID of the template
            zoneid - the ID of zone of the template
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteTemplate', args)
 

    def listTemplates(self, args={}):
        '''
        List all public, private, and privileged templates.

        args - A dictionary. The following are options for keys:
            templatefilter - possible values are "featured", "self", "self-executable",
               "executable", and "community".* featured-templates that are featured and are
               public* self-templates that have been registered/created by the owner*
               selfexecutable-templates that have been registered/created by the owner that can
               be used to deploy a new VM* executable-all templates that can be used to deploy
               a new VM* community-templates that are public.
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            hypervisor - the hypervisor for which to restrict the search
            id - the template ID
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            name - the template name
            page - 
            pagesize - 
            projectid - list firewall rules by project
            zoneid - list templates by zoneId
            page - Pagination
        '''
        if not 'templatefilter' in args:
            raise RuntimeError("Missing required argument 'templatefilter'")

        return self.request('listTemplates', args)
 

    def updateTemplatePermissions(self, args={}):
        '''
        Updates a template visibility permissions. A public template is visible to all
        accounts within the same domain. A private template is visible only to the owner
        of the template. A priviledged template is a private template with account
        permissions added. Only accounts specified under the template permissions are
        visible to them.

        args - A dictionary. The following are options for keys:
            id - the template ID
            accounts - a comma delimited list of accounts. If specified, "op" parameter
               has to be passed in.
            isextractable - true if the template/iso is extractable, false other wise.
               Can be set only by root admin
            isfeatured - true for featured template/iso, false otherwise
            ispublic - true for public template/iso, false for private templates/isos
            op - permission operator (add, remove, reset)
            projectids - a comma delimited list of projects. If specified, "op"
               parameter has to be passed in.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateTemplatePermissions', args)
 

    def listTemplatePermissions(self, args={}):
        '''
        List template visibility and all accounts that have permissions to view this
        template.

        args - A dictionary. The following are options for keys:
            id - the template ID
            page - Pagination
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('listTemplatePermissions', args)
 

    def extractTemplate(self, args={}):
        '''
        Extracts a template

        args - A dictionary. The following are options for keys:
            id - the ID of the template
            mode - the mode of extraction - HTTP_DOWNLOAD or FTP_UPLOAD
            url - the url to which the ISO would be extracted
            zoneid - the ID of the zone where the ISO is originally located
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'mode' in args:
            raise RuntimeError("Missing required argument 'mode'")

        return self.request('extractTemplate', args)
 

    def prepareTemplate(self, args={}):
        '''
        load template into primary storage

        args - A dictionary. The following are options for keys:
            templateid - template ID of the template to be prepared in primary
               storage(s).
            zoneid - zone ID of the template to be prepared in primary storage(s).
        '''
        if not 'templateid' in args:
            raise RuntimeError("Missing required argument 'templateid'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('prepareTemplate', args)
 

    def attachIso(self, args={}):
        '''
        Attaches an ISO to a virtual machine.

        args - A dictionary. The following are options for keys:
            id - the ID of the ISO file
            virtualmachineid - the ID of the virtual machine
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'virtualmachineid' in args:
            raise RuntimeError("Missing required argument 'virtualmachineid'")

        return self.request('attachIso', args)
 

    def detachIso(self, args={}):
        '''
        Detaches any ISO file (if any) currently attached to a virtual machine.

        args - A dictionary. The following are options for keys:
            virtualmachineid - The ID of the virtual machine
        '''
        if not 'virtualmachineid' in args:
            raise RuntimeError("Missing required argument 'virtualmachineid'")

        return self.request('detachIso', args)
 

    def listIsos(self, args={}):
        '''
        Lists all available ISO files.

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            bootable - true if the ISO is bootable, false otherwise
            domainid - list only resources belonging to the domain specified
            hypervisor - the hypervisor for which to restrict the search
            id - list all isos by id
            isofilter - possible values are "featured", "self",
               "self-executable","executable", and "community". * featured-ISOs that are
               featured and are publicself-ISOs that have been registered/created by the owner.
               * selfexecutable-ISOs that have been registered/created by the owner that can be
               used to deploy a new VM. * executable-all ISOs that can be used to deploy a new
               VM * community-ISOs that are public.
            ispublic - true if the ISO is publicly available to all users, false
               otherwise.
            isready - true if this ISO is ready to be deployed
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            name - list all isos by name
            page - 
            pagesize - 
            projectid - list firewall rules by project
            zoneid - the ID of the zone
            page - Pagination
        '''

        return self.request('listIsos', args)
 

    def registerIso(self, args={}):
        '''
        Registers an existing ISO into the Cloud.com Cloud.

        args - A dictionary. The following are options for keys:
            displaytext - the display text of the ISO. This is usually used for display
               purposes.
            name - the name of the ISO
            url - the URL to where the ISO is currently being hosted
            zoneid - the ID of the zone you wish to register the ISO to.
            account - an optional account name. Must be used with domainId.
            bootable - true if this ISO is bootable. If not passed explicitly its
               assumed to be true
            checksum - the MD5 checksum value of this ISO
            domainid - an optional domainId. If the account parameter is used, domainId
               must also be used.
            isextractable - true if the iso or its derivatives are extractable; default
               is false
            isfeatured - true if you want this ISO to be featured
            ispublic - true if you want to register the ISO to be publicly available to
               all users, false otherwise.
            ostypeid - the ID of the OS Type that best represents the OS of this ISO. If
               the iso is bootable this parameter needs to be passed
            projectid - Register iso for the project
        '''
        if not 'displaytext' in args:
            raise RuntimeError("Missing required argument 'displaytext'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'url' in args:
            raise RuntimeError("Missing required argument 'url'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('registerIso', args)
 

    def updateIso(self, args={}):
        '''
        Updates an ISO file.

        args - A dictionary. The following are options for keys:
            id - the ID of the image file
            bootable - true if image is bootable, false otherwise
            displaytext - the display text of the image
            format - the format for the image
            name - the name of the image file
            ostypeid - the ID of the OS type that best represents the OS of this image.
            passwordenabled - true if the image supports the password reset feature;
               default is false
            sortkey - sort key of the template, integer
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateIso', args)
 

    def deleteIso(self, args={}):
        '''
        Deletes an ISO file.

        args - A dictionary. The following are options for keys:
            id - the ID of the ISO file
            zoneid - the ID of the zone of the ISO file. If not specified, the ISO will
               be deleted from all the zones
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteIso', args)
 

    def copyIso(self, args={}):
        '''
        Copies a template from one zone to another.

        args - A dictionary. The following are options for keys:
            id - Template ID.
            destzoneid - ID of the zone the template is being copied to.
            sourcezoneid - ID of the zone the template is currently hosted on.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'destzoneid' in args:
            raise RuntimeError("Missing required argument 'destzoneid'")
        if not 'sourcezoneid' in args:
            raise RuntimeError("Missing required argument 'sourcezoneid'")

        return self.request('copyIso', args)
 

    def updateIsoPermissions(self, args={}):
        '''
        Updates iso permissions

        args - A dictionary. The following are options for keys:
            id - the template ID
            accounts - a comma delimited list of accounts. If specified, "op" parameter
               has to be passed in.
            isextractable - true if the template/iso is extractable, false other wise.
               Can be set only by root admin
            isfeatured - true for featured template/iso, false otherwise
            ispublic - true for public template/iso, false for private templates/isos
            op - permission operator (add, remove, reset)
            projectids - a comma delimited list of projects. If specified, "op"
               parameter has to be passed in.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateIsoPermissions', args)
 

    def listIsoPermissions(self, args={}):
        '''
        List template visibility and all accounts that have permissions to view this
        template.

        args - A dictionary. The following are options for keys:
            id - the template ID
            page - Pagination
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('listIsoPermissions', args)
 

    def extractIso(self, args={}):
        '''
        Extracts an ISO

        args - A dictionary. The following are options for keys:
            id - the ID of the ISO file
            mode - the mode of extraction - HTTP_DOWNLOAD or FTP_UPLOAD
            url - the url to which the ISO would be extracted
            zoneid - the ID of the zone where the ISO is originally located
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'mode' in args:
            raise RuntimeError("Missing required argument 'mode'")

        return self.request('extractIso', args)
 

    def listPortForwardingRules(self, args={}):
        '''
        Lists all port forwarding rules for an IP address.

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            id - Lists rule with the specified ID.
            ipaddressid - the id of IP address of the port forwarding services
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            page - 
            pagesize - 
            projectid - list firewall rules by project
            page - Pagination
        '''

        return self.request('listPortForwardingRules', args)
 

    def createPortForwardingRule(self, args={}):
        '''
        Creates a port forwarding rule

        args - A dictionary. The following are options for keys:
            ipaddressid - the IP address id of the port forwarding rule
            privateport - the starting port of port forwarding rule's private port
               range
            protocol - the protocol for the port fowarding rule. Valid values are TCP or
               UDP.
            publicport - the starting port of port forwarding rule's public port range
            virtualmachineid - the ID of the virtual machine for the port forwarding
               rule
            cidrlist - the cidr list to forward traffic from
            openfirewall - if true, firewall rule for source/end pubic port is
               automatically created; if false - firewall rule has to be created explicitely.
               Has value true by default
        '''
        if not 'ipaddressid' in args:
            raise RuntimeError("Missing required argument 'ipaddressid'")
        if not 'privateport' in args:
            raise RuntimeError("Missing required argument 'privateport'")
        if not 'protocol' in args:
            raise RuntimeError("Missing required argument 'protocol'")
        if not 'publicport' in args:
            raise RuntimeError("Missing required argument 'publicport'")
        if not 'virtualmachineid' in args:
            raise RuntimeError("Missing required argument 'virtualmachineid'")

        return self.request('createPortForwardingRule', args)
 

    def deletePortForwardingRule(self, args={}):
        '''
        Deletes a port forwarding rule

        args - A dictionary. The following are options for keys:
            id - the ID of the port forwarding rule
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deletePortForwardingRule', args)
 

    def createFirewallRule(self, args={}):
        '''
        Creates a firewall rule for a given ip address

        args - A dictionary. The following are options for keys:
            protocol - the protocol for the firewall rule. Valid values are
               TCP/UDP/ICMP.
            cidrlist - the cidr list to forward traffic from
            endport - the ending port of firewall rule
            icmpcode - error code for this icmp message
            icmptype - type of the icmp message being sent
            ipaddressid - the IP address id of the port forwarding rule
            startport - the starting port of firewall rule
            type - type of firewallrule: system/user
        '''
        if not 'protocol' in args:
            raise RuntimeError("Missing required argument 'protocol'")

        return self.request('createFirewallRule', args)
 

    def deleteFirewallRule(self, args={}):
        '''
        Deletes a firewall rule

        args - A dictionary. The following are options for keys:
            id - the ID of the firewall rule
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteFirewallRule', args)
 

    def listFirewallRules(self, args={}):
        '''
        Lists all firewall rules for an IP address.

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            id - Lists rule with the specified ID.
            ipaddressid - the id of IP address of the firwall services
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            page - 
            pagesize - 
            projectid - list firewall rules by project
            page - Pagination
        '''

        return self.request('listFirewallRules', args)
 

    def addSrxFirewall(self, args={}):
        '''
        Adds a SRX firewall device

        args - A dictionary. The following are options for keys:
            networkdevicetype - supports only JuniperSRXFirewall
            password - Credentials to reach SRX firewall device
            physicalnetworkid - the Physical Network ID
            url - URL of the SRX appliance.
            username - Credentials to reach SRX firewall device
        '''
        if not 'networkdevicetype' in args:
            raise RuntimeError("Missing required argument 'networkdevicetype'")
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")
        if not 'physicalnetworkid' in args:
            raise RuntimeError("Missing required argument 'physicalnetworkid'")
        if not 'url' in args:
            raise RuntimeError("Missing required argument 'url'")
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")

        return self.request('addSrxFirewall', args)
 

    def deleteSrxFirewall(self, args={}):
        '''
        delete a SRX firewall device

        args - A dictionary. The following are options for keys:
            fwdeviceid - srx firewall device ID
        '''
        if not 'fwdeviceid' in args:
            raise RuntimeError("Missing required argument 'fwdeviceid'")

        return self.request('deleteSrxFirewall', args)
 

    def configureSrxFirewall(self, args={}):
        '''
        Configures a SRX firewall device

        args - A dictionary. The following are options for keys:
            fwdeviceid - SRX firewall device ID
            fwdevicecapacity - capacity of the firewall device, Capacity will be
               interpreted as number of networks device can handle
        '''
        if not 'fwdeviceid' in args:
            raise RuntimeError("Missing required argument 'fwdeviceid'")

        return self.request('configureSrxFirewall', args)
 

    def listSrxFirewalls(self, args={}):
        '''
        lists SRX firewall devices in a physical network

        args - A dictionary. The following are options for keys:
            fwdeviceid - SRX firewall device ID
            keyword - List by keyword
            page - 
            pagesize - 
            physicalnetworkid - the Physical Network ID
            page - Pagination
        '''

        return self.request('listSrxFirewalls', args)
 

    def startRouter(self, args={}):
        '''
        Starts a router.

        args - A dictionary. The following are options for keys:
            id - the ID of the router
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('startRouter', args)
 

    def rebootRouter(self, args={}):
        '''
        Starts a router.

        args - A dictionary. The following are options for keys:
            id - the ID of the router
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('rebootRouter', args)
 

    def stopRouter(self, args={}):
        '''
        Stops a router.

        args - A dictionary. The following are options for keys:
            id - the ID of the router
            forced - Force stop the VM. The caller knows the VM is stopped.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('stopRouter', args)
 

    def destroyRouter(self, args={}):
        '''
        Destroys a router.

        args - A dictionary. The following are options for keys:
            id - the ID of the router
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('destroyRouter', args)
 

    def changeServiceForRouter(self, args={}):
        '''
        Upgrades domain router to a new service offering

        args - A dictionary. The following are options for keys:
            id - The ID of the router
            serviceofferingid - the service offering ID to apply to the domain router
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'serviceofferingid' in args:
            raise RuntimeError("Missing required argument 'serviceofferingid'")

        return self.request('changeServiceForRouter', args)
 

    def listRouters(self, args={}):
        '''
        List routers.

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            hostid - the host ID of the router
            id - the ID of the disk router
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            name - the name of the router
            networkid - list by network id
            page - 
            pagesize - 
            podid - the Pod ID of the router
            projectid - list firewall rules by project
            state - the state of the router
            zoneid - the Zone ID of the router
            page - Pagination
        '''

        return self.request('listRouters', args)
 

    def createVirtualRouterElement(self, args={}):
        '''
        Create a virtual router element.

        args - A dictionary. The following are options for keys:
            nspid - the network service provider ID of the virtual router element
        '''
        if not 'nspid' in args:
            raise RuntimeError("Missing required argument 'nspid'")

        return self.request('createVirtualRouterElement', args)
 

    def configureVirtualRouterElement(self, args={}):
        '''
        Configures a virtual router element.

        args - A dictionary. The following are options for keys:
            id - the ID of the virtual router provider
            enabled - Enabled/Disabled the service provider
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'enabled' in args:
            raise RuntimeError("Missing required argument 'enabled'")

        return self.request('configureVirtualRouterElement', args)
 

    def listVirtualRouterElements(self, args={}):
        '''
        Lists all available virtual router elements.

        args - A dictionary. The following are options for keys:
            enabled - list network offerings by enabled state
            id - list virtual router elements by id
            keyword - List by keyword
            nspid - list virtual router elements by network service provider id
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listVirtualRouterElements', args)
 

    def createProject(self, args={}):
        '''
        Creates a project

        args - A dictionary. The following are options for keys:
            displaytext - display text of the project
            name - name of the project
            account - account who will be Admin for the project
            domainid - domain ID of the account owning a project
        '''
        if not 'displaytext' in args:
            raise RuntimeError("Missing required argument 'displaytext'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('createProject', args)
 

    def deleteProject(self, args={}):
        '''
        Deletes a project

        args - A dictionary. The following are options for keys:
            id - id of the project to be deleted
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteProject', args)
 

    def updateProject(self, args={}):
        '''
        Updates a project

        args - A dictionary. The following are options for keys:
            id - id of the project to be modified
            account - new Admin account for the project
            displaytext - display text of the project
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateProject', args)
 

    def activateProject(self, args={}):
        '''
        Activates a project

        args - A dictionary. The following are options for keys:
            id - id of the project to be modified
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('activateProject', args)
 

    def suspendProject(self, args={}):
        '''
        Suspends a project

        args - A dictionary. The following are options for keys:
            id - id of the project to be suspended
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('suspendProject', args)
 

    def listProjects(self, args={}):
        '''
        Lists projects and provides detailed information for listed projects

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            displaytext - list projects by display text
            domainid - list only resources belonging to the domain specified
            id - list projects by project ID
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            name - list projects by name
            page - 
            pagesize - 
            state - list projects by state
            page - Pagination
        '''

        return self.request('listProjects', args)
 

    def listProjectInvitations(self, args={}):
        '''
        Lists projects and provides detailed information for listed projects

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            activeonly - if true, list only active invitations - having Pending state
               and ones that are not timed out yet
            domainid - list only resources belonging to the domain specified
            id - list invitations by id
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            page - 
            pagesize - 
            projectid - list by project id
            state - list invitations by state
            page - Pagination
        '''

        return self.request('listProjectInvitations', args)
 

    def updateProjectInvitation(self, args={}):
        '''
        Accepts or declines project invitation

        args - A dictionary. The following are options for keys:
            projectid - id of the project to join
            accept - if true, accept the invitation, decline if false. True by default
            account - account that is joining the project
            token - list invitations for specified account; this parameter has to be
               specified with domainId
        '''
        if not 'projectid' in args:
            raise RuntimeError("Missing required argument 'projectid'")

        return self.request('updateProjectInvitation', args)
 

    def deleteProjectInvitation(self, args={}):
        '''
        Accepts or declines project invitation

        args - A dictionary. The following are options for keys:
            id - id of the invitation
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteProjectInvitation', args)
 

    def addHost(self, args={}):
        '''
        Adds a new host.

        args - A dictionary. The following are options for keys:
            hypervisor - hypervisor type of the host
            password - the password for the host
            url - the host URL
            username - the username for the host
            zoneid - the Zone ID for the host
            allocationstate - Allocation state of this Host for allocation of new
               resources
            clusterid - the cluster ID for the host
            clustername - the cluster name for the host
            hosttags - list of tags to be added to the host
            podid - the Pod ID for the host
        '''
        if not 'hypervisor' in args:
            raise RuntimeError("Missing required argument 'hypervisor'")
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")
        if not 'url' in args:
            raise RuntimeError("Missing required argument 'url'")
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('addHost', args)
 

    def reconnectHost(self, args={}):
        '''
        Reconnects a host.

        args - A dictionary. The following are options for keys:
            id - the host ID
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('reconnectHost', args)
 

    def updateHost(self, args={}):
        '''
        Updates a host.

        args - A dictionary. The following are options for keys:
            id - the ID of the host to update
            allocationstate - Change resource state of host, valid values are [Enable,
               Disable]. Operation may failed if host in states not allowing Enable/Disable
            hosttags - list of tags to be added to the host
            oscategoryid - the id of Os category to update the host with
            url - the new uri for the secondary storage: nfs://host/path
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateHost', args)
 

    def deleteHost(self, args={}):
        '''
        Deletes a host.

        args - A dictionary. The following are options for keys:
            id - the host ID
            forced - Force delete the host. All HA enabled vms running on the host will
               be put to HA; HA disabled ones will be stopped
            forcedestroylocalstorage - Force destroy local storage on this host. All VMs
               created on this local storage will be destroyed
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteHost', args)
 

    def prepareHostForMaintenance(self, args={}):
        '''
        Prepares a host for maintenance.

        args - A dictionary. The following are options for keys:
            id - the host ID
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('prepareHostForMaintenance', args)
 

    def cancelHostMaintenance(self, args={}):
        '''
        Cancels host maintenance.

        args - A dictionary. The following are options for keys:
            id - the host ID
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('cancelHostMaintenance', args)
 

    def listHosts(self, args={}):
        '''
        Lists hosts.

        args - A dictionary. The following are options for keys:
            clusterid - lists hosts existing in particular cluster
            details - comma separated list of host details requested, value can be a
               list of [ min, all, capacity, events, stats]
            id - the id of the host
            keyword - List by keyword
            name - the name of the host
            page - 
            pagesize - 
            podid - the Pod ID for the host
            resourcestate - list hosts by resource state. Resource state represents
               current state determined by admin of host, valule can be one of [Enabled,
               Disabled, Unmanaged, PrepareForMaintenance, ErrorInMaintenance, Maintenance,
               Error]
            state - the state of the host
            type - the host type
            virtualmachineid - lists hosts in the same cluster as this VM and flag hosts
               with enough CPU/RAm to host this VM
            zoneid - the Zone ID for the host
            page - Pagination
        '''

        return self.request('listHosts', args)
 

    def addSecondaryStorage(self, args={}):
        '''
        Adds secondary storage.

        args - A dictionary. The following are options for keys:
            url - the URL for the secondary storage
            zoneid - the Zone ID for the secondary storage
        '''
        if not 'url' in args:
            raise RuntimeError("Missing required argument 'url'")

        return self.request('addSecondaryStorage', args)
 

    def updateHostPassword(self, args={}):
        '''
        Update password of a host/pool on management server.

        args - A dictionary. The following are options for keys:
            password - the new password for the host/cluster
            username - the username for the host/cluster
            clusterid - the cluster ID
            hostid - the host ID
        '''
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")

        return self.request('updateHostPassword', args)
 

    def createAccount(self, args={}):
        '''
        Creates an account

        args - A dictionary. The following are options for keys:
            accounttype - Type of the account.  Specify 0 for user, 1 for root admin,
               and 2 for domain admin
            email - email
            firstname - firstname
            lastname - lastname
            password - Hashed password (Default is MD5). If you wish to use any other
               hashing algorithm, you would need to write a custom authentication adapter See
               Docs section.
            username - Unique username.
            account - Creates the user under the specified account. If no account is
               specified, the username will be used as the account name.
            accountdetails - details for account used to store specific parameters
            domainid - Creates the user under the specified domain.
            networkdomain - Network domain for the account's networks
            timezone - Specifies a timezone for this command. For more information on
               the timezone parameter, see Time Zone Format.
        '''
        if not 'accounttype' in args:
            raise RuntimeError("Missing required argument 'accounttype'")
        if not 'email' in args:
            raise RuntimeError("Missing required argument 'email'")
        if not 'firstname' in args:
            raise RuntimeError("Missing required argument 'firstname'")
        if not 'lastname' in args:
            raise RuntimeError("Missing required argument 'lastname'")
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")

        return self.request('createAccount', args)
 

    def deleteAccount(self, args={}):
        '''
        Deletes a account, and all users associated with this account

        args - A dictionary. The following are options for keys:
            id - Account id
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteAccount', args)
 

    def updateAccount(self, args={}):
        '''
        Updates account information for the authenticated user

        args - A dictionary. The following are options for keys:
            newname - new name for the account
            account - the current account name
            accountdetails - details for account used to store specific parameters
            domainid - the ID of the domain where the account exists
            id - Account id
            networkdomain - Network domain for the account's networks; empty string will
               update domainName with NULL value
        '''
        if not 'newname' in args:
            raise RuntimeError("Missing required argument 'newname'")

        return self.request('updateAccount', args)
 

    def disableAccount(self, args={}):
        '''
        Disables an account

        args - A dictionary. The following are options for keys:
            lock - If true, only lock the account; else disable the account
            account - Disables specified account.
            domainid - Disables specified account in this domain.
            id - Account id
        '''
        if not 'lock' in args:
            raise RuntimeError("Missing required argument 'lock'")

        return self.request('disableAccount', args)
 

    def enableAccount(self, args={}):
        '''
        Enables an account

        args - A dictionary. The following are options for keys:
            account - Enables specified account.
            domainid - Enables specified account in this domain.
            id - Account id
        '''

        return self.request('enableAccount', args)
 

    def listAccounts(self, args={}):
        '''
        Lists accounts and provides detailed account information for listed accounts

        args - A dictionary. The following are options for keys:
            accounttype - list accounts by account type. Valid account types are 1
               (admin), 2 (domain-admin), and 0 (user).
            domainid - list only resources belonging to the domain specified
            id - list account by account ID
            iscleanuprequired - list accounts by cleanuprequred attribute (values are
               true or false)
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            name - list account by account name
            page - 
            pagesize - 
            state - list accounts by state. Valid states are enabled, disabled, and
               locked.
            page - Pagination
        '''

        return self.request('listAccounts', args)
 

    def addAccountToProject(self, args={}):
        '''
        Adds acoount to a project

        args - A dictionary. The following are options for keys:
            projectid - id of the project to add the account to
            account - name of the account to be added to the project
            email - email to which invitation to the project is going to be sent
        '''
        if not 'projectid' in args:
            raise RuntimeError("Missing required argument 'projectid'")

        return self.request('addAccountToProject', args)
 

    def deleteAccountFromProject(self, args={}):
        '''
        Deletes account from the project

        args - A dictionary. The following are options for keys:
            account - name of the account to be removed from the project
            projectid - id of the project to remove the account from
        '''
        if not 'account' in args:
            raise RuntimeError("Missing required argument 'account'")
        if not 'projectid' in args:
            raise RuntimeError("Missing required argument 'projectid'")

        return self.request('deleteAccountFromProject', args)
 

    def listProjectAccounts(self, args={}):
        '''
        Lists project's accounts

        args - A dictionary. The following are options for keys:
            projectid - id of the project
            account - list accounts of the project by account name
            keyword - List by keyword
            page - 
            pagesize - 
            role - list accounts of the project by role
            page - Pagination
        '''
        if not 'projectid' in args:
            raise RuntimeError("Missing required argument 'projectid'")

        return self.request('listProjectAccounts', args)
 

    def listStoragePools(self, args={}):
        '''
        Lists storage pools.

        args - A dictionary. The following are options for keys:
            clusterid - list storage pools belongig to the specific cluster
            id - the ID of the storage pool
            ipaddress - the IP address for the storage pool
            keyword - List by keyword
            name - the name of the storage pool
            page - 
            pagesize - 
            path - the storage pool path
            podid - the Pod ID for the storage pool
            zoneid - the Zone ID for the storage pool
            page - Pagination
        '''

        return self.request('listStoragePools', args)
 

    def createStoragePool(self, args={}):
        '''
        Creates a storage pool.

        args - A dictionary. The following are options for keys:
            name - the name for the storage pool
            url - the URL of the storage pool
            zoneid - the Zone ID for the storage pool
            clusterid - the cluster ID for the storage pool
            details - the details for the storage pool
            podid - the Pod ID for the storage pool
            tags - the tags for the storage pool
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'url' in args:
            raise RuntimeError("Missing required argument 'url'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('createStoragePool', args)
 

    def updateStoragePool(self, args={}):
        '''
        Updates a storage pool.

        args - A dictionary. The following are options for keys:
            id - the Id of the storage pool
            tags - comma-separated list of tags for the storage pool
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateStoragePool', args)
 

    def deleteStoragePool(self, args={}):
        '''
        Deletes a storage pool.

        args - A dictionary. The following are options for keys:
            id - Storage pool id
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteStoragePool', args)
 

    def createPool(self, args={}):
        '''
        Create a pool

        args - A dictionary. The following are options for keys:
            algorithm - algorithm.
            name - pool name.
        '''
        if not 'algorithm' in args:
            raise RuntimeError("Missing required argument 'algorithm'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('createPool', args)
 

    def deletePool(self, args={}):
        '''
        Delete a pool

        args - A dictionary. The following are options for keys:
            poolname - pool name.
        '''
        if not 'poolname' in args:
            raise RuntimeError("Missing required argument 'poolname'")

        return self.request('deletePool', args)
 

    def modifyPool(self, args={}):
        '''
        Modify pool

        args - A dictionary. The following are options for keys:
            algorithm - algorithm.
            poolname - pool name.
        '''
        if not 'algorithm' in args:
            raise RuntimeError("Missing required argument 'algorithm'")
        if not 'poolname' in args:
            raise RuntimeError("Missing required argument 'poolname'")

        return self.request('modifyPool', args)
 

    def listPools(self, args={}):
        '''
        List Pool

        args - A dictionary. The following are options for keys:
            page - Pagination
        '''

        return self.request('listPools', args)
 

    def createSecurityGroup(self, args={}):
        '''
        Creates a security group

        args - A dictionary. The following are options for keys:
            name - name of the security group
            account - an optional account for the security group. Must be used with
               domainId.
            description - the description of the security group
            domainid - an optional domainId for the security group. If the account
               parameter is used, domainId must also be used.
            projectid - Deploy vm for the project
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('createSecurityGroup', args)
 

    def deleteSecurityGroup(self, args={}):
        '''
        Deletes security group

        args - A dictionary. The following are options for keys:
            account - the account of the security group. Must be specified with domain
               ID
            domainid - the domain ID of account owning the security group
            id - The ID of the security group. Mutually exclusive with name parameter
            name - The ID of the security group. Mutually exclusive with id parameter
            projectid - the project of the security group
        '''

        return self.request('deleteSecurityGroup', args)
 

    def authorizeSecurityGroupIngress(self, args={}):
        '''
        Authorizes a particular ingress rule for this security group

        args - A dictionary. The following are options for keys:
            account - an optional account for the security group. Must be used with
               domainId.
            cidrlist - the cidr list associated
            domainid - an optional domainId for the security group. If the account
               parameter is used, domainId must also be used.
            endport - end port for this ingress rule
            icmpcode - error code for this icmp message
            icmptype - type of the icmp message being sent
            projectid - an optional project of the security group
            protocol - TCP is default. UDP is the other supported protocol
            securitygroupid - The ID of the security group. Mutually exclusive with
               securityGroupName parameter
            securitygroupname - The name of the security group. Mutually exclusive with
               securityGroupName parameter
            startport - start port for this ingress rule
            usersecuritygrouplist - user to security group mapping
        '''

        return self.request('authorizeSecurityGroupIngress', args)
 

    def revokeSecurityGroupIngress(self, args={}):
        '''
        Deletes a particular ingress rule from this security group

        args - A dictionary. The following are options for keys:
            id - The ID of the ingress rule
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('revokeSecurityGroupIngress', args)
 

    def authorizeSecurityGroupEgress(self, args={}):
        '''
        Authorizes a particular egress rule for this security group

        args - A dictionary. The following are options for keys:
            account - an optional account for the security group. Must be used with
               domainId.
            cidrlist - the cidr list associated
            domainid - an optional domainId for the security group. If the account
               parameter is used, domainId must also be used.
            endport - end port for this egress rule
            icmpcode - error code for this icmp message
            icmptype - type of the icmp message being sent
            projectid - an optional project of the security group
            protocol - TCP is default. UDP is the other supported protocol
            securitygroupid - The ID of the security group. Mutually exclusive with
               securityGroupName parameter
            securitygroupname - The name of the security group. Mutually exclusive with
               securityGroupName parameter
            startport - start port for this egress rule
            usersecuritygrouplist - user to security group mapping
        '''

        return self.request('authorizeSecurityGroupEgress', args)
 

    def revokeSecurityGroupEgress(self, args={}):
        '''
        Deletes a particular egress rule from this security group

        args - A dictionary. The following are options for keys:
            id - The ID of the egress rule
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('revokeSecurityGroupEgress', args)
 

    def listSecurityGroups(self, args={}):
        '''
        Lists security groups

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            id - list the security group by the id provided
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            page - 
            pagesize - 
            projectid - list firewall rules by project
            securitygroupname - lists security groups by name
            virtualmachineid - lists security groups by virtual machine id
            page - Pagination
        '''

        return self.request('listSecurityGroups', args)
 

    def startSystemVm(self, args={}):
        '''
        Starts a system virtual machine.

        args - A dictionary. The following are options for keys:
            id - The ID of the system virtual machine
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('startSystemVm', args)
 

    def rebootSystemVm(self, args={}):
        '''
        Reboots a system VM.

        args - A dictionary. The following are options for keys:
            id - The ID of the system virtual machine
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('rebootSystemVm', args)
 

    def stopSystemVm(self, args={}):
        '''
        Stops a system VM.

        args - A dictionary. The following are options for keys:
            id - The ID of the system virtual machine
            forced - Force stop the VM.  The caller knows the VM is stopped.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('stopSystemVm', args)
 

    def destroySystemVm(self, args={}):
        '''
        Destroyes a system virtual machine.

        args - A dictionary. The following are options for keys:
            id - The ID of the system virtual machine
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('destroySystemVm', args)
 

    def listSystemVms(self, args={}):
        '''
        List system virtual machines.

        args - A dictionary. The following are options for keys:
            hostid - the host ID of the system VM
            id - the ID of the system VM
            keyword - List by keyword
            name - the name of the system VM
            page - 
            pagesize - 
            podid - the Pod ID of the system VM
            state - the state of the system VM
            systemvmtype - the system VM type. Possible types are "consoleproxy" and
               "secondarystoragevm".
            zoneid - the Zone ID of the system VM
            page - Pagination
        '''

        return self.request('listSystemVms', args)
 

    def migrateSystemVm(self, args={}):
        '''
        Attempts Migration of a system virtual machine to the host specified.

        args - A dictionary. The following are options for keys:
            hostid - destination Host ID to migrate VM to
            virtualmachineid - the ID of the virtual machine
        '''
        if not 'hostid' in args:
            raise RuntimeError("Missing required argument 'hostid'")
        if not 'virtualmachineid' in args:
            raise RuntimeError("Missing required argument 'virtualmachineid'")

        return self.request('migrateSystemVm', args)
 

    def createSnapshot(self, args={}):
        '''
        Creates an instant snapshot of a volume.

        args - A dictionary. The following are options for keys:
            volumeid - The ID of the disk volume
            account - The account of the snapshot. The account parameter must be used
               with the domainId parameter.
            domainid - The domain ID of the snapshot. If used with the account
               parameter, specifies a domain for the account associated with the disk volume.
            policyid - policy id of the snapshot, if this is null, then use
               MANUAL_POLICY.
        '''
        if not 'volumeid' in args:
            raise RuntimeError("Missing required argument 'volumeid'")

        return self.request('createSnapshot', args)
 

    def listSnapshots(self, args={}):
        '''
        Lists all available snapshots for the account.

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            id - lists snapshot by snapshot ID
            intervaltype - valid values are HOURLY, DAILY, WEEKLY, and MONTHLY.
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            name - lists snapshot by snapshot name
            page - 
            pagesize - 
            projectid - list firewall rules by project
            snapshottype - valid values are MANUAL or RECURRING.
            volumeid - the ID of the disk volume
            page - Pagination
        '''

        return self.request('listSnapshots', args)
 

    def deleteSnapshot(self, args={}):
        '''
        Deletes a snapshot of a disk volume.

        args - A dictionary. The following are options for keys:
            id - The ID of the snapshot
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteSnapshot', args)
 

    def createSnapshotPolicy(self, args={}):
        '''
        Creates a snapshot policy for the account.

        args - A dictionary. The following are options for keys:
            intervaltype - valid values are HOURLY, DAILY, WEEKLY, and MONTHLY
            maxsnaps - maximum number of snapshots to retain
            schedule - time the snapshot is scheduled to be taken. Format is:* if
               HOURLY, MM* if DAILY, MM:HH* if WEEKLY, MM:HH:DD (1-7)* if MONTHLY, MM:HH:DD
               (1-28)
            timezone - Specifies a timezone for this command. For more information on
               the timezone parameter, see Time Zone Format.
            volumeid - the ID of the disk volume
        '''
        if not 'intervaltype' in args:
            raise RuntimeError("Missing required argument 'intervaltype'")
        if not 'maxsnaps' in args:
            raise RuntimeError("Missing required argument 'maxsnaps'")
        if not 'schedule' in args:
            raise RuntimeError("Missing required argument 'schedule'")
        if not 'timezone' in args:
            raise RuntimeError("Missing required argument 'timezone'")
        if not 'volumeid' in args:
            raise RuntimeError("Missing required argument 'volumeid'")

        return self.request('createSnapshotPolicy', args)
 

    def deleteSnapshotPolicies(self, args={}):
        '''
        Deletes snapshot policies for the account.

        args - A dictionary. The following are options for keys:
            id - the Id of the snapshot policy
            ids - list of snapshots policy IDs separated by comma
        '''

        return self.request('deleteSnapshotPolicies', args)
 

    def listSnapshotPolicies(self, args={}):
        '''
        Lists snapshot policies.

        args - A dictionary. The following are options for keys:
            volumeid - the ID of the disk volume
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''
        if not 'volumeid' in args:
            raise RuntimeError("Missing required argument 'volumeid'")

        return self.request('listSnapshotPolicies', args)
 

    def createLunOnFiler(self, args={}):
        '''
        Create a LUN from a pool

        args - A dictionary. The following are options for keys:
            name - pool name.
            size - LUN size.
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'size' in args:
            raise RuntimeError("Missing required argument 'size'")

        return self.request('createLunOnFiler', args)
 

    def destroyLunOnFiler(self, args={}):
        '''
        Destroy a LUN

        args - A dictionary. The following are options for keys:
            path - LUN path.
        '''
        if not 'path' in args:
            raise RuntimeError("Missing required argument 'path'")

        return self.request('destroyLunOnFiler', args)
 

    def listLunsOnFiler(self, args={}):
        '''
        List LUN

        args - A dictionary. The following are options for keys:
            poolname - pool name.
            page - Pagination
        '''
        if not 'poolname' in args:
            raise RuntimeError("Missing required argument 'poolname'")

        return self.request('listLunsOnFiler', args)
 

    def associateLun(self, args={}):
        '''
        Associate a LUN with a guest IQN

        args - A dictionary. The following are options for keys:
            iqn - Guest IQN to which the LUN associate.
            name - LUN name.
        '''
        if not 'iqn' in args:
            raise RuntimeError("Missing required argument 'iqn'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('associateLun', args)
 

    def dissociateLun(self, args={}):
        '''
        Dissociate a LUN

        args - A dictionary. The following are options for keys:
            iqn - Guest IQN.
            path - LUN path.
        '''
        if not 'iqn' in args:
            raise RuntimeError("Missing required argument 'iqn'")
        if not 'path' in args:
            raise RuntimeError("Missing required argument 'path'")

        return self.request('dissociateLun', args)
 

    def enableStaticNat(self, args={}):
        '''
        Enables static nat for given ip address

        args - A dictionary. The following are options for keys:
            ipaddressid - the public IP address id for which static nat feature is being
               enabled
            virtualmachineid - the ID of the virtual machine for enabling static nat
               feature
        '''
        if not 'ipaddressid' in args:
            raise RuntimeError("Missing required argument 'ipaddressid'")
        if not 'virtualmachineid' in args:
            raise RuntimeError("Missing required argument 'virtualmachineid'")

        return self.request('enableStaticNat', args)
 

    def createIpForwardingRule(self, args={}):
        '''
        Creates an ip forwarding rule

        args - A dictionary. The following are options for keys:
            ipaddressid - the public IP address id of the forwarding rule, already
               associated via associateIp
            protocol - the protocol for the rule. Valid values are TCP or UDP.
            startport - the start port for the rule
            cidrlist - the cidr list to forward traffic from
            endport - the end port for the rule
            openfirewall - if true, firewall rule for source/end pubic port is
               automatically created; if false - firewall rule has to be created explicitely.
               Has value true by default
        '''
        if not 'ipaddressid' in args:
            raise RuntimeError("Missing required argument 'ipaddressid'")
        if not 'protocol' in args:
            raise RuntimeError("Missing required argument 'protocol'")
        if not 'startport' in args:
            raise RuntimeError("Missing required argument 'startport'")

        return self.request('createIpForwardingRule', args)
 

    def deleteIpForwardingRule(self, args={}):
        '''
        Deletes an ip forwarding rule

        args - A dictionary. The following are options for keys:
            id - the id of the forwarding rule
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteIpForwardingRule', args)
 

    def listIpForwardingRules(self, args={}):
        '''
        List the ip forwarding rules

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            id - Lists rule with the specified ID.
            ipaddressid - list the rule belonging to this public ip address
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            page - 
            pagesize - 
            projectid - list firewall rules by project
            virtualmachineid - Lists all rules applied to the specified Vm.
            page - Pagination
        '''

        return self.request('listIpForwardingRules', args)
 

    def disableStaticNat(self, args={}):
        '''
        Disables static rule for given ip address

        args - A dictionary. The following are options for keys:
            ipaddressid - the public IP address id for which static nat feature is being
               disableed
        '''
        if not 'ipaddressid' in args:
            raise RuntimeError("Missing required argument 'ipaddressid'")

        return self.request('disableStaticNat', args)
 

    def createDomain(self, args={}):
        '''
        Creates a domain

        args - A dictionary. The following are options for keys:
            name - creates domain with this name
            networkdomain - Network domain for networks in the domain
            parentdomainid - assigns new domain a parent domain by domain ID of the
               parent.  If no parent domain is specied, the ROOT domain is assumed.
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('createDomain', args)
 

    def updateDomain(self, args={}):
        '''
        Updates a domain with a new name

        args - A dictionary. The following are options for keys:
            id - ID of domain to update
            name - updates domain with this name
            networkdomain - Network domain for the domain's networks; empty string will
               update domainName with NULL value
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateDomain', args)
 

    def deleteDomain(self, args={}):
        '''
        Deletes a specified domain

        args - A dictionary. The following are options for keys:
            id - ID of domain to delete
            cleanup - true if all domain resources (child domains, accounts) have to be
               cleaned up, false otherwise
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteDomain', args)
 

    def listDomains(self, args={}):
        '''
        Lists domains and provides detailed information for listed domains

        args - A dictionary. The following are options for keys:
            id - List domain by domain ID.
            keyword - List by keyword
            level - List domains by domain level.
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            name - List domain by domain name.
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listDomains', args)
 

    def listDomainChildren(self, args={}):
        '''
        Lists all children domains belonging to a specified domain

        args - A dictionary. The following are options for keys:
            id - list children domain by parent domain ID.
            isrecursive - to return the entire tree, use the value "true". To return the
               first level children, use the value "false".
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            name - list children domains by name
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listDomainChildren', args)
 

    def createZone(self, args={}):
        '''
        Creates a Zone.

        args - A dictionary. The following are options for keys:
            dns1 - the first DNS for the Zone
            internaldns1 - the first internal DNS for the Zone
            name - the name of the Zone
            networktype - network type of the zone, can be Basic or Advanced
            allocationstate - Allocation state of this Zone for allocation of new
               resources
            dns2 - the second DNS for the Zone
            domain - Network domain name for the networks in the zone
            domainid - the ID of the containing domain, null for public zones
            guestcidraddress - the guest CIDR address for the Zone
            internaldns2 - the second internal DNS for the Zone
            securitygroupenabled - true if network is security group enabled, false
               otherwise
        '''
        if not 'dns1' in args:
            raise RuntimeError("Missing required argument 'dns1'")
        if not 'internaldns1' in args:
            raise RuntimeError("Missing required argument 'internaldns1'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'networktype' in args:
            raise RuntimeError("Missing required argument 'networktype'")

        return self.request('createZone', args)
 

    def updateZone(self, args={}):
        '''
        Updates a Zone.

        args - A dictionary. The following are options for keys:
            id - the ID of the Zone
            allocationstate - Allocation state of this cluster for allocation of new
               resources
            details - the details for the Zone
            dhcpprovider - the dhcp Provider for the Zone
            dns1 - the first DNS for the Zone
            dns2 - the second DNS for the Zone
            dnssearchorder - the dns search order list
            domain - Network domain name for the networks in the zone; empty string will
               update domain with NULL value
            guestcidraddress - the guest CIDR address for the Zone
            internaldns1 - the first internal DNS for the Zone
            internaldns2 - the second internal DNS for the Zone
            ispublic - updates a private zone to public if set, but not vice-versa
            name - the name of the Zone
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateZone', args)
 

    def deleteZone(self, args={}):
        '''
        Deletes a Zone.

        args - A dictionary. The following are options for keys:
            id - the ID of the Zone
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteZone', args)
 

    def listZones(self, args={}):
        '''
        Lists zones

        args - A dictionary. The following are options for keys:
            available - true if you want to retrieve all available Zones. False if you
               only want to return the Zones from which you have at least one VM. Default is
               false.
            domainid - the ID of the domain associated with the zone
            id - the ID of the zone
            keyword - List by keyword
            page - 
            pagesize - 
            showcapacities - flag to display the capacity of the zones
            page - Pagination
        '''

        return self.request('listZones', args)
 

    def createInstanceGroup(self, args={}):
        '''
        Creates a vm group

        args - A dictionary. The following are options for keys:
            name - the name of the instance group
            account - the account of the instance group. The account parameter must be
               used with the domainId parameter.
            domainid - the domain ID of account owning the instance group
            projectid - The project of the instance group
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('createInstanceGroup', args)
 

    def deleteInstanceGroup(self, args={}):
        '''
        Deletes a vm group

        args - A dictionary. The following are options for keys:
            id - the ID of the instance group
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteInstanceGroup', args)
 

    def updateInstanceGroup(self, args={}):
        '''
        Updates a vm group

        args - A dictionary. The following are options for keys:
            id - Instance group ID
            name - new instance group name
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateInstanceGroup', args)
 

    def listInstanceGroups(self, args={}):
        '''
        Lists vm groups

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            id - list instance groups by ID
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            name - list instance groups by name
            page - 
            pagesize - 
            projectid - list firewall rules by project
            page - Pagination
        '''

        return self.request('listInstanceGroups', args)
 

    def createServiceOffering(self, args={}):
        '''
        Creates a service offering.

        args - A dictionary. The following are options for keys:
            cpunumber - the CPU number of the service offering
            cpuspeed - the CPU speed of the service offering in MHz.
            displaytext - the display text of the service offering
            memory - the total memory of the service offering in MB
            name - the name of the service offering
            domainid - the ID of the containing domain, null for public offerings
            hosttags - the host tag for this service offering.
            issystem - is this a system vm offering
            limitcpuuse - restrict the CPU usage to committed service offering
            networkrate - data transfer rate in megabits per second allowed. Supported
               only for non-System offering and system offerings having "domainrouter"
               systemvmtype
            offerha - the HA for the service offering
            storagetype - the storage type of the service offering. Values are local and
               shared.
            systemvmtype - the system VM type. Possible types are "domainrouter",
               "consoleproxy" and "secondarystoragevm".
            tags - the tags for this service offering.
        '''
        if not 'cpunumber' in args:
            raise RuntimeError("Missing required argument 'cpunumber'")
        if not 'cpuspeed' in args:
            raise RuntimeError("Missing required argument 'cpuspeed'")
        if not 'displaytext' in args:
            raise RuntimeError("Missing required argument 'displaytext'")
        if not 'memory' in args:
            raise RuntimeError("Missing required argument 'memory'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('createServiceOffering', args)
 

    def deleteServiceOffering(self, args={}):
        '''
        Deletes a service offering.

        args - A dictionary. The following are options for keys:
            id - the ID of the service offering
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteServiceOffering', args)
 

    def updateServiceOffering(self, args={}):
        '''
        Updates a service offering.

        args - A dictionary. The following are options for keys:
            id - the ID of the service offering to be updated
            displaytext - the display text of the service offering to be updated
            name - the name of the service offering to be updated
            sortkey - sort key of the service offering, integer
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateServiceOffering', args)
 

    def listServiceOfferings(self, args={}):
        '''
        Lists all available service offerings.

        args - A dictionary. The following are options for keys:
            domainid - the ID of the domain associated with the service offering
            id - ID of the service offering
            issystem - is this a system vm offering
            keyword - List by keyword
            name - name of the service offering
            page - 
            pagesize - 
            systemvmtype - the system VM type. Possible types are "consoleproxy",
               "secondarystoragevm" or "domainrouter".
            virtualmachineid - the ID of the virtual machine. Pass this in if you want
               to see the available service offering that a virtual machine can be changed to.
            page - Pagination
        '''

        return self.request('listServiceOfferings', args)
 

    def createPod(self, args={}):
        '''
        Creates a new Pod.

        args - A dictionary. The following are options for keys:
            gateway - the gateway for the Pod
            name - the name of the Pod
            netmask - the netmask for the Pod
            startip - the starting IP address for the Pod
            zoneid - the Zone ID in which the Pod will be created
            allocationstate - Allocation state of this Pod for allocation of new
               resources
            endip - the ending IP address for the Pod
        '''
        if not 'gateway' in args:
            raise RuntimeError("Missing required argument 'gateway'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'netmask' in args:
            raise RuntimeError("Missing required argument 'netmask'")
        if not 'startip' in args:
            raise RuntimeError("Missing required argument 'startip'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('createPod', args)
 

    def updatePod(self, args={}):
        '''
        Updates a Pod.

        args - A dictionary. The following are options for keys:
            id - the ID of the Pod
            allocationstate - Allocation state of this cluster for allocation of new
               resources
            endip - the ending IP address for the Pod
            gateway - the gateway for the Pod
            name - the name of the Pod
            netmask - the netmask of the Pod
            startip - the starting IP address for the Pod
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updatePod', args)
 

    def deletePod(self, args={}):
        '''
        Deletes a Pod.

        args - A dictionary. The following are options for keys:
            id - the ID of the Pod
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deletePod', args)
 

    def listPods(self, args={}):
        '''
        Lists all Pods.

        args - A dictionary. The following are options for keys:
            allocationstate - list pods by allocation state
            id - list Pods by ID
            keyword - List by keyword
            name - list Pods by name
            page - 
            pagesize - 
            showcapacities - flag to display the capacity of the pods
            zoneid - list Pods by Zone ID
            page - Pagination
        '''

        return self.request('listPods', args)
 

    def createDiskOffering(self, args={}):
        '''
        Creates a disk offering.

        args - A dictionary. The following are options for keys:
            displaytext - alternate display text of the disk offering
            name - name of the disk offering
            customized - whether disk offering is custom or not
            disksize - size of the disk offering in GB
            domainid - the ID of the containing domain, null for public offerings
            tags - tags for the disk offering
        '''
        if not 'displaytext' in args:
            raise RuntimeError("Missing required argument 'displaytext'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('createDiskOffering', args)
 

    def updateDiskOffering(self, args={}):
        '''
        Updates a disk offering.

        args - A dictionary. The following are options for keys:
            id - ID of the disk offering
            displaytext - updates alternate display text of the disk offering with this
               value
            name - updates name of the disk offering with this value
            sortkey - sort key of the disk offering, integer
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateDiskOffering', args)
 

    def deleteDiskOffering(self, args={}):
        '''
        Updates a disk offering.

        args - A dictionary. The following are options for keys:
            id - ID of the disk offering
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteDiskOffering', args)
 

    def listDiskOfferings(self, args={}):
        '''
        Lists all available disk offerings.

        args - A dictionary. The following are options for keys:
            domainid - the ID of the domain of the disk offering.
            id - ID of the disk offering
            keyword - List by keyword
            name - name of the disk offering
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listDiskOfferings', args)
 

    def addCluster(self, args={}):
        '''
        Adds a new cluster

        args - A dictionary. The following are options for keys:
            clustername - the cluster name
            clustertype - type of the cluster: CloudManaged, ExternalManaged
            hypervisor - hypervisor type of the cluster:
               XenServer,KVM,VMware,Hyperv,BareMetal,Simulator
            zoneid - the Zone ID for the cluster
            allocationstate - Allocation state of this cluster for allocation of new
               resources
            password - the password for the host
            podid - the Pod ID for the host
            url - the URL
            username - the username for the cluster
        '''
        if not 'clustername' in args:
            raise RuntimeError("Missing required argument 'clustername'")
        if not 'clustertype' in args:
            raise RuntimeError("Missing required argument 'clustertype'")
        if not 'hypervisor' in args:
            raise RuntimeError("Missing required argument 'hypervisor'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('addCluster', args)
 

    def deleteCluster(self, args={}):
        '''
        Deletes a cluster.

        args - A dictionary. The following are options for keys:
            id - the cluster ID
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteCluster', args)
 

    def updateCluster(self, args={}):
        '''
        Updates an existing cluster

        args - A dictionary. The following are options for keys:
            id - the ID of the Cluster
            allocationstate - Allocation state of this cluster for allocation of new
               resources
            clustername - the cluster name
            clustertype - hypervisor type of the cluster
            hypervisor - hypervisor type of the cluster
            managedstate - whether this cluster is managed by cloudstack
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateCluster', args)
 

    def listClusters(self, args={}):
        '''
        Lists clusters.

        args - A dictionary. The following are options for keys:
            allocationstate - lists clusters by allocation state
            clustertype - lists clusters by cluster type
            hypervisor - lists clusters by hypervisor type
            id - lists clusters by the cluster ID
            keyword - List by keyword
            managedstate - whether this cluster is managed by cloudstack
            name - lists clusters by the cluster name
            page - 
            pagesize - 
            podid - lists clusters by Pod ID
            showcapacities - flag to display the capacity of the clusters
            zoneid - lists clusters by Zone ID
            page - Pagination
        '''

        return self.request('listClusters', args)
 

    def createRemoteAccessVpn(self, args={}):
        '''
        Creates a l2tp/ipsec remote access vpn

        args - A dictionary. The following are options for keys:
            publicipid - public ip address id of the vpn server
            account - an optional account for the VPN. Must be used with domainId.
            domainid - an optional domainId for the VPN. If the account parameter is
               used, domainId must also be used.
            iprange - the range of ip addresses to allocate to vpn clients. The first ip
               in the range will be taken by the vpn server
            openfirewall - if true, firewall rule for source/end pubic port is
               automatically created; if false - firewall rule has to be created explicitely.
               Has value true by default
        '''
        if not 'publicipid' in args:
            raise RuntimeError("Missing required argument 'publicipid'")

        return self.request('createRemoteAccessVpn', args)
 

    def deleteRemoteAccessVpn(self, args={}):
        '''
        Destroys a l2tp/ipsec remote access vpn

        args - A dictionary. The following are options for keys:
            publicipid - public ip address id of the vpn server
        '''
        if not 'publicipid' in args:
            raise RuntimeError("Missing required argument 'publicipid'")

        return self.request('deleteRemoteAccessVpn', args)
 

    def listRemoteAccessVpns(self, args={}):
        '''
        Lists remote access vpns

        args - A dictionary. The following are options for keys:
            publicipid - public ip address id of the vpn server
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            page - 
            pagesize - 
            projectid - list firewall rules by project
            page - Pagination
        '''
        if not 'publicipid' in args:
            raise RuntimeError("Missing required argument 'publicipid'")

        return self.request('listRemoteAccessVpns', args)
 

    def createVlanIpRange(self, args={}):
        '''
        Creates a VLAN IP range.

        args - A dictionary. The following are options for keys:
            startip - the beginning IP address in the VLAN IP range
            account - account who will own the VLAN. If VLAN is Zone wide, this
               parameter should be ommited
            domainid - domain ID of the account owning a VLAN
            endip - the ending IP address in the VLAN IP range
            forvirtualnetwork - true if VLAN is of Virtual type, false if Direct
            gateway - the gateway of the VLAN IP range
            netmask - the netmask of the VLAN IP range
            networkid - the network id
            physicalnetworkid - the physical network id
            podid - optional parameter. Have to be specified for Direct Untagged vlan
               only.
            projectid - project who will own the VLAN. If VLAN is Zone wide, this
               parameter should be ommited
            vlan - the ID or VID of the VLAN. Default is an "untagged" VLAN.
            zoneid - the Zone ID of the VLAN IP range
        '''
        if not 'startip' in args:
            raise RuntimeError("Missing required argument 'startip'")

        return self.request('createVlanIpRange', args)
 

    def deleteVlanIpRange(self, args={}):
        '''
        Creates a VLAN IP range.

        args - A dictionary. The following are options for keys:
            id - the id of the VLAN IP range
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteVlanIpRange', args)
 

    def listVlanIpRanges(self, args={}):
        '''
        Lists all VLAN IP ranges.

        args - A dictionary. The following are options for keys:
            account - the account with which the VLAN IP range is associated. Must be
               used with the domainId parameter.
            domainid - the domain ID with which the VLAN IP range is associated.  If
               used with the account parameter, returns all VLAN IP ranges for that account in
               the specified domain.
            forvirtualnetwork - true if VLAN is of Virtual type, false if Direct
            id - the ID of the VLAN IP range
            keyword - List by keyword
            networkid - network id of the VLAN IP range
            page - 
            pagesize - 
            physicalnetworkid - physical network id of the VLAN IP range
            podid - the Pod ID of the VLAN IP range
            projectid - project who will own the VLAN
            vlan - the ID or VID of the VLAN. Default is an "untagged" VLAN.
            zoneid - the Zone ID of the VLAN IP range
            page - Pagination
        '''

        return self.request('listVlanIpRanges', args)
 

    def createSSHKeyPair(self, args={}):
        '''
        Create a new keypair and returns the private key

        args - A dictionary. The following are options for keys:
            name - Name of the keypair
            account - an optional account for the ssh key. Must be used with domainId.
            domainid - an optional domainId for the ssh key. If the account parameter is
               used, domainId must also be used.
            projectid - an optional project for the ssh key
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('createSSHKeyPair', args)
 

    def deleteSSHKeyPair(self, args={}):
        '''
        Deletes a keypair by name

        args - A dictionary. The following are options for keys:
            name - Name of the keypair
            account - the account associated with the keypair. Must be used with the
               domainId parameter.
            domainid - the domain ID associated with the keypair
            projectid - the project associated with keypair
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('deleteSSHKeyPair', args)
 

    def listSSHKeyPairs(self, args={}):
        '''
        List registered keypairs

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            fingerprint - A public key fingerprint to look for
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            name - A key pair name to look for
            page - 
            pagesize - 
            projectid - list firewall rules by project
            page - Pagination
        '''

        return self.request('listSSHKeyPairs', args)
 

    def updateResourceLimit(self, args={}):
        '''
        Updates resource limits for an account or domain.

        args - A dictionary. The following are options for keys:
            resourcetype - Type of resource to update. Values are 0, 1, 2, 3, and 4. 0 -
               Instance. Number of instances a user can create. 1 - IP. Number of public IP
               addresses a user can own. 2 - Volume. Number of disk volumes a user can create.3
               - Snapshot. Number of snapshots a user can create.4 - Template. Number of
               templates that a user can register/create.
            account - Update resource for a specified account. Must be used with the
               domainId parameter.
            domainid - Update resource limits for all accounts in specified domain. If
               used with the account parameter, updates resource limits for a specified account
               in specified domain.
            max - Maximum resource limit.
            projectid - Update resource limits for project
        '''
        if not 'resourcetype' in args:
            raise RuntimeError("Missing required argument 'resourcetype'")

        return self.request('updateResourceLimit', args)
 

    def updateResourceCount(self, args={}):
        '''
        Recalculate and update resource count for an account or domain.

        args - A dictionary. The following are options for keys:
            domainid - If account parameter specified then updates resource counts for a
               specified account in this domain else update resource counts for all accounts &
               child domains in specified domain.
            account - Update resource count for a specified account. Must be used with
               the domainId parameter.
            projectid - Update resource limits for project
            resourcetype - Type of resource to update. If specifies valid values are 0,
               1, 2, 3, and 4. If not specified will update all resource counts0 - Instance.
               Number of instances a user can create. 1 - IP. Number of public IP addresses a
               user can own. 2 - Volume. Number of disk volumes a user can create.3 - Snapshot.
               Number of snapshots a user can create.4 - Template. Number of templates that a
               user can register/create.
        '''
        if not 'domainid' in args:
            raise RuntimeError("Missing required argument 'domainid'")

        return self.request('updateResourceCount', args)
 

    def listResourceLimits(self, args={}):
        '''
        Lists resource limits.

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            id - Lists resource limits by ID.
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            page - 
            pagesize - 
            projectid - list firewall rules by project
            resourcetype - Type of resource to update. Values are 0, 1, 2, 3, and 4. 0 -
               Instance. Number of instances a user can create. 1 - IP. Number of public IP
               addresses a user can own. 2 - Volume. Number of disk volumes a user can create.3
               - Snapshot. Number of snapshots a user can create.4 - Template. Number of
               templates that a user can register/create.
            page - Pagination
        '''

        return self.request('listResourceLimits', args)
 

    def listHypervisors(self, args={}):
        '''
        List hypervisors

        args - A dictionary. The following are options for keys:
            zoneid - the zone id for listing hypervisors.
            page - Pagination
        '''

        return self.request('listHypervisors', args)
 

    def updateHypervisorCapabilities(self, args={}):
        '''
        Updates a hypervisor capabilities.

        args - A dictionary. The following are options for keys:
            id - ID of the hypervisor capability
            maxguestslimit - the max number of Guest VMs per host for this hypervisor.
            securitygroupenabled - set true to enable security group for this
               hypervisor.
        '''

        return self.request('updateHypervisorCapabilities', args)
 

    def listHypervisorCapabilities(self, args={}):
        '''
        Lists all hypervisor capabilities.

        args - A dictionary. The following are options for keys:
            hypervisor - the hypervisor for which to restrict the search
            id - ID of the hypervisor capability
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listHypervisorCapabilities', args)
 

    def addExternalLoadBalancer(self, args={}):
        '''
        Adds F5 external load balancer appliance.

        args - A dictionary. The following are options for keys:
            password - Password of the external load balancer appliance.
            url - URL of the external load balancer appliance.
            username - Username of the external load balancer appliance.
            zoneid - Zone in which to add the external load balancer appliance.
        '''
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")
        if not 'url' in args:
            raise RuntimeError("Missing required argument 'url'")
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('addExternalLoadBalancer', args)
 

    def deleteExternalLoadBalancer(self, args={}):
        '''
        Deletes a F5 external load balancer appliance added in a zone.

        args - A dictionary. The following are options for keys:
            id - Id of the external loadbalancer appliance.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteExternalLoadBalancer', args)
 

    def listExternalLoadBalancers(self, args={}):
        '''
        Lists F5 external load balancer appliances added in a zone.

        args - A dictionary. The following are options for keys:
            keyword - List by keyword
            page - 
            pagesize - 
            zoneid - zone Id
            page - Pagination
        '''

        return self.request('listExternalLoadBalancers', args)
 

    def addExternalFirewall(self, args={}):
        '''
        Adds an external firewall appliance

        args - A dictionary. The following are options for keys:
            password - Password of the external firewall appliance.
            url - URL of the external firewall appliance.
            username - Username of the external firewall appliance.
            zoneid - Zone in which to add the external firewall appliance.
        '''
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")
        if not 'url' in args:
            raise RuntimeError("Missing required argument 'url'")
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('addExternalFirewall', args)
 

    def deleteExternalFirewall(self, args={}):
        '''
        Deletes an external firewall appliance.

        args - A dictionary. The following are options for keys:
            id - Id of the external firewall appliance.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteExternalFirewall', args)
 

    def listExternalFirewalls(self, args={}):
        '''
        List external firewall appliances.

        args - A dictionary. The following are options for keys:
            zoneid - zone Id
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('listExternalFirewalls', args)
 

    def updateConfiguration(self, args={}):
        '''
        Updates a configuration.

        args - A dictionary. The following are options for keys:
            name - the name of the configuration
            value - the value of the configuration
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('updateConfiguration', args)
 

    def listConfigurations(self, args={}):
        '''
        Lists all configurations.

        args - A dictionary. The following are options for keys:
            category - lists configurations by category
            keyword - List by keyword
            name - lists configuration by name
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listConfigurations', args)
 

    def listCapabilities(self, args={}):
        '''
        Lists capabilities

        args - A dictionary. The following are options for keys:
            page - Pagination
        '''

        return self.request('listCapabilities', args)
 

    def associateIpAddress(self, args={}):
        '''
        Acquires and associates a public IP to an account.

        args - A dictionary. The following are options for keys:
            account - the account to associate with this IP address
            domainid - the ID of the domain to associate with this IP address
            networkid - The network this ip address should be associated to.
            projectid - Deploy vm for the project
            zoneid - the ID of the availability zone you want to acquire an public IP
               address from
        '''

        return self.request('associateIpAddress', args)
 

    def disassociateIpAddress(self, args={}):
        '''
        Disassociates an ip address from the account.

        args - A dictionary. The following are options for keys:
            id - the id of the public ip address to disassociate
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('disassociateIpAddress', args)
 

    def listPublicIpAddresses(self, args={}):
        '''
        Lists all public ip addresses

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            allocatedonly - limits search results to allocated public IP addresses
            associatednetworkid - lists all public IP addresses associated to the
               network specified
            domainid - list only resources belonging to the domain specified
            forloadbalancing - list only ips used for load balancing
            forvirtualnetwork - the virtual network for the IP address
            id - lists ip address by id
            ipaddress - lists the specified IP address
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            issourcenat - list only source nat ip addresses
            isstaticnat - list only static nat ip addresses
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            page - 
            pagesize - 
            physicalnetworkid - lists all public IP addresses by physical network id
            projectid - list firewall rules by project
            vlanid - lists all public IP addresses by VLAN ID
            zoneid - lists all public IP addresses by Zone ID
            page - Pagination
        '''

        return self.request('listPublicIpAddresses', args)
 

    def addSwift(self, args={}):
        '''
        Adds Swift.

        args - A dictionary. The following are options for keys:
            url - the URL for swift
            account - the account for swift
            key - key for the user for swift
            username - the username for swift
        '''
        if not 'url' in args:
            raise RuntimeError("Missing required argument 'url'")

        return self.request('addSwift', args)
 

    def listSwifts(self, args={}):
        '''
        List Swift.

        args - A dictionary. The following are options for keys:
            id - the id of the swift
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listSwifts', args)
 

    def enableStorageMaintenance(self, args={}):
        '''
        Puts storage pool into maintenance state

        args - A dictionary. The following are options for keys:
            id - Primary storage ID
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('enableStorageMaintenance', args)
 

    def cancelStorageMaintenance(self, args={}):
        '''
        Cancels maintenance for primary storage

        args - A dictionary. The following are options for keys:
            id - the primary storage ID
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('cancelStorageMaintenance', args)
 

    def listOsTypes(self, args={}):
        '''
        Lists all supported OS types for this cloud.

        args - A dictionary. The following are options for keys:
            id - list by Os type Id
            keyword - List by keyword
            oscategoryid - list by Os Category id
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listOsTypes', args)
 

    def listOsCategories(self, args={}):
        '''
        Lists all supported OS categories for this cloud.

        args - A dictionary. The following are options for keys:
            id - list Os category by id
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listOsCategories', args)
 

    def listEvents(self, args={}):
        '''
        A command to list events.

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            duration - the duration of the event
            enddate - the end date range of the list you want to retrieve (use format
               "yyyy-MM-dd" or the new format "yyyy-MM-dd HH:mm:ss")
            entrytime - the time the event was entered
            id - the ID of the event
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            level - the event level (INFO, WARN, ERROR)
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            page - 
            pagesize - 
            projectid - list firewall rules by project
            startdate - the start date range of the list you want to retrieve (use
               format "yyyy-MM-dd" or the new format "yyyy-MM-dd HH:mm:ss")
            type - the event type (see event types)
            page - Pagination
        '''

        return self.request('listEvents', args)
 

    def listEventTypes(self, args={}):
        '''
        List Event Types

        args - A dictionary. The following are options for keys:
            page - Pagination
        '''

        return self.request('listEventTypes', args)
 

    def queryAsyncJobResult(self, args={}):
        '''
        Retrieves the current status of asynchronous job.

        args - A dictionary. The following are options for keys:
            jobid - the ID of the asychronous job
        '''
        if not 'jobid' in args:
            raise RuntimeError("Missing required argument 'jobid'")

        return self.request('queryAsyncJobResult', args)
 

    def listAsyncJobs(self, args={}):
        '''
        Lists all pending asynchronous jobs for the account.

        args - A dictionary. The following are options for keys:
            account - List resources by account. Must be used with the domainId
               parameter.
            domainid - list only resources belonging to the domain specified
            isrecursive - defaults to false, but if true, lists all resources from the
               parent specified by the domainId till leaves.
            keyword - List by keyword
            listall - If set to false, list only resources belonging to the command's
               caller; if set to true - list resources that the caller is authorized to see.
               Default value is false
            page - 
            pagesize - 
            startdate - the start date of the async job
            page - Pagination
        '''

        return self.request('listAsyncJobs', args)
 

    def listCapacity(self, args={}):
        '''
        Lists all the system wide capacities.

        args - A dictionary. The following are options for keys:
            clusterid - lists capacity by the Cluster ID
            fetchlatest - recalculate capacities and fetch the latest
            keyword - List by keyword
            page - 
            pagesize - 
            podid - lists capacity by the Pod ID
            sortby - Sort the results. Available values: Usage
            type - lists capacity by type* CAPACITY_TYPE_MEMORY = 0* CAPACITY_TYPE_CPU =
               1* CAPACITY_TYPE_STORAGE = 2* CAPACITY_TYPE_STORAGE_ALLOCATED = 3*
               CAPACITY_TYPE_VIRTUAL_NETWORK_PUBLIC_IP = 4* CAPACITY_TYPE_PRIVATE_IP = 5*
               CAPACITY_TYPE_SECONDARY_STORAGE = 6* CAPACITY_TYPE_VLAN = 7*
               CAPACITY_TYPE_DIRECT_ATTACHED_PUBLIC_IP = 8* CAPACITY_TYPE_LOCAL_STORAGE = 9.
            zoneid - lists capacity by the Zone ID
            page - Pagination
        '''

        return self.request('listCapacity', args)
 

    def registerSSHKeyPair(self, args={}):
        '''
        Register a public key in a keypair under a certain name

        args - A dictionary. The following are options for keys:
            name - Name of the keypair
            publickey - Public key material of the keypair
            account - an optional account for the ssh key. Must be used with domainId.
            domainid - an optional domainId for the ssh key. If the account parameter is
               used, domainId must also be used.
            projectid - an optional project for the ssh key
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'publickey' in args:
            raise RuntimeError("Missing required argument 'publickey'")

        return self.request('registerSSHKeyPair', args)
 

    def logout(self, args={}):
        '''
        Logs out the user

        args - A dictionary. The following are options for keys:
        '''

        return self.request('logout', args)
 

    def login(self, args={}):
        '''
        Logs a user into the CloudStack. A successful login attempt will generate a
        JSESSIONID cookie value that can be passed in subsequent Query command calls
        until the "logout" command has been issued or the session has expired.

        args - A dictionary. The following are options for keys:
            username - Username
            password - Hashed password (Default is MD5). If you wish to use any other
               hashing algorithm, you would need to write a custom authentication adapter See
               Docs section.
            domain - path of the domain that the user belongs to. Example:
               domain=/com/cloud/internal.  If no domain is passed in, the ROOT domain is
               assumed.
            domainId - id of the domain that the user belongs to. If both domain and
               domainId are passed in, "domainId" parameter takes precendence
        '''
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")

        return self.request('login', args)
 

    def ldapConfig(self, args={}):
        '''
        Configure the LDAP context for this site.

        args - A dictionary. The following are options for keys:
            hostname - Hostname or ip address of the ldap server eg: my.ldap.com
            queryfilter - You specify a query filter here, which narrows down the users,
               who can be part of this domain.
            searchbase - The search base defines the starting point for the search in
               the directory tree Example:  dc=cloud,dc=com.
            binddn - Specify the distinguished name of a user with the search permission
               on the directory.
            bindpass - Enter the password.
            port - Specify the LDAP port if required, default is 389.
            ssl - Check Use SSL if the external LDAP server is configured for LDAP over
               SSL.
            truststore - Enter the path to trust certificates store.
            truststorepass - Enter the password for trust store.
        '''
        if not 'hostname' in args:
            raise RuntimeError("Missing required argument 'hostname'")
        if not 'queryfilter' in args:
            raise RuntimeError("Missing required argument 'queryfilter'")
        if not 'searchbase' in args:
            raise RuntimeError("Missing required argument 'searchbase'")

        return self.request('ldapConfig', args)
 

    def getCloudIdentifier(self, args={}):
        '''
        Retrieves a cloud identifier.

        args - A dictionary. The following are options for keys:
            userid - the user ID for the cloud identifier
        '''
        if not 'userid' in args:
            raise RuntimeError("Missing required argument 'userid'")

        return self.request('getCloudIdentifier', args)
 

    def uploadCustomCertificate(self, args={}):
        '''
        Uploads custom certificate

        args - A dictionary. The following are options for keys:
            certificate - the custom cert to be uploaded
            domainsuffix - DNS domain suffix that the certificate is granted for
            id - the custom cert id in the chain
            name - the alias of the certificate
            privatekey - the private key for the certificate
        '''
        if not 'certificate' in args:
            raise RuntimeError("Missing required argument 'certificate'")
        if not 'domainsuffix' in args:
            raise RuntimeError("Missing required argument 'domainsuffix'")

        return self.request('uploadCustomCertificate', args)
 

    def listAlerts(self, args={}):
        '''
        Lists all alerts.

        args - A dictionary. The following are options for keys:
            id - the ID of the alert
            keyword - List by keyword
            page - 
            pagesize - 
            type - list by alert type
            page - Pagination
        '''

        return self.request('listAlerts', args)
 

