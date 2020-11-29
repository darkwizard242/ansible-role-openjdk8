[![build-test](https://github.com/darkwizard242/ansible-role-openjdk8/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-openjdk8/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-openjdk8/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-openjdk8/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/43263?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/43263?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/43263?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-openjdk8&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-openjdk8) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-openjdk8&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-openjdk8) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-openjdk8&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-openjdk8) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-openjdk8&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-openjdk8) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-openjdk8?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-openjdk8?color=orange&style=flat-square)

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

Variable               | Value (default)          | Description
---------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------
openjdk8_app_debian    | openjdk-8-jdk            | Defines the app to install on Debian based systems i.e. **openjdk-8-jdk**
openjdk8_app_el        | java-1.8.0-openjdk-devel | Defines the app to install on Enterprise Linux (Redhat/CentOS) systems i.e. **java-1.8.0-openjdk-devel**
openjdk8_desired_state | present                  | Defined to dynamically select whether to install (i.e. either `present` or `latest`) or uninstall (i.e. `absent`) the package. Default set to `present`.

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

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
