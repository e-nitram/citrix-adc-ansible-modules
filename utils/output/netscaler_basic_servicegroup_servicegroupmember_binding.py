#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'commiter',
                    'version': '1.0'}


DOCUMENTATION = '''
---
module: XXX
short_description: XXX
description:
    - XXX

version_added: 2.3.1

options:

    servicegroupname:
        description:
            - "Name of the service group."
            - "Minimum length = 1"

    ip:
        description:
            - "IP Address."

    port:
        description:
            - "Server port number."
            - "Range 1 - 65535"
            - "* in CLI is represented as 65535 in NITRO API"

    state:
        choices:
            - 'ENABLED'
            - 'DISABLED'
        description:
            - "Initial state of the service group."
            - "Default value: ENABLED"
            - "Possible values = ENABLED, DISABLED"

    hashid:
        description:
            - >-
                The hash identifier for the service. This must be unique for each service. This parameter is used by
                hash based load balancing methods.
            - "Minimum value = 1"

    serverid:
        description:
            - "The identifier for the service. This is used when the persistency type is set to Custom Server ID."

    servername:
        description:
            - "Name of the server to which to bind the service group."
            - "Minimum length = 1"

    customserverid:
        description:
            - "The identifier for this IP:Port pair. Used when the persistency type is set to Custom Server ID."
            - "Default value: \"None\""

    weight:
        description:
            - >-
                Weight to assign to the servers in the service group. Specifies the capacity of the servers relative
                to the other servers in the load balancing configuration. The higher the weight, the higher the
                percentage of requests sent to the service.
            - "Minimum value = 1"
            - "Maximum value = 100"


extends_documentation_fragment: netscaler
requirements:
    - nitro python sdk
'''

EXAMPLES = '''
'''

RETURN = '''
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    from ansible.module_utils.netscaler import ConfigProxy, get_nitro_client, netscaler_common_arguments, log, loglines, ensure_feature_is_enabled
    try:
        from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
        python_sdk_imported = True
    except ImportError as e:
        python_sdk_imported = False

    module_specific_arguments = dict(
        servicegroupname=dict(type='str'),
        ip=dict(type='str'),
        port=dict(type='int'),
        state=dict(
            type='str',
            choices=[
                'ENABLED',
                'DISABLED',
            ]
        ),
        hashid=dict(type='float'),
        serverid=dict(type='float'),
        servername=dict(type='str'),
        customserverid=dict(type='str'),
        weight=dict(type='float'),
    )

    hand_inserted_arguments = dict(
    )

    argument_spec = dict()

    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)
    argument_spec.update(hand_inserted_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )
    module_result = dict(
        changed=False,
        failed=False,
        loglines=loglines,
    )

    # Fail the module if imports failed
    if not python_sdk_imported:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution
    client = get_nitro_client(module)
    client.login()

    readwrite_attrs = [
        'servicegroupname',
        'ip',
        'port',
        'state',
        'hashid',
        'serverid',
        'servername',
        'customserverid',
        'weight',
    ]

    readonly_attrs = [
        'delay',
        'statechangetimesec',
        'svrstate',
        'tickssincelaststatechange',
        'graceful',
        '__count',
    ]

    # Instantiate config proxy
    _proxy = ConfigProxy(
        actual=_(),
        client=client,
        attribute_values_dict=module.params,
        readwrite_attrs=readwrite_attrs,
        readonly_attrs=readonly_attrs,
    )

    def _exists():
        if _.count_filtered(client, 'name:%s' % module.params['name']) > 0:
            return True
        else:
            return False

    def _identical():
        _list = _.get_filtered(client, 'name:%s' % module.params['name'])
        diff_dict = _proxy.diff_object(_list[0])
        if len(diff_dict) == 0:
            return True
        else:
            return False

    def diff():
        _list = _.get_filtered(client, 'name:%s' % module.params['name'])
        return _proxy.diff_object(_list[0])

    try:
        ensure_feature_is_enabled(client, ' _')
        # Apply appropriate operation
        if module.params['operation'] == 'present':
            if not _exists():
                if not module.check_mode:
                    _proxy.add()
                    client.save_config()
                module_result['changed'] = True
            elif not _identical():
                if not module.check_mode:
                    _proxy.update()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not module.check_mode:
                if not _exists():
                    module.fail_json(msg='Service does not exist', **module_result)
                if not _identical():
                    module.fail_json(msg='Service differs from configured', diff=diff(), **module_result)

        elif module.params['operation'] == 'absent':
            if _exists():
                if not module.check_mode:
                    _proxy.delete()
                    client.save_config()
                module_result['changed'] = True
            else:
                module_result['changed'] = False

            # Sanity check for operation
            if not module.check_mode:
                if _exists():
                    module.fail_json(msg='Service still exists', **module_result)

    except nitro_exception as e:
        msg = "nitro exception errorcode=%s, message=%s" % (str(e.errorcode), e.message)
        module.fail_json(msg=msg, **module_result)

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
