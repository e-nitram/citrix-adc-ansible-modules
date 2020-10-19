#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2017 Citrix Systems
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: citrix_adc_save_config
short_description: Save Netscaler configuration.
description:
    - This module uncoditionally saves the configuration on the target netscaler node.
    - This module does not support check mode.
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.

version_added: "1.0.0"

author: George Nikolopoulos (@giorgos-nikolopoulos)

options:
    nsip:
        type: str
        description:
            - The ip address of the netscaler appliance where the nitro API calls will be made.
            - "The port can be specified with the colon (:). E.g. C(192.168.1.1:555)."
        required: True
        aliases:
            - mas_ip

    nitro_user:
        type: str
        description:
            - The username with which to authenticate to the netscaler node.
        aliases:
            - mas_user

    nitro_pass:
        type: str
        description:
            - The password with which to authenticate to the netscaler node.
        aliases:
            - mas_pass

    nitro_protocol:
        type: str
        choices: [ 'http', 'https' ]
        default: https
        description:
            - Which protocol to use when accessing the nitro API objects.

    validate_certs:
        type: bool
        description:
            - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
        required: false
        default: 'yes'

    nitro_auth_token:
        type: str
        description:
            - The authentication token provided by the C(mas_login) operation. It is required when issuing Nitro API calls through a MAS proxy.
        aliases:
            - mas_auth_token

    nitro_timeout:
        type: float
        description:
            - Time in seconds until a timeout error is thrown when establishing a new session with Netscaler.
        default: 310

    instance_ip:
        type: str
        description:
            - The IP address of the target Netscaler instance when issuing a Nitro request through a MAS proxy.

    mas_proxy_call:
        description:
            - If true the underlying NITRO API calls made by the module will be proxied through a MAS node to the target Netscaler instance.
            - "When true you must also define the following options: I(nitro_auth_token), I(instance_ip)."
        type: bool
        default: false

requirements:
    - nitro python sdk
'''

EXAMPLES = '''
---
- name: Save netscaler configuration
  delegate_to: localhost
  citrix_adc_save_config:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

- name: Setup server without saving  configuration
  delegate_to: localhost
  notify: Save configuration
  citrix_adc_server:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot

    save_config: no

    name: server-1
    ipaddress: 192.168.1.1

# Under playbook's handlers

- name: Save configuration
  delegate_to: localhost
  citrix_adc_save_config:
    nsip: 172.18.0.2
    nitro_user: nsroot
    nitro_pass: nsroot
'''

RETURN = '''
loglines:
    description: list of logged messages by the module
    returned: always
    type: list
    sample: ['message 1', 'message 2']

msg:
    description: Message detailing the failure reason
    returned: failure
    type: str
    sample: "Action does not exist"

'''

import copy

try:
    from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
    PYTHON_SDK_IMPORTED = True
except ImportError as e:
    PYTHON_SDK_IMPORTED = False

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.citrix.citrixadc_modules.plugins.module_utils.citrix_adc import (
    get_nitro_client,
    log,
    loglines,
    netscaler_common_arguments
)


def main():

    argument_spec = copy.deepcopy(netscaler_common_arguments)

    # Delete common arguments irrelevant to this module
    del argument_spec['state']
    del argument_spec['save_config']

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=False,
    )

    module_result = dict(
        changed=False,
        failed=False,
        loglines=loglines,
    )

    # Fail the module if imports failed
    if not PYTHON_SDK_IMPORTED:
        module.fail_json(msg='Could not load nitro python sdk')

    # Fallthrough to rest of execution
    client = get_nitro_client(module)

    if not module.params['mas_proxy_call']:
        try:
            client.login()
        except nitro_exception as e:
            msg = "nitro exception during login. errorcode=%s, message=%s" % (str(e.errorcode), e.message)
            module.fail_json(msg=msg)
        except Exception as e:
            if str(type(e)) == "<class 'requests.exceptions.ConnectionError'>":
                module.fail_json(msg='Connection error %s' % str(e))
            elif str(type(e)) == "<class 'requests.exceptions.SSLError'>":
                module.fail_json(msg='SSL Error %s' % str(e))
            else:
                module.fail_json(msg='Unexpected error during login %s' % str(e))

    try:
        log('Saving configuration')
        client.save_config()
    except nitro_exception as e:
        msg = "nitro exception errorcode=" + str(e.errorcode) + ",message=" + e.message
        module.fail_json(msg=msg, **module_result)

    if not module.params['mas_proxy_call']:
        client.logout()

    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
