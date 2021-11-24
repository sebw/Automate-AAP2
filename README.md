# Automate-AAP2

Demo Content - Automate your automation!

A fully automated Ansible Automation Platform.

## Context

Installing and configuring Ansible Automation Platform is an easy process.

You might be tempted to start configuring Ansible Controller (the new name of Ansible Tower!) manually, because it's just a few clicks in a web interface.

As your automation footprint grows, the few clicks become a large amount of clicks.

So why not automate your automation?

## Demo Content

In this demo, we will use simple Ansible playbooks taking advantage of the `Ansible Controller` collection to automate your day 2 operations:

- create a new organization
- create a project
- create an inventory containing one RHEL machine
- create SSH credentials to manage your RHEL machine (for the sake of the demo, we intentionally didn't vault the password!)
- create a job
- launch the job

With this, you are fully embracing infrastructure as code practices.

In case of disaster, you might not even need to restore backups. You just need to rerun those playbooks.

## Day 2 operation

We assume Ansible Automation Platform is already installed. You will need the hostname, a user with admin access and its password.

```bash
git clone https://github.com/RedHatBelux/Automate-AAP2
cd Automate-AAP2
ansible-vault create vault.yml (fill in your AAP details in there, see below for sample)
vim vars.yml
for i in $(ls -1 *.yml); do ansible-playbook $i; done
```

`ansible.cfg` is configured to check the vault password in a `vault-password.txt` file. Update your configuration or command accordingly.

When finished you will find your org, project, inventory, credential, job and a job should be already running.

## Simulate a disaster and recover from it

Want to simulate a disaster? 🧨

Just run:

```bash
ansible-playbook 99-destroy.yaml
```

Then rerun:

```bash
for i in $(ls -1 *.yml); do ansible-playbook -i $i; done
```

You're back in business in a few minutes!

## Vault variables

Some variables are located in the encrypted `vault.yml`.

If you want to pass your own variables, delete the existing `vault.yml` and recreate one using `ansible-vault create vault.yml`.

Your vault structure should look like this:

```yaml
aap2_host: my.aap2.example.com
aap2_username: your-user
aap2_password: your-password
```

## Compatibility

Tested against Ansible Automation Platform 2.0.0 and 2.0.1.

Playbooks executed from a Fedora 35 workstation with Ansible 2.9.27.

## Want a live demo from your Red Hat account team?

Reach out to me at <swains@redhat.com>!
