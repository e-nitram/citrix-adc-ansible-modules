========================
Citrix.Adc Release Notes
========================

.. contents:: Topics


v1.3.0
======

v1.1.0
======

Major Changes
-------------

- Add diff mode for the following modules
  citrix_adc_cs_vserver
  citrix_adc_lb_vserver
  citrix_adc_nitro_resource
  citrix_adc_server
  citrix_adc_service
  citrix_adc_servicegroup
- Add mas_proxy_call option in citrix_adc_nitro_request
- Update citrix_adc_service module to use NITRO API directly. Also update arguments to current NITRO API version.

Minor Changes
-------------

- Patch citrix_adc_nitro_resource object workflow to return no exists for a resource if the endpoint is not on the returned object

Bugfixes
--------

- Fix debug message failing in citrix_adc_nitro_resource

New Modules
-----------

- citrix.adc.citrix_adc_dnsnsrec - Configuration for name server record resource.
- citrix.adc.citrix_adc_nitro_info - Retrieve information from various NITRO API endpoints
- citrix.adc.citrix_adc_sslcipher - Manage custom SSL ciphers
- citrix.adc.citrix_adc_sslcipher_sslciphersuite_binding - Manage SSL cipher and SSL ciphersuite bindings
- citrix.adc.citrix_adc_sslprofile_sslcipher_binding - Manage SSL profile and SSL cipher bindings
- citrix.adc.citrix_adc_system_file - Upload systemfile to ADC

v1.0.0
======

New Plugins
-----------

Connection
~~~~~~~~~~

- citrix.adc.ssh_citrix_adc - connect via ssh client binary with Citrix ADC bypassing the cli

New Modules
-----------

- citrix.adc.citrix_adc_appfw_confidfield - Configuration for configured confidential form fields resource.
- citrix.adc.citrix_adc_appfw_fieldtype - Configuration for application firewall form field type resource.
- citrix.adc.citrix_adc_appfw_global_bindings - Define global bindings for AppFW
- citrix.adc.citrix_adc_appfw_htmlerrorpage - Configuration for configured confidential form fields resource.
- citrix.adc.citrix_adc_appfw_jsoncontenttype - Configuration for JSON content type resource.
- citrix.adc.citrix_adc_appfw_learningsettings - Configuration for learning settings resource.
- citrix.adc.citrix_adc_appfw_policy - Manage Citrix ADC Web Application Firewall policies.
- citrix.adc.citrix_adc_appfw_policylabel - Manage Citrix ADC Web Application Firewall policy labels.
- citrix.adc.citrix_adc_appfw_profile - Manage Citrix ADC Web Application Firewall profiles.
- citrix.adc.citrix_adc_appfw_settings - Manage Citrix ADC Web Application Firewall settings.
- citrix.adc.citrix_adc_appfw_signatures - Configuration for configured confidential form fields resource.
- citrix.adc.citrix_adc_appfw_wsdl - Configuration for configured confidential form fields resource.
- citrix.adc.citrix_adc_appfw_xmlcontenttype - Configuration for XML Content type resource.
- citrix.adc.citrix_adc_appfw_xmlerrorpage - Configuration for configured confidential form fields resource.
- citrix.adc.citrix_adc_appfw_xmlschema - Configuration for configured confidential form fields resource.
- citrix.adc.citrix_adc_cs_action - Manage content switching actions
- citrix.adc.citrix_adc_cs_policy - Manage content switching policy
- citrix.adc.citrix_adc_cs_vserver - Manage content switching vserver
- citrix.adc.citrix_adc_gslb_service - Manage GSLB services
- citrix.adc.citrix_adc_gslb_site - Manage gslb site entities in Citrix ADC.
- citrix.adc.citrix_adc_gslb_vserver - Configure gslb vserver entities in Citrix ADC.
- citrix.adc.citrix_adc_lb_monitor - Manage load balancing monitors
- citrix.adc.citrix_adc_lb_vserver - Manage load balancing vserver configuration
- citrix.adc.citrix_adc_nitro_request - Issue Nitro API requests to a Citrix ADC instance.
- citrix.adc.citrix_adc_nitro_resource - Manage NITRO resources
- citrix.adc.citrix_adc_password_reset - Perform default password reset.
- citrix.adc.citrix_adc_save_config - Save Citrix ADC configuration.
- citrix.adc.citrix_adc_server - Manage server configuration
- citrix.adc.citrix_adc_service - Manage service configuration in Citrix ADC
- citrix.adc.citrix_adc_servicegroup - Manage service group configuration in Citrix ADC
- citrix.adc.citrix_adc_ssl_certkey - Manage ssl cerificate keys.
