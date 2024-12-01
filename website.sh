nano /var/www/html/CI-CD_Pipeline/Website.sh


#!/bin/bash

REPO_DIR="/var/www/html/CI-CD_Pipeline"  # Your Git repository
WEBSITE_DIR="/var/www/html/CI-CD_Pipeline"  # Nginx root directory


# Pull the latest changes from GitHub
cd $REPO_DIR || exit
git pull origin main

# Sync the files to the Nginx website directory
rsync -av --delete "$REPO_DIR/" "$WEBSITE_DIR/"

# Restart Nginx to serve the updated content
sudo systemctl restart nginx

echo "Website updated successfully."
