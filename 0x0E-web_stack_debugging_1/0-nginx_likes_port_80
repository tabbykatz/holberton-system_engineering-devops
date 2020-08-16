#!/usr/bin/env bash
# change nginx server to listen on port 80 and restart

sed -i "s/8080/80/g" /etc/nginx/sites-enabled/default
service nginx restart
