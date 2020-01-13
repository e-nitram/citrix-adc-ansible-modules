class ModuleDocFragment(object):
    DOCUMENTATION = '''

options:
    nsip:
        description:
            - The ip address of the netscaler appliance where the nitro API calls will be made.
            - "The port can be specified with the colon (:). E.g. 192.168.1.1:555."
        aliases:
            - mas_ip
        required: True

    nitro_user:
        description:
            - The username with which to authenticate to the netscaler node.
        required: False
        aliases:
            - mas_user

    nitro_pass:
        description:
            - The password with which to authenticate to the netscaler node.
        required: False
        aliases:
            - mas_pass

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

    state:
        choices: ['present', 'absent']
        default: 'present'
        description:
            - The state of the resource being configured by the module on the netscaler node.
            - When present the resource will be created if needed and configured according to the module's parameters.
            - When absent the resource will be deleted from the netscaler node.

    save_config:
        description:
            - If true the module will save the configuration on the netscaler node if it makes any changes.
            - The module will not save the configuration on the netscaler node if it made no changes.
        type: bool
        default: true

    mas_proxy_call:
        description:
            - If true the underlying NITRO API calls made by the module will be proxied through a MAS node to the target Netscaler instance.
            - "When true you must also define the following options: I(nitro_auth_token), I(instance_ip)."
        type: bool
        default: false
        version_added: "2.6.0"

    nitro_auth_token:
        description:
            - The authentication token provided by a login operation.
        aliases:
            - mas_auth_token
        version_added: "2.6.0"

    instance_ip:
        description:
            - The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.
            - It is meaningful only when having set C(mas_proxy_call) to C(true)
        version_added: "2.6.0"
notes:
  - For more information on using Ansible to manage Citrix NetScaler Network devices see U(https://www.ansible.com/ansible-netscaler).
'''
