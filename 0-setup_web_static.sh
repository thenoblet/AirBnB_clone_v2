#!/usr/bin/env bash
# This script configures web servers for deployment

# Install Nginx if not already installed
if ! [ -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create a fake HTML file for testing
sudo echo "<html>
    <head>
        <title>Test Page</title>
    </head>
    <body>
        <h1>This is a test page for web_static deployment</h1>
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link and set ownership
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config="server {
    server_name _;

    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}"

# Remove default configuration and add new one
sudo rm -f /etc/nginx/sites-enabled/default
sudo echo "$config" | sudo tee /etc/nginx/sites-available/hbnb_static
sudo ln -sf /etc/nginx/sites-available/hbnb_static /etc/nginx/sites-enabled/

# Restart Nginx to apply changes
service nginx restart

