import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


OPENJDK8_BINARY_PATH = '/usr/bin/java'
OPENJDK8_PACKAGE_DEBIAN = 'openjdk-8-jdk'
OPENJDK8_PACKAGE_EL = 'java-1.8.0-openjdk'


def test_openjdk8_package_installed(host):
    host.package("OPENJDK8_PACKAGE_DEBIAN").is_installed or \
      host.package("OPENJDK8_PACKAGE_EL").is_installed


def test_openjdk8_binary_exists(host):
    host.file('OPENJDK8_BINARY_PATH').exists


def test_openjdk8_binary_file(host):
    host.file('OPENJDK8_BINARY_PATH').is_file


def test_openjdk8_binary_which(host):
    host.check_output('which java') == OPENJDK8_BINARY_PATH
