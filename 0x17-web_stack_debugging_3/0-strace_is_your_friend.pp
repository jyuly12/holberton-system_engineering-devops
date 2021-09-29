# Find the issue, fix it and then automate it using Puppet
exec { 'fixed-program':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/bin';
  }