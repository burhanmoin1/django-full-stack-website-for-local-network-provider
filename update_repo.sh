#!/bin/bash

# Change to your repository directory
cd C:/Users/XC/OneDrive/Documents/delta customer app/customercare

# Pull changes from the remote repository
git pull origin main

# Add and commit changes (replace with appropriate paths)
git add .
git commit -m "Auto-update $(date +'%Y-%m-%d %H:%M:%S')"

# Push changes to the remote repository
git push origin main