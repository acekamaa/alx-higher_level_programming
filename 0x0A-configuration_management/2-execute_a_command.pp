#!/usr/bin/pup
#killing a process
exec { 'kill_killmenow_process':
  command => 'pkill -f killmenow',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'pgrep -f killmenow',
}