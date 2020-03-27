# Amtega gitlab_clean role

This is an [Ansible](http://www.ansible.com) role to cleanup GitLab projects forks and merge requests.

## Role Variables

A list of all the default variables for this role is available in `defaults/main.yml`.

## Example Playbook

This is an example playbook:

``` yaml
---
- name: Get GitLab projects fact
  hosts: localhost
  roles:  
    - amtega.gitlab_cleanup
  vars:    
    gitlab_clean_server: https://gitlab.acme.com
    gitlab_clean_api_version: 4
    gitlab_clean_token: mytoken
    gitlab_clean_forks: yes
    gitlab_clean_owned_projects: yes
    gitlab_clean_forks_name_regex: .*
    gitlab_clean_forks_created_seconds_ago: 0
    gitlab_clean_forks_last_activity_seconds_ago: 60
    gitlab_clean_mr: yes
    gitlab_clean_mr_scope: created_by_me
    gitlab_clean_mr_author_username_regex: .*
    gitlab_clean_mr_title_regex: .*
    gitlab_clean_mr_created_seconds_ago: 360
    gitlab_clean_mr_updated_at_seconds_ago: 360
    gitlab_clean_validate_certs: no    
```

## Testing

Tests are based on docker containers. You can setup docker engine quickly using the playbook `files/setup.yml` available in the role [amtega.docker_engine](https://galaxy.ansible.com/amtega/docker_engine).

To run test you need provide the variables defined in `defaults/main.yml`. One way to provide this information is calling the testing playbook passing an additional plus the default one provided for testing, as it's show in this example:

```shell
$ cd amtega.gitlab_clean/tests
$ ansible-playbook main.yml -i inventory -i ~/mycustominventory.yml --vault-id myvault@prompt
```

## License

Copyright (C) 2020 AMTEGA - Xunta de Galicia

This role is free software: you can redistribute it and/or modify it under the terms of:

GNU General Public License version 3, or (at your option) any later version; or the European Union Public License, either Version 1.2 or – as soon they will be approved by the European Commission ­subsequent versions of the EUPL.

This role is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details or European Union Public License for more details.

## Author Information

- Juan Antonio Valiño García.
