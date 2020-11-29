import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_DEBIAN = 'openjdk-8-jdk'
PACKAGE_EL = 'java-1.8.0-openjdk'
PACKAGE_BINARY = '/usr/bin/java'


def test_openjdk8_package_installed(host):
    """
    Tests if openjdk is installed on DEBIAN/EL systems.
    """
    assert host.package(PACKAGE_DEBIAN).is_installed or \
        host.package(PACKAGE_EL).is_installed


def test_openjdk8_binary_exists(host):
    """
    Tests if openjdk binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_openjdk8_binary_which(host):
    """
    Tests the output to confirm openjdk's binary location.
    """
    assert host.check_output('which java') == PACKAGE_BINARY
