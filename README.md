# Automate-AAP2

Demo Content - Automate your automation!

A fully automated Ansible Automation Platform using infrastructure as code (IAC) practices.

## Context

Installing Ansible Automation Platform (day 1) is easy.

Configuring Ansible Automation Platform (day 2) is also easy.

It's so easy it's tempting to get started fast and to create jobs and all kind of objects manually by clicking in the web interface.

But as your automation footprint grows, the few clicks become a large amount of clicks. You might also end up wondering if a job is still really needed or not. Who owns it anyway?

As any platform you need governance (who can do what and when):

- a solid RBAC model (which AAP has)
- a scalable and flexible platform (which AAP is)
- AUTOMATION

That's right, you need to automate your automation platform! Let's embrace infrastructure as code and all its benefits (source control versioning, peer reviewing, etc.).

## Demo Content

In this demo, we will use simple Ansible playbooks taking advantage of the `Ansible Controller` collection to automate your day 2 operations:

- create a new organization
- create a project
- create an inventory containing one RHEL machine
- create SSH credentials to manage your RHEL machine (password is stored in vault under `root_password`)
- create three jobs
- create a workflow including those jobs with a decision tree (success/fail)
- launch the workflow
- launch an individual job

Now that you are doing infrastructure as code, in case of disaster, you might not even need to restore any backup. You just need to re-run those playbooks to rebuild your infrastructure!

## Day 2 operations

We assume Ansible Automation Platform is already installed. You will need its hostname, a user with admin access and its password.

### Clone this repository

```bash
git clone https://github.com/sebw/Automate-AAP2
cd Automate-AAP2
```

### Create your vault containing your secrets

```bash
ansible-vault create vault.yml
```

### Vault structure must look like this, adjust with your values

```yaml
aap2_host: my.aap2.example.com
aap2_username: your-user
aap2_password: your-password

root_password: your_machine_password
```

### Store your vault password in a file

```bash
echo "my_complex_vault_password" > vault-password.txt
```

Comment `vault_password_file` in `ansible.cfg` if you don't want to store your vault password in a file.

### Now edit the variable file

```bash
vim vars.yml
```

### Fire up your playbooks

```
for i in $(ls -1 0*.yml); do ansible-playbook $i; done
```

The order of execution of playbooks is important, this is the reason why they are stored numerically. For example, a job can't be created if the organization doesn't exist.

### Browse Ansible Automation Platform and find all objects

- organization
- project
- inventory
- credential
- jobs
- workflow

If you check under "Jobs" you should see a workflow and related jobs running.

## Simulate a disaster and recover from it

Want to simulate a disaster? 🧨

### Just run

```bash
ansible-playbook 99-destroy.yml
```

### Then re-run

```bash
for i in $(ls -1 0*.yml); do ansible-playbook $i; done
```

We are back in business in under a minute!


## Compatibility

Tested against Ansible Automation Platform 

- 2.0.0
- 2.0.1
- 2.2.0

Playbooks tested from 

- Fedora 35 with Ansible 2.9.27
- Fedora 36 with Ansible 2.12.10

## Want a live demo from your Red Hat account team?

Reach out to me at <swains@redhat.com>!
