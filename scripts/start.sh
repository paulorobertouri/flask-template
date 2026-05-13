#!/usr/bin/env bash
set -euo pipefail
echo "Starting Flask services..."
docker compose up -d
sleep 5
curl -f http://localhost:8000/health && echo "Healthy!" || echo "Check failed."
