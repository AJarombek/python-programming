### Overview

Working with [Mojo](https://docs.modular.com/mojo/), a new programming language which is a superset of Python.

### Commands

*Running the Vagrant VM Locally*

Mojo currently only works on Ubuntu.  To run Mojo locally on macOS, you need to install Vagrant and VirtualBox, 
and run the following commands.

```bash
# Install Vagrant
brew install hashicorp/tap/hashicorp-vagrant
vagrant --version

# Install VirtualBox
# https://www.virtualbox.org/wiki/Downloads

# Start the Vagrant VM
vagrant up

# Reload a Vagrant VM with latest Vagrantfile changes
vagrant reload
```
