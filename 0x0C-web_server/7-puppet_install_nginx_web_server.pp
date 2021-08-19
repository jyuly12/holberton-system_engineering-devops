# Install and configure the web server

exec {'Update and Upgrade':
  command => 'sudo apt-get -y update; sudo apt-get -y upgrade;' 
}
package {'nginx':
  ensure  => 'installed'
}
service {'start nginx':
  ensure  => running,
  require => Package['nginx'],
}
file {'/var/www/html/index.html':
  content => 'Holberton School',
}
file_line { 'Add redirection, 301':
  path   => '/etc/nginx/sites-available/default',
  ensure => 'present',
  after  => 'listen 80 default_server',
  line   => 'rewrite ^/redirect_me https://github.com/jyuly12 permanent;'
}

