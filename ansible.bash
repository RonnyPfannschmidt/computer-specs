#!/bin/bash
exec .env/bin/ansible-playbook "${@}" -i inventory/local.ini
