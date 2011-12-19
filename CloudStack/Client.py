from BaseClient import BaseClient

class Client(BaseClient):
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
            account - account. Must be used with the domainId parameter.
            domainid - the domain ID. If used with the account parameter, lists virtual
               machines for the specified account in this domain.
            forvirtualnetwork - list by network type; true if need to list vms using
               Virtual Network, false otherwise
            groupid - the group ID
            hostid - the host ID
            hypervisor - the target hypervisor for the template
            id - the ID of the virtual machine
            isrecursive - Must be used with domainId parameter. Defaults to false, but
               if true, lists all vms from the parent specified by the domain id till leaves.
            keyword - List by keyword
            name - name of the virtual machine
            networkid - list by network id
            page - 
            pagesize - 
            podid - the pod ID
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
        Attempts Migration of a virtual machine to the host specified.

        args - A dictionary. The following are options for keys:
            hostid - destination Host ID to migrate VM to
            virtualmachineid - the ID of the virtual machine
        '''
        if not 'hostid' in args:
            raise RuntimeError("Missing required argument 'hostid'")
        if not 'virtualmachineid' in args:
            raise RuntimeError("Missing required argument 'virtualmachineid'")

        return self.request('migrateVirtualMachine', args)
 

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
            domainid - an optional domainId. If the account parameter is used, domainId
               must also be used.
            isextractable - true if the template or its derivatives are extractable;
               default is false
            isfeatured - true if this template is a featured template, false otherwise
            ispublic - true if the template is available to all accounts; default is
               true
            passwordenabled - true if the template supports the password reset feature;
               default is false
            requireshvm - true if this template requires HVM
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
            account - list template by account. Must be used with the domainId
               parameter.
            domainid - list all templates in specified domain. If used with the account
               parameter, lists all templates for an account in the specified domain.
            hypervisor - the hypervisor for which to restrict the search
            id - the template ID
            keyword - List by keyword
            name - the template name
            page - 
            pagesize - 
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
            account - List template visibility and permissions for the specified
               account. Must be used with the domainId parameter.
            domainid - List template visibility and permissions by domain. If used with
               the account parameter, specifies in which domain the specified account exists.
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
            zoneid - the ID of the zone where the ISO is originally located
            url - the url to which the ISO would be extracted
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'mode' in args:
            raise RuntimeError("Missing required argument 'mode'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

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
            account - the account of the ISO file. Must be used with the domainId
               parameter.
            bootable - true if the ISO is bootable, false otherwise
            domainid - lists all available ISO files by ID of a domain. If used with the
               account parameter, lists all available ISO files for the account in the ID of a
               domain.
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
            keyword - List by keyword
            name - list all isos by name
            page - 
            pagesize - 
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
            bootable - true if this ISO is bootable
            domainid - an optional domainId. If the account parameter is used, domainId
               must also be used.
            isextractable - true if the iso or its derivatives are extractable; default
               is false
            isfeatured - true if you want this ISO to be featured
            ispublic - true if you want to register the ISO to be publicly available to
               all users, false otherwise.
            ostypeid - the ID of the OS Type that best represents the OS of this ISO
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
            account - List template visibility and permissions for the specified
               account. Must be used with the domainId parameter.
            domainid - List template visibility and permissions by domain. If used with
               the account parameter, specifies in which domain the specified account exists.
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
            zoneid - the ID of the zone where the ISO is originally located
            url - the url to which the ISO would be extracted
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")
        if not 'mode' in args:
            raise RuntimeError("Missing required argument 'mode'")
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

        return self.request('extractIso', args)
 

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
            account - the account associated with the disk volume. Must be used with the
               domainId parameter.
            domainid - Lists all disk volumes for the specified domain ID. If used with
               the account parameter, returns all disk volumes for an account in the specified
               domain ID.
            hostid - list volumes on specified host
            id - the ID of the disk volume
            isrecursive - defaults to false, but if true, lists all volumes from the
               parent specified by the domain id till leaves.
            keyword - List by keyword
            name - the name of the disk volume
            page - 
            pagesize - 
            podid - the pod id the disk volume belongs to
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
            allocationstate - Allocation state of this Host for allocation of new
               resources
            hosttags - list of tags to be added to the host
            oscategoryid - the id of Os category to update the host with
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
            allocationstate - list hosts by allocation state
            clusterid - lists hosts existing in particular cluster
            id - the id of the host
            keyword - List by keyword
            name - the name of the host
            page - 
            pagesize - 
            podid - the Pod ID for the host
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
            password - the password for the host/cluster
            username - the username for the host/cluster
            clusterid - the cluster ID for the host
            hostid - the host ID
        '''
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")

        return self.request('updateHostPassword', args)
 

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
            zoneid - lists clusters by Zone ID
            page - Pagination
        '''

        return self.request('listClusters', args)
 

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
            account - the current account name
            domainid - the ID of the domain where the account exists
            newname - new name for the account
            networkdomain - Network domain for the account's networks
        '''
        if not 'account' in args:
            raise RuntimeError("Missing required argument 'account'")
        if not 'domainid' in args:
            raise RuntimeError("Missing required argument 'domainid'")
        if not 'newname' in args:
            raise RuntimeError("Missing required argument 'newname'")

        return self.request('updateAccount', args)
 

    def disableAccount(self, args={}):
        '''
        Disables an account

        args - A dictionary. The following are options for keys:
            account - Disables specified account.
            domainid - Disables specified account in this domain.
            lock - If true, only lock the account; else disable the account
        '''
        if not 'account' in args:
            raise RuntimeError("Missing required argument 'account'")
        if not 'domainid' in args:
            raise RuntimeError("Missing required argument 'domainid'")
        if not 'lock' in args:
            raise RuntimeError("Missing required argument 'lock'")

        return self.request('disableAccount', args)
 

    def enableAccount(self, args={}):
        '''
        Enables an account

        args - A dictionary. The following are options for keys:
            account - Enables specified account.
            domainid - Enables specified account in this domain.
        '''
        if not 'account' in args:
            raise RuntimeError("Missing required argument 'account'")
        if not 'domainid' in args:
            raise RuntimeError("Missing required argument 'domainid'")

        return self.request('enableAccount', args)
 

    def listAccounts(self, args={}):
        '''
        Lists accounts and provides detailed account information for listed accounts

        args - A dictionary. The following are options for keys:
            accounttype - list accounts by account type. Valid account types are 1
               (admin), 2 (domain-admin), and 0 (user).
            domainid - list all accounts in specified domain. If used with the name
               parameter, retrieves account information for the account with specified name in
               specified domain.
            id - list account by account ID
            iscleanuprequired - list accounts by cleanuprequred attribute (values are
               true or false)
            isrecursive - defaults to false, but if true, lists all accounts from the
               parent specified by the domain id till leaves.
            keyword - List by keyword
            name - list account by account name
            page - 
            pagesize - 
            state - list accounts by state. Valid states are enabled, disabled, and
               locked.
            page - Pagination
        '''

        return self.request('listAccounts', args)
 

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
            account - lists snapshot belongig to the specified account. Must be used
               with the domainId parameter.
            domainid - the domain ID. If used with the account parameter, lists
               snapshots for the specified account in this domain.
            id - lists snapshot by snapshot ID
            intervaltype - valid values are HOURLY, DAILY, WEEKLY, and MONTHLY.
            isrecursive - defaults to false, but if true, lists all snapshots from the
               parent specified by the domain id till leaves.
            keyword - List by keyword
            name - lists snapshot by snapshot name
            page - 
            pagesize - 
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
            id - the Id of the snapshot
            ids - list of snapshots IDs separated by comma
        '''

        return self.request('deleteSnapshotPolicies', args)
 

    def listSnapshotPolicies(self, args={}):
        '''
        Lists snapshot policies.

        args - A dictionary. The following are options for keys:
            volumeid - the ID of the disk volume
            account - lists snapshot policies for the specified account. Must be used
               with domainid parameter.
            domainid - the domain ID. If used with the account parameter, lists snapshot
               policies for the specified account in this domain.
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''
        if not 'volumeid' in args:
            raise RuntimeError("Missing required argument 'volumeid'")

        return self.request('listSnapshotPolicies', args)
 

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
            account - List user by account. Must be used with the domainId parameter.
            accounttype - List users by account type. Valid types include admin,
               domain-admin, read-only-admin, or user.
            domainid - List all users in a domain. If used with the account parameter,
               lists an account in a specific domain.
            id - List user by ID.
            keyword - List by keyword
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
            networkdomain - Network domain for the domain's networks
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
            name - list children domains by name
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listDomainChildren', args)
 

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
            podid - optional parameter. Have to be specified for Direct Untagged vlan
               only.
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
            podid - the Pod ID of the VLAN IP range
            vlan - the ID or VID of the VLAN. Default is an "untagged" VLAN.
            zoneid - the Zone ID of the VLAN IP range
            page - Pagination
        '''

        return self.request('listVlanIpRanges', args)
 

    def associateIpAddress(self, args={}):
        '''
        Acquires and associates a public IP to an account.

        args - A dictionary. The following are options for keys:
            zoneid - the ID of the availability zone you want to acquire an public IP
               address from
            account - the account to associate with this IP address
            domainid - the ID of the domain to associate with this IP address
            networkid - The network this ip address should be associated to.
        '''
        if not 'zoneid' in args:
            raise RuntimeError("Missing required argument 'zoneid'")

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
            account - lists all public IP addresses by account. Must be used with the
               domainId parameter.
            allocatedonly - limits search results to allocated public IP addresses
            domainid - lists all public IP addresses by domain ID. If used with the
               account parameter, lists all public IP addresses by account for specified
               domain.
            forloadbalancing - list only ips used for load balancing
            forvirtualnetwork - the virtual network for the IP address
            id - lists ip address by id
            ipaddress - lists the specified IP address
            keyword - List by keyword
            page - 
            pagesize - 
            vlanid - lists all public IP addresses by VLAN ID
            zoneid - lists all public IP addresses by Zone ID
            page - Pagination
        '''

        return self.request('listPublicIpAddresses', args)
 

    def listPortForwardingRules(self, args={}):
        '''
        Lists all port forwarding rules for an IP address.

        args - A dictionary. The following are options for keys:
            account - account. Must be used with the domainId parameter.
            domainid - the domain ID. If used with the account parameter, lists port
               forwarding rules for the specified account in this domain.
            id - Lists rule with the specified ID.
            ipaddressid - the id of IP address of the port forwarding services
            keyword - List by keyword
            page - 
            pagesize - 
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
            privateendport - the ending port of port forwarding rule's private port
               range
            publicendport - the ending port of port forwarding rule's private port
               range
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
            ipaddressid - the IP address id of the port forwarding rule
            protocol - the protocol for the firewall rule. Valid values are
               TCP/UDP/ICMP.
            cidrlist - the cidr list to forward traffic from
            endport - the ending port of firewall rule
            icmpcode - error code for this icmp message
            icmptype - type of the icmp message being sent
            startport - the starting port of firewall rule
        '''
        if not 'ipaddressid' in args:
            raise RuntimeError("Missing required argument 'ipaddressid'")
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
            account - account. Must be used with the domainId parameter.
            domainid - the domain ID. If used with the account parameter, lists firewall
               rules for the specified account in this domain.
            id - Lists rule with the specified ID.
            ipaddressid - the id of IP address of the firwall services
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listFirewallRules', args)
 

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
            account - the account associated with the ip forwarding rule. Must be used
               with the domainId parameter.
            domainid - Lists all rules for this id. If used with the account parameter,
               returns all rules for an account in the specified domain ID.
            id - Lists rule with the specified ID.
            ipaddressid - list the rule belonging to this public ip address
            keyword - List by keyword
            page - 
            pagesize - 
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
            openfirewall - if true, firewall rule for source/end pubic port is
               automatically created; if false - firewall rule has to be created explicitely.
               Has value true by default
            publicipid - public ip address id from where the network traffic will be
               load balanced from
            zoneid - public ip address id from where the network traffic will be load
               balanced from
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
 

    def listLoadBalancerRules(self, args={}):
        '''
        Lists load balancer rules.

        args - A dictionary. The following are options for keys:
            account - the account of the load balancer rule. Must be used with the
               domainId parameter.
            domainid - the domain ID of the load balancer rule. If used with the account
               parameter, lists load balancer rules for the account in the specified domain.
            id - the ID of the load balancer rule
            keyword - List by keyword
            name - the name of the load balancer rule
            page - 
            pagesize - 
            publicipid - the public IP address id of the load balancer rule
            virtualmachineid - the ID of the virtual machine of the load balancer rule
            zoneid - the availability zone ID
            page - Pagination
        '''

        return self.request('listLoadBalancerRules', args)
 

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
            account - the name of the account associated with the router. Must be used
               with the domainId parameter.
            domainid - the domain ID associated with the router. If used with the
               account parameter, lists all routers associated with an account in the specified
               domain.
            hostid - the host ID of the router
            id - the ID of the disk router
            keyword - List by keyword
            name - the name of the router
            networkid - list by network id
            page - 
            pagesize - 
            podid - the Pod ID of the router
            state - the state of the router
            zoneid - the Zone ID of the router
            page - Pagination
        '''

        return self.request('listRouters', args)
 

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
 

    def createConfiguration(self, args={}):
        '''
        Adds configuration value

        args - A dictionary. The following are options for keys:
            category - component's category
            component - the component of the configuration
            instance - the instance of the configuration
            name - the name of the configuration
            description - the description of the configuration
            value - the value of the configuration
        '''
        if not 'category' in args:
            raise RuntimeError("Missing required argument 'category'")
        if not 'component' in args:
            raise RuntimeError("Missing required argument 'component'")
        if not 'instance' in args:
            raise RuntimeError("Missing required argument 'instance'")
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('createConfiguration', args)
 

    def listCapabilities(self, args={}):
        '''
        Lists capabilities

        args - A dictionary. The following are options for keys:
            page - Pagination
        '''

        return self.request('listCapabilities', args)
 

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
            zoneid - list Pods by Zone ID
            page - Pagination
        '''

        return self.request('listPods', args)
 

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
            vlan - the VLAN for the Zone
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
            domain - Network domain name for the networks in the zone
            guestcidraddress - the guest CIDR address for the Zone
            internaldns1 - the first internal DNS for the Zone
            internaldns2 - the second internal DNS for the Zone
            ispublic - updates a private zone to public if set, but not vice-versa
            name - the name of the Zone
            vlan - the VLAN for the Zone
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
            page - Pagination
        '''

        return self.request('listZones', args)
 

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
        '''

        return self.request('updateNetworkOffering', args)
 

    def listNetworkOfferings(self, args={}):
        '''
        Lists all available network offerings.

        args - A dictionary. The following are options for keys:
            availability - the availability of network offering. Default value is
               Required
            displaytext - list network offerings by display text
            guestiptype - the guest ip type for the network offering, supported types
               are Direct and Virtual.
            id - list network offerings by id
            isdefault - true if need to list only default network offerings. Default
               value is false
            isshared - true is network offering supports vlans
            keyword - List by keyword
            name - list network offerings by name
            page - 
            pagesize - 
            specifyvlan - the tags for the network offering.
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
            domainid - domain ID of the account owning a network
            endip - the ending IP address in the network IP range. If not specified,
               will be defaulted to startIP
            gateway - the gateway of the network
            isdefault - true if network is default, false otherwise
            isshared - true is network is shared across accounts in the Zone
            netmask - the netmask of the network
            networkdomain - network domain
            startip - the beginning IP address in the network IP range
            tags - Tag the network
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
            account - account who will own the VLAN. If VLAN is Zone wide, this
               parameter should be ommited
            domainid - domain ID of the account owning a VLAN
            id - list networks by id
            isdefault - true if network is default, false otherwise
            isshared - true if network is shared across accounts in the Zone, false
               otherwise
            issystem - true if network is system, false otherwise
            keyword - List by keyword
            page - 
            pagesize - 
            traffictype - type of the traffic
            type - the type of the network
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
            displaytext - the new display text for the network
            name - the new name for the network
            networkdomain - network domain
            tags - tags for the network
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('updateNetwork', args)
 

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
            account - the account of the remote access vpn. Must be used with the
               domainId parameter.
            domainid - the domain ID of the remote access vpn rule. If used with the
               account parameter, lists remote access vpns for the account in the specified
               domain.
            keyword - List by keyword
            page - 
            pagesize - 
            page - Pagination
        '''
        if not 'publicipid' in args:
            raise RuntimeError("Missing required argument 'publicipid'")

        return self.request('listRemoteAccessVpns', args)
 

    def addVpnUser(self, args={}):
        '''
        Adds vpn users

        args - A dictionary. The following are options for keys:
            password - password for the username
            username - username for the vpn user
            account - an optional account for the vpn user. Must be used with domainId.
            domainid - an optional domainId for the vpn user. If the account parameter
               is used, domainId must also be used.
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
        '''
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")

        return self.request('removeVpnUser', args)
 

    def listVpnUsers(self, args={}):
        '''
        Lists vpn users

        args - A dictionary. The following are options for keys:
            account - the account of the remote access vpn. Must be used with the
               domainId parameter.
            domainid - the domain ID of the remote access vpn. If used with the account
               parameter, lists remote access vpns for the account in the specified domain.
            id - the ID of the vpn user
            keyword - List by keyword
            page - 
            pagesize - 
            username - the username of the vpn user.
            page - Pagination
        '''

        return self.request('listVpnUsers', args)
 

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
            account - Lists resource limits by account. Must be used with the domainId
               parameter.
            domainid - Lists resource limits by domain ID. If used with the account
               parameter, lists resource limits for a specified account in a specified domain.
            id - Lists resource limits by ID.
            keyword - List by keyword
            page - 
            pagesize - 
            resourcetype - Type of resource to update. Values are 0, 1, 2, 3, and 4. 0 -
               Instance. Number of instances a user can create. 1 - IP. Number of public IP
               addresses a user can own. 2 - Volume. Number of disk volumes a user can create.3
               - Snapshot. Number of snapshots a user can create.4 - Template. Number of
               templates that a user can register/create.
            page - Pagination
        '''

        return self.request('listResourceLimits', args)
 

    def getCloudIdentifier(self, args={}):
        '''
        Retrieves a cloud identifier.

        args - A dictionary. The following are options for keys:
            userid - the user ID for the cloud identifier
        '''
        if not 'userid' in args:
            raise RuntimeError("Missing required argument 'userid'")

        return self.request('getCloudIdentifier', args)
 

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
 

    def createInstanceGroup(self, args={}):
        '''
        Creates a vm group

        args - A dictionary. The following are options for keys:
            name - the name of the instance group
            account - the account of the instance group. The account parameter must be
               used with the domainId parameter.
            domainid - the domain ID of account owning the instance group
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
            account - list instance group belonging to the specified account. Must be
               used with domainid parameter
            domainid - the domain ID. If used with the account parameter, lists virtual
               machines for the specified account in this domain.
            id - list instance groups by ID
            keyword - List by keyword
            name - list instance groups by name
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listInstanceGroups', args)
 

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
 

    def deleteStoragePool(self, args={}):
        '''
        Deletes a storage pool.

        args - A dictionary. The following are options for keys:
            id - Storage pool id
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteStoragePool', args)
 

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
        '''

        return self.request('deleteSecurityGroup', args)
 

    def authorizeSecurityGroupIngress(self, args={}):
        '''
        Authorizes a particular ingress rule for this security group

        args - A dictionary. The following are options for keys:
            account - an optional account for the virtual machine. Must be used with
               domainId.
            cidrlist - the cidr list associated
            domainid - an optional domainId for the security group. If the account
               parameter is used, domainId must also be used.
            endport - end port for this ingress rule
            icmpcode - error code for this icmp message
            icmptype - type of the icmp message being sent
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
 

    def listSecurityGroups(self, args={}):
        '''
        Lists security groups

        args - A dictionary. The following are options for keys:
            account - lists all available port security groups for the account. Must be
               used with domainID parameter
            domainid - lists all available security groups for the domain ID. If used
               with the account parameter, lists all available security groups for the account
               in the specified domain ID.
            id - list the security group by the id provided
            keyword - List by keyword
            page - 
            pagesize - 
            securitygroupname - lists security groups by name
            virtualmachineid - lists security groups by virtual machine id
            page - Pagination
        '''

        return self.request('listSecurityGroups', args)
 

    def registerSSHKeyPair(self, args={}):
        '''
        Register a public key in a keypair under a certain name

        args - A dictionary. The following are options for keys:
            name - Name of the keypair
            publickey - Public key material of the keypair
            account - an optional account for the ssh key. Must be used with domainId.
            domainid - an optional domainId for the ssh key. If the account parameter is
               used, domainId must also be used.
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")
        if not 'publickey' in args:
            raise RuntimeError("Missing required argument 'publickey'")

        return self.request('registerSSHKeyPair', args)
 

    def createSSHKeyPair(self, args={}):
        '''
        Create a new keypair and returns the private key

        args - A dictionary. The following are options for keys:
            name - Name of the keypair
            account - an optional account for the ssh key. Must be used with domainId.
            domainid - an optional domainId for the ssh key. If the account parameter is
               used, domainId must also be used.
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
        '''
        if not 'name' in args:
            raise RuntimeError("Missing required argument 'name'")

        return self.request('deleteSSHKeyPair', args)
 

    def listSSHKeyPairs(self, args={}):
        '''
        List registered keypairs

        args - A dictionary. The following are options for keys:
            fingerprint - A public key fingerprint to look for
            keyword - List by keyword
            name - A key pair name to look for
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listSSHKeyPairs', args)
 

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
            account - the account associated with the async job. Must be used with the
               domainId parameter.
            domainid - the domain ID associated with the async job.  If used with the
               account parameter, returns async jobs for the account in the specified domain.
            keyword - List by keyword
            page - 
            pagesize - 
            startdate - the start date of the async job
            page - Pagination
        '''

        return self.request('listAsyncJobs', args)
 

    def uploadCustomCertificate(self, args={}):
        '''
        Uploads custom certificate

        args - A dictionary. The following are options for keys:
            certificate - the custom cert to be uploaded
            domainsuffix - DNS domain suffix that the certificate is granted for
            privatekey - the private key for the certificate
        '''
        if not 'certificate' in args:
            raise RuntimeError("Missing required argument 'certificate'")
        if not 'domainsuffix' in args:
            raise RuntimeError("Missing required argument 'domainsuffix'")
        if not 'privatekey' in args:
            raise RuntimeError("Missing required argument 'privatekey'")

        return self.request('uploadCustomCertificate', args)
 

    def listHypervisors(self, args={}):
        '''
        List hypervisors

        args - A dictionary. The following are options for keys:
            zoneid - the zone id for listing hypervisors.
            page - Pagination
        '''

        return self.request('listHypervisors', args)
 

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
 

    def listEvents(self, args={}):
        '''
        A command to list events.

        args - A dictionary. The following are options for keys:
            account - the account for the event. Must be used with the domainId
               parameter.
            domainid - the domain ID for the event. If used with the account parameter,
               returns all events for an account in the specified domain ID.
            duration - the duration of the event
            enddate - the end date range of the list you want to retrieve (use format
               "yyyy-MM-dd" or the new format "yyyy-MM-dd HH:mm:ss")
            entrytime - the time the event was entered
            id - the ID of the event
            keyword - List by keyword
            level - the event level (INFO, WARN, ERROR)
            page - 
            pagesize - 
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
        '''
        if not 'username' in args:
            raise RuntimeError("Missing required argument 'username'")
        if not 'password' in args:
            raise RuntimeError("Missing required argument 'password'")

        return self.request('login', args)
 

    def logout(self, args={}):
        '''
        Logs out the user

        args - A dictionary. The following are options for keys:
        '''

        return self.request('logout', args)
 

    def listCapacity(self, args={}):
        '''
        Lists capacity.

        args - A dictionary. The following are options for keys:
            hostid - lists capacity by the Host ID
            keyword - List by keyword
            page - 
            pagesize - 
            podid - lists capacity by the Pod ID
            type - lists capacity by type
            zoneid - lists capacity by the Zone ID
            page - Pagination
        '''

        return self.request('listCapacity', args)
 

    def addNetworkDevice(self, args={}):
        '''
        List external load balancer appliances.

        args - A dictionary. The following are options for keys:
            networkdeviceparameterlist - parameters for network device
            networkdevicetype - Network device type, now supports ExternalDhcp,
               ExternalFirewall, ExternalLoadBalancer, PxeServer
        '''

        return self.request('addNetworkDevice', args)
 

    def listNetworkDevice(self, args={}):
        '''
        List network device.

        args - A dictionary. The following are options for keys:
            keyword - List by keyword
            networkdeviceparameterlist - parameters for network device
            networkdevicetype - Network device type, now supports ExternalDhcp,
               ExternalFirewall, ExternalLoadBalancer, PxeServer
            page - 
            pagesize - 
            page - Pagination
        '''

        return self.request('listNetworkDevice', args)
 

    def deleteNetworkDevice(self, args={}):
        '''
        Delete network device.

        args - A dictionary. The following are options for keys:
            id - Id of network device to delete
        '''

        return self.request('deleteNetworkDevice', args)
 

    def addExternalLoadBalancer(self, args={}):
        '''
        Adds an external load balancer appliance.

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
        Deletes an external load balancer appliance.

        args - A dictionary. The following are options for keys:
            id - Id of the external loadbalancer appliance.
        '''
        if not 'id' in args:
            raise RuntimeError("Missing required argument 'id'")

        return self.request('deleteExternalLoadBalancer', args)
 

    def listExternalLoadBalancers(self, args={}):
        '''
        List external load balancer appliances.

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
 

    def generateUsageRecords(self, args={}):
        '''
        Generates usage records

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
            page - Pagination
        '''
        if not 'enddate' in args:
            raise RuntimeError("Missing required argument 'enddate'")
        if not 'startdate' in args:
            raise RuntimeError("Missing required argument 'startdate'")

        return self.request('listUsageRecords', args)
 

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
 

