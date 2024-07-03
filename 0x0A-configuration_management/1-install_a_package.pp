#!/usr/bin/pup
#InstallFlask
class InstallFlask {
  include puppet::stdlib

  $flask_version = '2.1.0'

  package { 'flask':
    ensure => $flask_version,
    provider => Puppet::Provider::Package['pip3'],
    source => "pypi",
    options => "--no-cache-dir"
  }
}