# Automate-AAP2

Demo Content - Automate your automation!

A fully automated Ansible Automation Platform.

## Context

Installing and configuring Ansible Automation Platform is an easy process.

You might be tempted to start configuring Ansible Controller (the new name of Ansible Tower!) manually, because it's just a few clicks in a web interface.

As your automation footprint grows, the few clicks become a large amount of clicks.

So, instead, why not automate your automation?

## Vault variables

Some variables are located in the encrypted `vault.yml`.

If you want to pass your own variables, your vault should look like this:

```
aap2_host: my.aap2.example.com
aap2_username: your-user
aap2_password: your-password
```

## Demo Content

In this demo, we will use Ansible playbooks to automate your day 2 operations:

- create a new organization
- create a project using a Github repository
- create an inventory containing a host
- create SSH credentials to manage the host (for the sake of the demo, we intentionally didn't vault the password!)
- create a job
- launch the job

With this, you are fully embracing infrastructure as code practices.

In case of disaster, you might not even need to restore backups. You just need to rerun those playbooks.

Want to simulate a disaster? 🧨 Just run `99-destroy.yml` and rerun all the playbooks in order.

You're back in business in a few minutes!

## Compatibility

Tested against Ansible Automation Platform 2.0

Playbooks executed from a Fedora 35 workstation with Ansible 2.9.27.

## Want a live demo from your Red Hat account team?

Reach out to me at <swains@redhat.com>!
