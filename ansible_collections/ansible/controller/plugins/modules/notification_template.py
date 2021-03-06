#!/usr/bin/python
# coding: utf-8 -*-

# (c) 2018, Samuel Carpentier <samuelcarpentier0@gmail.ca>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ['preview'], 'supported_by': 'community'}


DOCUMENTATION = '''
---
module: notification_template
author: "Samuel Carpentier (@samcarpentier)"
short_description: create, update, or destroy Automation Platform Controller notification.
description:
    - Create, update, or destroy Automation Platform Controller notifications. See
      U(https://www.ansible.com/tower) for an overview.
options:
    name:
      description:
        - The name of the notification.
      type: str
      required: True
    new_name:
      description:
        - Setting this option will change the existing name (looked up via the name field.
      type: str
    copy_from:
      description:
        - Name or id to copy the notification from.
        - This will copy an existing notification and change any parameters supplied.
        - The new notification name will be the one provided in the name parameter.
        - The organization parameter is not used in this, to facilitate copy from one organization to another.
        - Provide the id or use the lookup plugin to provide the id if multiple notifications share the same name.
      type: str
    description:
      description:
        - The description of the notification.
      type: str
    organization:
      description:
        - The organization the notification belongs to.
      type: str
    notification_type:
      description:
        - The type of notification to be sent.
      choices:
        - 'email'
        - 'grafana'
        - 'irc'
        - 'mattermost'
        - 'pagerduty'
        - 'rocketchat'
        - 'slack'
        - 'twilio'
        - 'webhook'
      type: str
    notification_configuration:
      description:
        - The notification configuration file. Note providing this field would disable all notification-configuration-related fields.
      type: dict
    messages:
      description:
        - Optional custom messages for notification template.
      type: dict
    username:
      description:
        - The mail server username.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    sender:
      description:
        - The sender email address.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    recipients:
      description:
        - The recipients email addresses.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: list
      elements: str
    use_tls:
      description:
        - The TLS trigger.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: bool
    host:
      description:
        - The mail server host.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    use_ssl:
      description:
        - The SSL trigger.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: bool
    password:
      description:
        - The mail server password.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    port:
      description:
        - The mail server port.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: int
    channels:
      description:
        - The destination Slack channels.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: list
      elements: str
    token:
      description:
        - The access token.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    account_token:
      description:
        - The Twillio account token.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    from_number:
      description:
        - The source phone number.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    to_numbers:
      description:
        - The destination phone numbers.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: list
      elements: str
    account_sid:
      description:
        - The Twillio account SID.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    subdomain:
      description:
        - The PagerDuty subdomain.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    service_key:
      description:
        - The PagerDuty service/integration API key.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    client_name:
      description:
        - The PagerDuty client identifier.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    message_from:
      description:
        - The label to be shown with the notification.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    color:
      description:
        - The notification color.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      choices: ["yellow", "green", "red", "purple", "gray", "random"]
      type: str
    notify:
      description:
        - The notify channel trigger.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: bool
    url:
      description:
        - The target URL.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    headers:
      description:
        - The HTTP headers as JSON string.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: dict
    server:
      description:
        - The IRC server address.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    nickname:
      description:
        - The IRC nickname.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: str
    targets:
      description:
        - The destination channels or users.
        - This parameter has been deprecated, please use 'notification_configuration' instead.
      type: list
      elements: str
    state:
      description:
        - Desired state of the resource.
      default: "present"
      choices: ["present", "absent"]
      type: str
extends_documentation_fragment: ansible.controller.auth
'''


EXAMPLES = '''
- name: Add Slack notification with custom messages
  notification_template:
    name: slack notification
    organization: Default
    notification_type: slack
    notification_configuration:
      channels:
        - general
      token: cefda9e2be1f21d11cdd9452f5b7f97fda977f42
    messages:
       started:
         message: "{{ '{{ job_friendly_name }}{{ job.id }} started' }}"
       success:
         message: "{{ '{{ job_friendly_name }} completed in {{ job.elapsed }} seconds' }}"
       error:
         message: "{{ '{{ job_friendly_name }} FAILED! Please look at {{ job.url }}' }}"
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add webhook notification
  notification_template:
    name: webhook notification
    notification_type: webhook
    notification_configuration:
      url: http://www.example.com/hook
      headers:
        X-Custom-Header: value123
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add email notification
  notification_template:
    name: email notification
    notification_type: email
    notification_configuration:
      username: user
      password: s3cr3t
      sender: controller@example.com
      recipients:
        - user1@example.com
      host: smtp.example.com
      port: 25
      use_tls: no
      use_ssl: no
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add twilio notification
  notification_template:
    name: twilio notification
    notification_type: twilio
    notification_configuration:
      account_token: a_token
      account_sid: a_sid
      from_number: '+15551112222'
      to_numbers:
        - '+15553334444'
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add PagerDuty notification
  notification_template:
    name: pagerduty notification
    notification_type: pagerduty
    notification_configuration:
      token: a_token
      subdomain: sub
      client_name: client
      service_key: a_key
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Add IRC notification
  notification_template:
    name: irc notification
    notification_type: irc
    notification_configuration:
      nickname: controller
      password: s3cr3t
      targets:
        - user1
      port: 8080
      server: irc.example.com
      use_ssl: no
    state: present
    controller_config_file: "~/tower_cli.cfg"

- name: Delete notification
  notification_template:
    name: old notification
    state: absent
    controller_config_file: "~/tower_cli.cfg"

- name: Copy webhook notification
  notification_template:
    name: foo notification
    copy_from: email notification
    organization: Foo
'''


RETURN = ''' # '''


from ..module_utils.controller_api import ControllerAPIModule

OLD_INPUT_NAMES = (
    'username',
    'sender',
    'recipients',
    'use_tls',
    'host',
    'use_ssl',
    'password',
    'port',
    'channels',
    'token',
    'account_token',
    'from_number',
    'to_numbers',
    'account_sid',
    'subdomain',
    'service_key',
    'client_name',
    'message_from',
    'color',
    'notify',
    'url',
    'headers',
    'server',
    'nickname',
    'targets',
)


def main():
    # Any additional arguments that are not fields of the item can be added here
    argument_spec = dict(
        name=dict(required=True),
        new_name=dict(),
        copy_from=dict(),
        description=dict(),
        organization=dict(),
        notification_type=dict(choices=['email', 'grafana', 'irc', 'mattermost', 'pagerduty', 'rocketchat', 'slack', 'twilio', 'webhook']),
        notification_configuration=dict(type='dict'),
        messages=dict(type='dict'),
        username=dict(),
        sender=dict(),
        recipients=dict(type='list', elements='str'),
        use_tls=dict(type='bool'),
        host=dict(),
        use_ssl=dict(type='bool'),
        password=dict(no_log=True),
        port=dict(type='int'),
        channels=dict(type='list', elements='str'),
        token=dict(no_log=True),
        account_token=dict(no_log=True),
        from_number=dict(),
        to_numbers=dict(type='list', elements='str'),
        account_sid=dict(),
        subdomain=dict(),
        service_key=dict(no_log=True),
        client_name=dict(),
        message_from=dict(),
        color=dict(choices=['yellow', 'green', 'red', 'purple', 'gray', 'random']),
        notify=dict(type='bool'),
        url=dict(),
        headers=dict(type='dict'),
        server=dict(),
        nickname=dict(),
        targets=dict(type='list', elements='str'),
        state=dict(choices=['present', 'absent'], default='present'),
    )

    # Create a module for ourselves
    module = ControllerAPIModule(argument_spec=argument_spec)

    # Extract our parameters
    name = module.params.get('name')
    new_name = module.params.get('new_name')
    copy_from = module.params.get('copy_from')
    description = module.params.get('description')
    organization = module.params.get('organization')
    notification_type = module.params.get('notification_type')
    notification_configuration = module.params.get('notification_configuration')
    messages = module.params.get('messages')
    state = module.params.get('state')

    # Deprecation warnings for all other params
    for legacy_input in OLD_INPUT_NAMES:
        if module.params.get(legacy_input) is not None:
            module.deprecate(
                collection_name="awx.awx",
                msg='{0} parameter has been deprecated, please use notification_configuration instead'.format(legacy_input),
                version="4.0.0"
            )

    # Attempt to look up the related items the user specified (these will fail the module if not found)
    organization_id = None
    if organization:
        organization_id = module.resolve_name_to_id('organizations', organization)

    # Attempt to look up an existing item based on the provided data
    existing_item = module.get_one(
        'notification_templates',
        name_or_id=name,
        **{
            'data': {
                'organization': organization_id,
            }
        }
    )

    # Attempt to look up credential to copy based on the provided name
    if copy_from:
        # a new existing item is formed when copying and is returned.
        existing_item = module.copy_item(
            existing_item,
            copy_from,
            name,
            endpoint='notification_templates',
            item_type='notification_template',
            copy_lookup_data={},
        )

    if state == 'absent':
        # If the state was absent we can let the module delete it if needed, the module will handle exiting from this
        module.delete_if_needed(existing_item)

    # Create notification_configuration from legacy inputs
    final_notification_configuration = {}
    for legacy_input in OLD_INPUT_NAMES:
        if module.params.get(legacy_input) is not None:
            final_notification_configuration[legacy_input] = module.params.get(legacy_input)
    # Give anything in notification_configuration prescedence over the individual inputs
    if notification_configuration is not None:
        final_notification_configuration.update(notification_configuration)

    # Create the data that gets sent for create and update
    new_fields = {}
    if final_notification_configuration:
        new_fields['notification_configuration'] = final_notification_configuration
    new_fields['name'] = new_name if new_name else (module.get_item_name(existing_item) if existing_item else name)
    if description is not None:
        new_fields['description'] = description
    if organization is not None:
        new_fields['organization'] = organization_id
    if notification_type is not None:
        new_fields['notification_type'] = notification_type
    if messages is not None:
        new_fields['messages'] = messages

    # If the state was present and we can let the module build or update the existing item, this will return on its own
    module.create_or_update_if_needed(existing_item, new_fields, endpoint='notification_templates', item_type='notification_template', associations={})


if __name__ == '__main__':
    main()
