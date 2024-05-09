> :warning::rotating_light: This project is no longer maintained and has been archived.

# Ansible Role: openjdk8

Role to install (_by default_) [openjdk-8-jdk](https://openjdk.java.net/) package for Debian based systems and `java-1.8.0-openjdk-devel` for EL systems or uninstall (_if passed as var_) on **Debian** based and **EL** based systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
openjdk8_app_debian: openjdk-8-jdk
openjdk8_app_el: java-1.8.0-openjdk-devel
openjdk8_desired_state: present
```

### Variables table:

Variable               | Description
---------------------- | --------------------------------------------------------------------------------------------------------
openjdk8_app_debian    | Defines the app to install on Debian based systems i.e. **openjdk-8-jdk**
openjdk8_app_el        | Defines the app to install on Enterprise Linux (Redhat/CentOS) systems i.e. **java-1.8.0-openjdk-devel**
openjdk8_desired_state |                                                                                                          | Defined to dynamically select whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default set to `present`.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **openjdk8** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.openjdk8
```

For customizing behavior of role (i.e. installation of latest **openjdk8** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.openjdk8
  vars:
    openjdk8_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **openjdk8** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.openjdk8
  vars:
    openjdk8_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-openjdk8/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
