:orphan:

.. _citrix_adc_lb_vserver_module:

citrix_adc_lb_vserver - Manage load balancing vserver configuration
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage load balancing vserver configuration
- This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance



Requirements
~~~~~~~~~~~~
The below requirements are needed on the host that executes this module.

- nitro python sdk


Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - appflowlog
      - Choices:

          - enabled
          - disabled
      - Apply AppFlow logging to the virtual server.
    * - appfw_policybindings

        *(list)*
      -
      - List of appfw policy bindings
    * - authentication

        *(bool)*
      -
      - Enable or disable user authentication.
    * - authenticationhost
      -
      - Fully qualified domain name (FQDN) of the authentication virtual server to which the user must be redirected for authentication. Make sure that the Authentication parameter is set to ``yes``.

        Minimum length = 3

        Maximum length = 252
    * - authn401

        *(bool)*
      -
      - Enable or disable user authentication with HTTP 401 responses.
    * - authnprofile
      -
      - Name of the authentication profile to be used when authentication is turned on.
    * - authnvsname
      -
      - Name of an authentication virtual server with which to authenticate users.

        Minimum length = 1

        Maximum length = 252
    * - backuplbmethod
      - Choices:

          - ROUNDROBIN
          - LEASTCONNECTION
          - LEASTRESPONSETIME
          - SOURCEIPHASH
          - LEASTBANDWIDTH
          - LEASTPACKETS
          - CUSTOMLOAD
      - Backup load balancing method. Becomes operational if the primary load balancing me

        thod fails or cannot be used.

        Valid only if the primary method is based on static proximity.
    * - backuppersistencetimeout
      -
      - Time period for which backup persistence is in effect.

        Minimum value = ``2``

        Maximum value = ``1440``
    * - bypassaaaa

        *(bool)*
      -
      - If this option is enabled while resolving DNS64 query AAAA queries are not sent to back end dns server.
    * - cacheable

        *(bool)*
      -
      - Route cacheable requests to a cache redirection virtual server. The load balancing virtual server can forward requests only to a transparent cache redirection virtual server that has an IP address and port combination of *:80, so such a cache redirection virtual server must be configured on the appliance.
    * - clttimeout
      -
      - Idle time, in seconds, after which a client connection is terminated.

        Minimum value = ``0``

        Maximum value = ``31536000``
    * - comment
      -
      - Any comments that you might want to associate with the virtual server.
    * - connfailover
      - Choices:

          - DISABLED
          - STATEFUL
          - STATELESS
      - Mode in which the connection failover feature must operate for the virtual server. After a failover, established TCP connections and UDP packet flows are kept active and resumed on the secondary appliance. Clients remain connected to the same servers. Available settings function as follows:

        * ``STATEFUL`` - The primary appliance shares state information with the secondary appliance, in real time, resulting in some runtime processing overhead.

        * ``STATELESS`` - State information is not shared, and the new primary appliance tries to re-create the packet flow on the basis of the information contained in the packets it receives.

        * ``DISABLED`` - Connection failover does not occur.
    * - cookiename
      -
      - Use this parameter to specify the cookie name for ``COOKIE`` peristence type. It specifies the name of cookie with a maximum of 32 characters. If not specified, cookie name is internally generated.
    * - datalength
      -
      - Length of the token to be extracted from the data segment of an incoming packet, for use in the token method of load balancing. The length of the token, specified in bytes, must not be greater than 24 KB. Applicable to virtual servers of type TCP.

        Minimum value = ``1``

        Maximum value = ``100``
    * - dataoffset
      -
      - Offset to be considered when extracting a token from the TCP payload. Applicable to virtual servers, of type TCP, using the token method of load balancing. Must be within the first 24 KB of the TCP payload.

        Minimum value = ``0``

        Maximum value = ``25400``
    * - dbprofilename
      -
      - Name of the DB profile whose settings are to be applied to the virtual server.

        Minimum length = 1

        Maximum length = 127
    * - dbslb
      - Choices:

          - enabled
          - disabled
      - Enable database specific load balancing for MySQL and MSSQL service types.
    * - disabled

        *(bool)*
      - Default:

        *no*
      - When set to ``yes`` the lb vserver will be disabled.

        When set to ``no`` the lb vserver will be enabled.

        Note that due to limitations of the underlying NITRO API a ``disabled`` state change alone does not cause the module result to report a changed status.
    * - disableprimaryondown
      - Choices:

          - enabled
          - disabled
      - If the primary virtual server goes down, do not allow it to return to primary status until manually enabled.
    * - dns64
      - Choices:

          - enabled
          - disabled
      - This argument is for enabling/disabling the ``dns64`` on lbvserver.
    * - dnsprofilename
      -
      - Name of the DNS profile to be associated with the VServer. DNS profile properties will be applied to the transactions processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.

        Minimum length = 1

        Maximum length = 127
    * - downstateflush
      - Choices:

          - enabled
          - disabled
      - Flush all active transactions associated with a virtual server whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.
    * - hashlength
      -
      - Number of bytes to consider for the hash value used in the URLHASH and DOMAINHASH load balancing methods.

        Minimum value = ``1``

        Maximum value = ``4096``
    * - healththreshold
      -
      - Threshold in percent of active services below which vserver state is made down. If this threshold is 0, vserver state will be up even if one bound service is up.

        Minimum value = ``0``

        Maximum value = ``100``
    * - httpprofilename
      -
      - Name of the HTTP profile whose settings are to be applied to the virtual server.

        Minimum length = 1

        Maximum length = 127
    * - icmpvsrresponse
      - Choices:

          - PASSIVE
          - ACTIVE
      - How the NetScaler appliance responds to ping requests received for an IP address that is common to one or more virtual servers. Available settings function as follows:

        * If set to ``PASSIVE`` on all the virtual servers that share the IP address, the appliance always responds to the ping requests.

        * If set to ``ACTIVE`` on all the virtual servers that share the IP address, the appliance responds to the ping requests if at least one of the virtual servers is UP. Otherwise, the appliance does not respond.

        * If set to ``ACTIVE`` on some virtual servers and PASSIVE on the others, the appliance responds if at least one virtual server with the ACTIVE setting is UP. Otherwise, the appliance does not respond.

        Note: This parameter is available at the virtual server level. A similar parameter, ICMP Response, is available at the IP address level, for IPv4 addresses of type VIP. To set that parameter, use the add ip command in the CLI or the Create IP dialog box in the GUI.
    * - insertvserveripport
      - Choices:

          - OFF
          - VIPADDR
          - V6TOV4MAPPING
      - Insert an HTTP header, whose value is the IP address and port number of the virtual server, before forwarding a request to the server. The format of the header is <vipHeader>: <virtual server IP address>_<port number >, where vipHeader is the name that you specify for the header. If the virtual server has an IPv6 address, the address in the header is enclosed in brackets ([ and ]) to separate it from the port number. If you have mapped an IPv4 address to a virtual server's IPv6 address, the value of this parameter determines which IP address is inserted in the header, as follows:

        * ``VIPADDR`` - Insert the IP address of the virtual server in the HTTP header regardless of whether the virtual server has an IPv4 address or an IPv6 address. A mapped IPv4 address, if configured, is ignored.

        * ``V6TOV4MAPPING`` - Insert the IPv4 address that is mapped to the virtual server's IPv6 address. If a mapped IPv4 address is not configured, insert the IPv6 address.

        * ``OFF`` - Disable header insertion.
    * - instance_ip

        *(added in 2.6.0)*
      -
      - The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - ipmask
      -
      - IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing non-zero octets (for example, ``255.255.240.0`` or ``0.0.255.255``). Accordingly, the mask specifies whether the first n bits or the last n bits of the destination IP address in a client request are to be matched with the corresponding bits in the IP pattern. The former is called a forward mask. The latter is called a reverse mask.
    * - ippattern
      -
      - IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual server. The IP Mask parameter specifies which part of the destination IP address is matched against the pattern. Mutually exclusive with the IP Address parameter.

        For example, if the IP pattern assigned to the virtual server is ``198.51.100.0`` and the IP mask is ``255.255.240.0`` (a forward mask), the first 20 bits in the destination IP addresses are matched with the first 20 bits in the pattern. The virtual server accepts requests with IP addresses that range from ``198.51.96.1`` to ``198.51.111.254``. You can also use a pattern such as ``0.0.2.2`` and a mask such as ``0.0.255.255`` (a reverse mask).

        If a destination IP address matches more than one IP pattern, the pattern with the longest match is selected, and the associated virtual server processes the request. For example, if virtual servers ``vs1`` and ``vs2`` have the same IP pattern, ``0.0.100.128``, but different IP masks of ``0.0.255.255`` and ``0.0.224.255``, a destination IP address of ``198.51.100.128`` has the longest match with the IP pattern of vs1. If a destination IP address matches two or more virtual servers to the same extent, the request is processed by the virtual server whose port number matches the port number in the request.
    * - ipv46
      -
      - IPv4 or IPv6 address to assign to the virtual server.
    * - l2conn

        *(bool)*
      -
      - Use Layer 2 parameters (channel number, MAC address, and VLAN ID) in addition to the 4-tuple (<source IP>:<source port>::<destination IP>:<destination port>) that is used to identify a connection. Allows multiple TCP and non-TCP connections with the same 4-tuple to co-exist on the NetScaler appliance.
    * - lbmethod
      - Choices:

          - ROUNDROBIN
          - LEASTCONNECTION
          - LEASTRESPONSETIME
          - URLHASH
          - DOMAINHASH
          - DESTINATIONIPHASH
          - SOURCEIPHASH
          - SRCIPDESTIPHASH
          - LEASTBANDWIDTH
          - LEASTPACKETS
          - TOKEN
          - SRCIPSRCPORTHASH
          - LRTM
          - CALLIDHASH
          - CUSTOMLOAD
          - LEASTREQUEST
          - AUDITLOGHASH
          - STATICPROXIMITY
      - Load balancing method. The available settings function as follows:

        * ``ROUNDROBIN`` - Distribute requests in rotation, regardless of the load. Weights can be assigned to services to enforce weighted round robin distribution.

        * ``LEASTCONNECTION`` (default) - Select the service with the fewest connections.

        * ``LEASTRESPONSETIME`` - Select the service with the lowest average response time.

        * ``LEASTBANDWIDTH`` - Select the service currently handling the least traffic.

        * ``LEASTPACKETS`` - Select the service currently serving the lowest number of packets per second.

        * ``CUSTOMLOAD`` - Base service selection on the SNMP metrics obtained by custom load monitors.

        * ``LRTM`` - Select the service with the lowest response time. Response times are learned through monitoring probes. This method also takes the number of active connections into account.

        Also available are a number of hashing methods, in which the appliance extracts a predetermined portion of the request, creates a hash of the portion, and then checks whether any previous requests had the same hash value. If it finds a match, it forwards the request to the service that served those previous requests. Following are the hashing methods:

        * ``URLHASH`` - Create a hash of the request URL (or part of the URL).

        * ``DOMAINHASH`` - Create a hash of the domain name in the request (or part of the domain name). The domain name is taken from either the URL or the Host header. If the domain name appears in both locations, the URL is preferred. If the request does not contain a domain name, the load balancing method defaults to ``LEASTCONNECTION``.

        * ``DESTINATIONIPHASH`` - Create a hash of the destination IP address in the IP header.

        * ``SOURCEIPHASH`` - Create a hash of the source IP address in the IP header.

        * ``TOKEN`` - Extract a token from the request, create a hash of the token, and then select the service to which any previous requests with the same token hash value were sent.

        * ``SRCIPDESTIPHASH`` - Create a hash of the string obtained by concatenating the source IP address and destination IP address in the IP header.

        * ``SRCIPSRCPORTHASH`` - Create a hash of the source IP address and source port in the IP header.

        * ``CALLIDHASH`` - Create a hash of the SIP Call-ID header.
    * - listenpolicy
      -
      - Default syntax expression identifying traffic accepted by the virtual server. Can be either an expression (for example, ``CLIENT.IP.DST.IN_SUBNET(192.0.2.0/24``) or the name of a named expression. In the above example, the virtual server accepts all requests whose destination IP address is in the 192.0.2.0/24 subnet.
    * - listenpriority
      -
      - Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If a request matches the listen policies of more than one virtual server the virtual server whose listen policy has the highest priority (the lowest priority number) accepts the request.

        Minimum value = ``0``

        Maximum value = ``101``
    * - m
      - Choices:

          - IP
          - MAC
          - IPTUNNEL
          - TOS
      - Redirection mode for load balancing. Available settings function as follows:

        * ``IP`` - Before forwarding a request to a server, change the destination IP address to the server's IP address.

        * ``MAC`` - Before forwarding a request to a server, change the destination MAC address to the server's MAC address. The destination IP address is not changed. MAC-based redirection mode is used mostly in firewall load balancing deployments.

        * ``IPTUNNEL`` - Perform IP-in-IP encapsulation for client IP packets. In the outer IP headers, set the destination IP address to the IP address of the server and the source IP address to the subnet IP (SNIP). The client IP packets are not modified. Applicable to both IPv4 and IPv6 packets.

        * ``TOS`` - Encode the virtual server's TOS ID in the TOS field of the IP header.

        You can use either the ``IPTUNNEL`` or the ``TOS`` option to implement Direct Server Return (DSR).
    * - macmoderetainvlan
      - Choices:

          - enabled
          - disabled
      - This option is used to retain vlan information of incoming packet when macmode is enabled.
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a MAS node to the target Netscaler instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - maxautoscalemembers
      -
      - Maximum number of members expected to be present when vserver is used in Autoscale.

        Minimum value = ``0``

        Maximum value = ``5000``
    * - minautoscalemembers
      -
      - Minimum number of members expected to be present when vserver is used in Autoscale.

        Minimum value = ``0``

        Maximum value = ``5000``
    * - mssqlserverversion
      - Choices:

          - 70
          - 2000
          - 2000SP1
          - 2005
          - 2008
          - 2008R2
          - 2012
          - 2014
      - For a load balancing virtual server of type ``MSSQL``, the Microsoft SQL Server version. Set this parameter if you expect some clients to run a version different from the version of the database. This setting provides compatibility between the client-side and server-side connections by ensuring that all communication conforms to the server's version.
    * - mysqlcharacterset
      -
      - Character set that the virtual server advertises to clients.
    * - mysqlprotocolversion
      -
      - MySQL protocol version that the virtual server advertises to clients.
    * - mysqlservercapabilities
      -
      - Server capabilities that the virtual server advertises to clients.
    * - mysqlserverversion
      -
      - MySQL server version string that the virtual server advertises to clients.

        Minimum length = 1

        Maximum length = 31
    * - name
      -
      - Name for the virtual server. Must begin with an ASCII alphanumeric or underscore ``_`` character, and must contain only ASCII alphanumeric, underscore, hash ``#``, period ``.``, space `` ``, colon ``:``, at sign ``@``, equal sign ``=``, and hyphen ``-`` characters. Can be changed after the virtual server is created.

        Minimum length = 1
    * - netmask
      -
      - IPv4 subnet mask to apply to the destination IP address or source IP address when the load balancing method is ``DESTINATIONIPHASH`` or ``SOURCEIPHASH``.

        Minimum length = 1
    * - netprofile
      -
      - Name of the network profile to associate with the virtual server. If you set this parameter, the virtual server uses only the IP addresses in the network profile as source IP addresses when initiating connections with servers.

        Minimum length = 1

        Maximum length = 127
    * - newservicerequest
      -
      - Number of requests, or percentage of the load on existing services, by which to increase the load on a new service at each interval in slow-start mode. A non-zero value indicates that slow-start is applicable. A zero value indicates that the global RR startup parameter is applied. Changing the value to zero will cause services currently in slow start to take the full traffic as determined by the LB method. Subsequently, any new services added will use the global RR factor.
    * - newservicerequestincrementinterval
      -
      - Interval, in seconds, between successive increments in the load on a new service or a service whose state has just changed from DOWN to UP. A value of 0 (zero) specifies manual slow start.

        Minimum value = ``0``

        Maximum value = ``3600``
    * - newservicerequestunit
      - Choices:

          - PER_SECOND
          - PERCENT
      - Units in which to increment load at each interval in slow-start mode.
    * - nitro_auth_token

        *(added in 2.6.0)*
      -
      - The authentication token provided by a login operation.
    * - nitro_pass
      -
      - The password with which to authenticate to the netscaler node.
    * - nitro_protocol
      - Choices:

          - http (*default*)
          - https
      - Which protocol to use when accessing the nitro API objects.
    * - nitro_timeout
      - Default:

        *310*
      - Time in seconds until a timeout error is thrown when establishing a new session with Netscaler
    * - nitro_user
      -
      - The username with which to authenticate to the netscaler node.
    * - nsip
      -
      - The ip address of the netscaler appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - oracleserverversion
      - Choices:

          - 10G
          - 11G
      - Oracle server version.
    * - persistencebackup
      - Choices:

          - SOURCEIP
          - NONE
      - Backup persistence type for the virtual server. Becomes operational if the primary persistence mechanism fails.
    * - persistencetype
      - Choices:

          - SOURCEIP
          - COOKIEINSERT
          - SSLSESSION
          - RULE
          - URLPASSIVE
          - CUSTOMSERVERID
          - DESTIP
          - SRCIPDESTIP
          - CALLID
          - RTSPSID
          - DIAMETER
          - FIXSESSION
          - NONE
      - Type of persistence for the virtual server. Available settings function as follows:

        * ``SOURCEIP`` - Connections from the same client IP address belong to the same persistence session.

        * ``COOKIEINSERT`` - Connections that have the same HTTP Cookie, inserted by a Set-Cookie directive from a server, belong to the same persistence session.

        * ``SSLSESSION`` - Connections that have the same SSL Session ID belong to the same persistence session.

        * ``CUSTOMSERVERID`` - Connections with the same server ID form part of the same session. For this persistence type, set the Server ID (CustomServerID) parameter for each service and configure the Rule parameter to identify the server ID in a request.

        * ``RULE`` - All connections that match a user defined rule belong to the same persistence session.

        * ``URLPASSIVE`` - Requests that have the same server ID in the URL query belong to the same persistence session. The server ID is the hexadecimal representation of the IP address and port of the service to which the request must be forwarded. This persistence type requires a rule to identify the server ID in the request.

        * ``DESTIP`` - Connections to the same destination IP address belong to the same persistence session.

        * ``SRCIPDESTIP`` - Connections that have the same source IP address and destination IP address belong to the same persistence session.

        * ``CALLID`` - Connections that have the same CALL-ID SIP header belong to the same persistence session.

        * ``RTSPSID`` - Connections that have the same RTSP Session ID belong to the same persistence session.

        * FIXSESSION - Connections that have the same SenderCompID and TargetCompID values belong to the same persistence session.
    * - persistmask
      -
      - Persistence mask for IP based persistence types, for IPv4 virtual servers.

        Minimum length = 1
    * - port
      -
      - Port number for the virtual server.

        Range ``1`` - ``65535``

        * in CLI is represented as ``65535`` in NITRO API
    * - processlocal
      - Choices:

          - enabled
          - disabled
      - By turning on this option packets destined to a vserver in a cluster will not under go any steering. Turn this option for single packet request response mode or when the upstream device is performing a proper RSS for connection based distribution.
    * - push
      - Choices:

          - enabled
          - disabled
      - Process traffic with the push virtual server that is bound to this load balancing virtual server.
    * - pushlabel
      -
      - Expression for extracting a label from the server's response. Can be either an expression or the name of a named expression.
    * - pushmulticlients

        *(bool)*
      -
      - Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect updates.
    * - pushvserver
      -
      - Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which the server pushes updates received on the load balancing virtual server that you are configuring.

        Minimum length = 1
    * - range
      -
      - Number of IP addresses that the appliance must generate and assign to the virtual server. The virtual server then functions as a network virtual server, accepting traffic on any of the generated IP addresses. The IP addresses are generated automatically, as follows:

        * For a range of n, the last octet of the address specified by the IP Address parameter increments n-1 times.

        * If the last octet exceeds 255, it rolls over to 0 and the third octet increments by 1.

        Note: The Range parameter assigns multiple IP addresses to one virtual server. To generate an array of virtual servers, each of which owns only one IP address, use brackets in the IP Address and Name parameters to specify the range. For example:

        add lb vserver my_vserver[1-3] HTTP 192.0.2.[1-3] 80.

        Minimum value = ``1``

        Maximum value = ``254``
    * - recursionavailable

        *(bool)*
      -
      - When set to YES, this option causes the DNS replies from this vserver to have the RA bit turned on. Typically one would set this option to YES, when the vserver is load balancing a set of DNS servers thatsupport recursive queries.
    * - redirectportrewrite
      - Choices:

          - enabled
          - disabled
      - Rewrite the port and change the protocol to ensure successful HTTP redirects from services.
    * - redirurl
      -
      - URL to which to redirect traffic if the virtual server becomes unavailable.

        WARNING! Make sure that the domain in the URL does not match the domain specified for a content switching policy. If it does, requests are continuously redirected to the unavailable virtual server.

        Minimum length = 1
    * - rhistate
      - Choices:

          - PASSIVE
          - ACTIVE
      - Route Health Injection (RHI) functionality of the NetSaler appliance for advertising the route of the VIP address associated with the virtual server. When Vserver RHI Level (RHI) parameter is set to VSVR_CNTRLD, the following are different RHI behaviors for the VIP address on the basis of RHIstate (RHI STATE) settings on the virtual servers associated with the VIP address:

        * If you set ``rhistate`` to ``PASSIVE`` on all virtual servers, the NetScaler ADC always advertises the route for the VIP address.

        * If you set ``rhistate`` to ``ACTIVE`` on all virtual servers, the NetScaler ADC advertises the route for the VIP address if at least one of the associated virtual servers is in UP state.

        * If you set ``rhistate`` to ``ACTIVE`` on some and PASSIVE on others, the NetScaler ADC advertises the route for the VIP address if at least one of the associated virtual servers, whose ``rhistate`` set to ``ACTIVE``, is in UP state.
    * - rtspnat

        *(bool)*
      -
      - Use network address translation (NAT) for RTSP data connections.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - servicebindings
      -
      - List of services along with the weights that are load balanced.

        The following suboptions are available.

        .. list-table::
            :widths: 10 10 60
            :header-rows: 1

            * - Suboption
              - Choices/Defaults
              - Comment

            * - servicename
              -
              - Service to bind to the virtual server.

                Minimum length = 1
            * - weight
              -
              - Weight to assign to the specified service.

                Minimum value = ``1``

                Maximum value = ``100``

    * - servicegroupbindings
      -
      - List of service groups along with the weights that are load balanced.

        The following suboptions are available.

        .. list-table::
            :widths: 10 10 60
            :header-rows: 1

            * - Suboption
              - Choices/Defaults
              - Comment

            * - servicegroupname
              -
              - The service group name bound to the selected load balancing virtual server.
            * - weight
              -
              - Integer specifying the weight of the service. A larger number specifies a greater weight. Defines the capacity of the service relative to the other services in the load balancing configuration. Determines the priority given to the service in load balancing decisions.

                Minimum value = ``1``

                Maximum value = ``100``

    * - servicetype
      - Choices:

          - HTTP
          - FTP
          - TCP
          - UDP
          - SSL
          - SSL_BRIDGE
          - SSL_TCP
          - DTLS
          - NNTP
          - DNS
          - DHCPRA
          - ANY
          - SIP_UDP
          - SIP_TCP
          - SIP_SSL
          - DNS_TCP
          - RTSP
          - PUSH
          - SSL_PUSH
          - RADIUS
          - RDP
          - MYSQL
          - MSSQL
          - DIAMETER
          - SSL_DIAMETER
          - TFTP
          - ORACLE
          - SMPP
          - SYSLOGTCP
          - SYSLOGUDP
          - FIX
          - SSL_FIX
      - Protocol used by the service (also called the service type).
    * - sessionless
      - Choices:

          - enabled
          - disabled
      - Perform load balancing on a per-packet basis, without establishing sessions. Recommended for load balancing of intrusion detection system (IDS) servers and scenarios involving direct server return (DSR), where session information is unnecessary.
    * - skippersistency
      - Choices:

          - Bypass
          - ReLb
          - None
      - This argument decides the behavior incase the service which is selected from an existing persistence session has reached threshold.
    * - sobackupaction
      - Choices:

          - DROP
          - ACCEPT
          - REDIRECT
      - Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.
    * - somethod
      - Choices:

          - CONNECTION
          - DYNAMICCONNECTION
          - BANDWIDTH
          - HEALTH
          - NONE
      - Type of threshold that, when exceeded, triggers spillover. Available settings function as follows:

        * ``CONNECTION`` - Spillover occurs when the number of client connections exceeds the threshold.

        * DYNAMICCONNECTION - Spillover occurs when the number of client connections at the virtual server exceeds the sum of the maximum client (Max Clients) settings for bound services. Do not specify a spillover threshold for this setting, because the threshold is implied by the Max Clients settings of bound services.

        * ``BANDWIDTH`` - Spillover occurs when the bandwidth consumed by the virtual server's incoming and outgoing traffic exceeds the threshold.

        * ``HEALTH`` - Spillover occurs when the percentage of weights of the services that are UP drops below the threshold. For example, if services svc1, svc2, and svc3 are bound to a virtual server, with weights 1, 2, and 3, and the spillover threshold is 50%, spillover occurs if svc1 and svc3 or svc2 and svc3 transition to DOWN.

        * ``NONE`` - Spillover does not occur.
    * - sopersistence
      - Choices:

          - enabled
          - disabled
      - If spillover occurs, maintain source IP address based persistence for both primary and backup virtual servers.
    * - sopersistencetimeout
      -
      - Timeout for spillover persistence, in minutes.

        Minimum value = ``2``

        Maximum value = ``1440``
    * - sothreshold
      -
      - Threshold at which spillover occurs. Specify an integer for the ``CONNECTION`` spillover method, a bandwidth value in kilobits per second for the ``BANDWIDTH`` method (do not enter the units), or a percentage for the ``HEALTH`` method (do not enter the percentage symbol).

        Minimum value = ``1``

        Maximum value = ``4294967287``
    * - ssl_certkey
      -
      - The name of the ssl certificate that is bound to this service.

        The ssl certificate must already exist.

        Creating the certificate can be done with the citrix_adc_ssl_certkey module.

        This option is only applicable only when ``servicetype`` is ``SSL``.
    * - state
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
    * - tcpprofilename
      -
      - Name of the TCP profile whose settings are to be applied to the virtual server.

        Minimum length = 1

        Maximum length = 127
    * - timeout
      -
      - Time period for which a persistence session is in effect.

        Minimum value = ``0``

        Maximum value = ``1440``
    * - tosid
      -
      - TOS ID of the virtual server. Applicable only when the load balancing redirection mode is set to TOS.

        Minimum value = ``1``

        Maximum value = ``63``
    * - v6netmasklen
      -
      - Number of bits to consider in an IPv6 destination or source IP address, for creating the hash that is required by the ``DESTINATIONIPHASH`` and ``SOURCEIPHASH`` load balancing methods.

        Minimum value = ``1``

        Maximum value = ``128``
    * - v6persistmasklen
      -
      - Persistence mask for IP based persistence types, for IPv6 virtual servers.

        Minimum value = ``1``

        Maximum value = ``128``
    * - validate_certs
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    * - vipheader
      -
      - Name for the inserted header. The default name is vip-header.

        Minimum length = 1



Examples
--------

.. code-block:: yaml+jinja
    
    # Netscaler services service-http-1, service-http-2 must have been already created with the citrix_adc_service module
    
    - name: Create a load balancing vserver bound to services
      delegate_to: localhost
      citrix_adc_lb_vserver:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
        validate_certs: no
    
        state: present
    
        name: lb_vserver_1
        servicetype: HTTP
        timeout: 12
        ipv46: 6.93.3.3
        port: 80
        servicebindings:
            - servicename: service-http-1
              weight: 80
            - servicename: service-http-2
              weight: 20
    
    # Service group service-group-1 must have been already created with the citrix_adc_servicegroup module
    
    - name: Create load balancing vserver bound to servicegroup
      delegate_to: localhost
      citrix_adc_lb_vserver:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
        validate_certs: no
        state: present
    
        name: lb_vserver_2
        servicetype: HTTP
        ipv46: 6.92.2.2
        port: 80
        timeout: 10
        servicegroupbindings:
            - servicegroupname: service-group-1


Return Values
-------------
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Key
      - Returned
      - Description
    * - diff

        *(dict)*
      - failure
      - List of differences between the actual configured object and the configuration specified in the module

        **Sample:**

        {'clttimeout': 'difference. ours: (float) 10.0 other: (float) 20.0'}
    * - loglines

        *(list)*
      - always
      - list of logged messages by the module

        **Sample:**

        ['message 1', 'message 2']
    * - msg

        *(str)*
      - failure
      - Message detailing the failure reason

        **Sample:**

        Action does not exist
