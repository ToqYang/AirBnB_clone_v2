#!/usr/bin/env bash
# Prepare your web servers

sudo apt-get -y update
sudo apt-get -y install nginx
sudo service nginx start
sudo ufw allow 'Nginx HTTP'
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared 
echo "Hello holberton" | tee -a /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu -R /data/
sudo sed -i "48a\\\n\tlocation hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available
sudo service nginx restart
exit 0
