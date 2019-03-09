#!/usr/bin/env bash

cd "$(dirname "$0")"

REPO=algol2302

echo "Pushing build project into repo ${REPO}..."

for var in "$@"
do
    echo "Push $var..."
    docker push ${REPO}/defop-$var
    docker push ${REPO}/defop-$var:latest
done

echo "Complete!"
