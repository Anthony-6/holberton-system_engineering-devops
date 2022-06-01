# fix 500 error
exec {'fix error 500':
path    =>  ['/bin/', '/usr/bin/', '/user/sbin/'],
command =>   'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
}
