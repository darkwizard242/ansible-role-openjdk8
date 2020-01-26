import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_openjdk8_package_installed(host):
    assert host.package("openjdk-8-jdk").is_installed or \
      host.package("java-1.8.0-openjdk").is_installed


def test_openjdk8_binary_exists(host):
    assert host.file('/usr/bin/java').exists


def test_openjdk8_binary_which(host):
    assert host.check_output('which java') == '/usr/bin/java'
