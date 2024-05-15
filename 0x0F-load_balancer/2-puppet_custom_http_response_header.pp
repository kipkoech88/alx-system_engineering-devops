# install and configure nginx
exec { 'command':
     command => 'apt -y update;
     apt-get -y install nginx;
     sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
     service nginx restart;'
     provider => shell
     }
