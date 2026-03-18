#!/bin/bash

# Run as a sudo user
echo "Setting up environment and installing packages..."

sudo apt update -y && sudo apt upgrade -y
sudo apt install -y python3-venv

echo "Finished..."
