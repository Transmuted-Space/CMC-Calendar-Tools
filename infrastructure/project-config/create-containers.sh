#!/bin/sh
#
# Creates containers by calling `gcloud builds submit` for each directory in
# `/infrastructure/containers/`.
#
# SYNOPSIS: ./create-containers.sh
#
# This script prints the commands to be run to the console for preview and
# issues a prompt before continuing.
#
set -e

project_config_dir=$(dirname $(type -p ${0}))
containers_dir="${project_config_dir}/../containers"
project_id=$(gcloud config get-value project | sed -n 1p)

count="0"
for container_dir in ${containers_dir}/*; do
  if [ -d "${container_dir}" ]; then
    count=$(expr ${count} + 1)
    container_dir=${container_dir%*/}
    container=${container_dir##*/}
    echo "gcloud builds submit --tag gcr.io/${project_id}/${container}"
  fi
done


if [ "${count}" -gt "0" ]; then
  read -p "The commands above will be executed. Continue? [y/N]: " approve
else
  echo "No deployments found. Exiting"
  exit 1
fi

if echo "${approve}" | grep -iqF "y"; then
  for container_dir in ${containers_dir}/*; do
    if [ -d container_dir ]; then
      container_dir=${container_dir%*/}
      container=${container_dir##*/}
      gcloud builds sumbit --tag gcr.io/${project_id}/${container}
    fi
  done
fi
