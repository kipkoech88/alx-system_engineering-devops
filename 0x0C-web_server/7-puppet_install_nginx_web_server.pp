# configure server
package {'nginx':
	provider => 'apt',
	}
exec { 'home_page':
     command => sudo echo "Hello World!" > /var/www/html/index.nginx-debian.html,
     }
exec { 'redirect':
     command => sudo sed -i "66i rewrite ^/redirect_me https://www.youtube.com/ permanent;" > /etc/nginx/sites-available/default
     }
exec { 'start_server':
     command => /usr/bin/sudo /usr/bin/service nginx start,
     }