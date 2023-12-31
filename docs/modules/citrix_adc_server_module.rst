:orphan:

.. _citrix_adc_server_module:

citrix_adc_server - Manage server configuration
+++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage server entities configuration.
- This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual Citrix ADC instance.



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
    * - api_path

        *(str)*
      -
      - Base NITRO API path.

        Define only in case of an ADM service proxy call
    * - bearer_token

        *(str)*
      -
      - Authentication bearer token.

        Needed when doing an ADM service proxy call.
    * - comment

        *(str)*
      -
      - Any information about the server.
    * - delay

        *(float)*
      -
      - Time, in seconds, after which all the services configured on the server are disabled.

        This option is meaningful only when setting the ``disabled`` option to ``true``
    * - disabled

        *(bool)*
      - Default:

        *False*
      - When set to ``true`` the server state will be set to ``disabled``.

        When set to ``false`` the server state will be set to ``enabled``.

        Note that due to limitations of the underlying NITRO API a ``disabled`` state change alone does not cause the module result to report a changed status.
    * - domain

        *(str)*
      -
      - Domain name of the server. For a domain based configuration, you must create the server first.

        Minimum length = 1
    * - domainresolveretry

        *(int)*
      -
      - Time, in seconds, for which the Citrix ADC appliance must wait, after DNS resolution fails, before sending the next DNS query to resolve the domain name.

        Minimum value = ``5``

        Maximum value = ``20939``
    * - graceful

        *(bool)*
      -
      - Shut down gracefully, without accepting any new connections, and disabling each service when all of its connections are closed.

        This option is meaningful only when setting the ``disabled`` option to ``true``
    * - instance_id

        *(str)*
      -
      - The id of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Citrix ADC instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - instance_name

        *(str)*
      -
      - The name of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
    * - ipaddress

        *(str)*
      -
      - IPv4 or IPv6 address of the server. If you create an IP address based server, you can specify the name of the server, instead of its IP address, when creating a service. Note: If you do not create a server entry, the server IP address that you enter when you create a service becomes the name of the server.
    * - ipv6address

        *(bool)*
      - Default:

        *False*
      - Support IPv6 addressing mode. If you configure a server with the IPv6 addressing mode, you cannot use the server in the IPv4 addressing mode.
    * - is_cloud

        *(bool)*
      - Default:

        *False*
      - When performing a Proxy API call with ADM service set this to ``true``
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Citrix ADC instance.

        When true you must also define the following options: ``nitro_auth_token``

        When true and adm service is the api proxy the following option must also be defined: ``bearer_token``

        When true you must define a target ADC by defining any of the following parameters

        I(instance_ip)

        I(instance_id)

        I(instance_name)
    * - name

        *(str)*
      -
      - Name for the server.

        Must begin with an ASCII alphabetic or underscore ``_`` character, and must contain only ASCII alphanumeric, underscore ``_``, hash ``#``, period ``.``, space `` ``, colon ``:``, at ``@``, equals ``=``, and hyphen ``-`` characters.

        Can be changed after the name is created.

        Minimum length = 1
    * - nitro_auth_token

        *(str)*

        *(added in 2.6.0)*
      -
      - The authentication token provided by a login operation.
    * - nitro_pass

        *(str)*
      -
      - The password with which to authenticate to the Citrix ADC node.
    * - nitro_protocol

        *(str)*
      - Choices:

          - http
          - https (*default*)
      - Which protocol to use when accessing the nitro API objects.
    * - nitro_timeout

        *(float)*
      - Default:

        *310*
      - Time in seconds until a timeout error is thrown when establishing a new session with Citrix ADC
    * - nitro_user

        *(str)*
      -
      - The username with which to authenticate to the Citrix ADC node.
    * - nsip

        *(str)*
      -
      - The ip address of the Citrix ADC appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the Citrix ADC node if it makes any changes.

        The module will not save the configuration on the Citrix ADC node if it made no changes.
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the Citrix ADC node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the Citrix ADC node.
    * - td

        *(float)*
      -
      - Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.

        Minimum value = ``0``

        Maximum value = ``4094``
    * - translationip

        *(str)*
      -
      - IP address used to transform the server's DNS-resolved IP address.
    * - translationmask

        *(str)*
      -
      - The netmask of the translation ip.
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    - name: Setup server
      delegate_to: localhost
      citrix_adc_server:
          nsip: 172.18.0.2
          nitro_user: nsroot
          nitro_pass: nsroot
    
          state: present
    
          name: server-1
          ipaddress: 192.168.1.1


Return Values
-------------
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Key
      - Returned
      - Description
    * - diff_list

        *(dict)*
      - failure
      - List of differences between the actual configured object and the configuration specified in the module

        **Sample:**

        {'targetlbvserver': 'difference. ours: (str) server1 other: (str) server2'}
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
