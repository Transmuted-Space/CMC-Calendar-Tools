#!/bin/sh
# SYNOPSIS: ./create-containers.sh [--dry-run|--commit]
#
# If --dry-run is specified or no option is given, the commands to be run will
# be emitted to the console, but no `gcloud` commands will actually be executed.
# If --commit is specified, containers will be created.
#
# This command does not do actual option parsing. Options other than the first
# parameter will not be recognized. There are no shorthands.
set -e

project_config_dir=$(dirname $(type -p ${0}))
containers_dir="${project_config_dir}/../containers"
project_id=$(gcloud config get-value project | sed -n 1p)

for container_dir in ${containers_dir}/*; do
  container_dir=${container_dir%*/}
  container=${container_dir##*/}
  echo "gcloud builds submit --tag gcr.io/${project_id}/${container}"
  if [ "${1}" == "--commit" ]; then
    gcloud builds sumbit --tag gcr.io/${project_id}/${container}
  fi
done
