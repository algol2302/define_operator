#!/usr/bin/env bash

cd "$(dirname "$0")"

REPO=algol2302

echo "Starting build project..."

for var in "$@"
do
    echo "Build $var..."
    docker build -t ${REPO}/defop-$var -t ${REPO}/def-$var:latest -f ../docker/$var/Dockerfile ..
done

echo "Complete!"
