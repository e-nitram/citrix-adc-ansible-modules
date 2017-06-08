#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2017 Citrix Systems
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'commiter',
                    'version': '1.0'}


DOCUMENTATION = '''
---
module: netscaler_server
short_description: Manage server configuration
description:
    - This module uncoditionally saves the configuration on the target netscaler node.
    - This module does not support check mode.
    - This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.

version_added: "2.4.0"

options:
    nsip:
        description:
            - The ip address of the netscaler appliance where the nitro API calls will be made.
            - "The port can be specified with the colon (:). E.g. 192.168.1.1:555."
        required: True

    nitro_user:
        description:
            - The username with which to authenticate to the netscaler node.
        required: True

    nitro_pass:
        description:
            - The password with which to authenticate to the netscaler node.
        required: True

    nitro_protocol:
        choices: [ 'http', 'https' ]
        default: http
        description:
            - Which protocol to use when accessing the nitro API objects.

    validate_certs:
        description:
            - If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
        required: false
        default: 'yes'

    nitro_timeout:
        description:
            - Time in seconds until a timeout error is thrown when establishing a new session with Netscaler
        default: 310

requirements:
    - nitro python sdk
'''

EXAMPLES = '''
- name: Save netscaler configuration
    delegate_to: localhost
    netscaler_save_config:
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

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.netscaler import get_nitro_client, log, loglines, netscaler_common_arguments

try:
    from nssrc.com.citrix.netscaler.nitro.exception.nitro_exception import nitro_exception
    PYTHON_SDK_IMPORTED = True
except ImportError as e:
    PYTHON_SDK_IMPORTED = False


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

    client.logout()
    module.exit_json(**module_result)


if __name__ == "__main__":
    main()
