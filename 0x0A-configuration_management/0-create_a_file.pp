#creating a file with the following properties
file {
    '/tmp/school':
    content => "I love Puppet\n",
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0644',
    path    => '/tmp/school',
}