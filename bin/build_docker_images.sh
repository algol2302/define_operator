#!/usr/bin/env bash

cd "$(dirname "$0")"

REPO=docker.sysols.ru/isku
VERSION=`git rev-parse --short HEAD`

echo "Starting build project..."

for var in "$@"
do
    echo "Build $var..."
    docker build -t ${REPO}/$var:$VERSION -t ${REPO}/$var:latest -f ../docker/$var/Dockerfile ..
done

echo "Complete!"
