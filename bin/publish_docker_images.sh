#!/usr/bin/env bash

cd "$(dirname "$0")"

REPO=docker.sysols.ru/isku
VERSION=`git rev-parse --short HEAD`

echo "Pushing build project into repo ${REPO}..."

for var in "$@"
do
    echo "Push $var..."
    docker push ${REPO}/$var:$VERSION
    docker push ${REPO}/$var:latest
done

echo "Complete!"
