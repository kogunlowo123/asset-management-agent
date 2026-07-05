#!/bin/bash
set -euo pipefail
echo "Setting up Asset Management Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
