#! /bin/bash
ansible-playbook -i hosts site.yml -vvvv --extra-vars "ansible_user=`whoami`" $@
