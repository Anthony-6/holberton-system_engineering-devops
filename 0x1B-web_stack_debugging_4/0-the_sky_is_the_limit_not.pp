# upgrade the ulimit
exec { 'unlimited poweeer':
  command => 'sed -i "s/ULIMIT.*/ULIMIT=\"-n 4096\"/" /etc/default/nginx; sudo \
service nginx restart',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
