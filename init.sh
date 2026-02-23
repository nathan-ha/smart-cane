#!/bin/bash

echo "Setting up environment and installing packages..."

python3 -m venv --system-site-packages test_venv

source test_venv/bin/activate

pip install -r requirements.txt --no-cache-dir --only-binary :all:

deactivate

echo "Finished..."
