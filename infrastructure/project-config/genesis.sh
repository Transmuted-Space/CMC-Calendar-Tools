#!/bin/sh
set -e

./enable-services.sh
./create-containers.sh --commit
./create-deployments.sh --preview
./create-deployments.sh --commit
