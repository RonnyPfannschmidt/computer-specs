#!/bin/bash
(
  . ./quickstart-ansible.bash
  set +e
  ansible-playbook "${@}" -i inventory/local.ini
  set -e
)
