# Install and configure the web server

exec {'Update and Upgrade':
  command => 'sudo apt-get -y update; sudo apt-get -y upgrade' 
}
package {'nginx':
  ensure  => 'installed',
  require => Exec['update packages']
}
exec { 'permissions':
  command => 'sudo ufw allow "Nginx HTTP"'
}
service {'Start nginx':
  ensure  => running,
  require => Package['nginx'],
}
file {'/var/www/html/index.html':
  content => 'Holberton School',
}
exec {'Set redirection':
  command => 'sed -i "/listen 80 default_server;/a rewrite ^/redirect_me https://github.com/jyuly12 permanent;" /etc/nginx/sites-available/default'
}

