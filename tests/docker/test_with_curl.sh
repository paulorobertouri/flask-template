#!/usr/bin/env bash
set -euo pipefail

IMAGE="flask-template-e2e"
CONTAINER="flask-template-e2e-container"

cleanup() {
  docker rm -f "$CONTAINER" >/dev/null 2>&1 || true
}
trap cleanup EXIT

docker build -f docker/build.Dockerfile -t "$IMAGE" .
docker run -d --name "$CONTAINER" -p 38080:8000 "$IMAGE"
sleep 3

curl -fsS http://127.0.0.1:38080/apidocs/ >/dev/null
curl -fsS http://127.0.0.1:38080/v1/customer >/dev/null

RAW_HEADERS=$(curl -isS http://127.0.0.1:38080/v1/auth/login)
if ! echo "$RAW_HEADERS" | grep -iq '^x-jwt-token:'; then
  echo "X-JWT-Token header was not returned"
  exit 1
fi

TOKEN=$(curl -fsS http://127.0.0.1:38080/v1/auth/login | python3 -c 'import json,sys; print(json.load(sys.stdin)["token"])')

curl -fsS -H "Authorization: Bearer ${TOKEN}" http://127.0.0.1:38080/v1/private >/dev/null
