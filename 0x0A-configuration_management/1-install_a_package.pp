# this script install a package
exec { 'gem install puppet-lint -v 2.5.0':
  path => 'usr/bin'
}
