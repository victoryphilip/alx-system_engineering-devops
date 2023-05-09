# Fourth web-stack debug script in puppet
exec { 'wsd3':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/' /var/www/html/wp-settings.php",
  path    =>  ['/bin', '/usr/bin']
}
