#!/bin/sh
#
# Creates preview deployments and commits previously-created previews for the
# entire project stack.
#
# SYNOPSIS: ./create-deployments.sh [--preview|--commit|--cancel]
#
# If --preview is specified, preview deployments are created.
# If --commit is specified, previously-created previews are executed.
# If --cancel is specified, previously-created previews are deleted.
#
# This script prints the commands to be run to the console for preview and
# issues a prompt before continuing.
#
# This script executes gcloud deployment-manager commands for each deployment
# found in `/microservices/{microservice}/infrastructure/{deployment}`. It
# assumes the top-level deployment configuration is found in
# `{deployment}/{deployment}.yml`; for example, if there is a directory called
# `/microservices/foo/infrastructure/bar`, the script looks for a top-level
# deployment configuration in `/microservices/foo/infrastructure/bar/bar.yml`.
#
# This cannot (currently) be run by CI; it has interactive prompts and can only
# be run in interactive mode.
#
# You MUST start with --preview. This script does not create deployments without
# previewing first.
#
set -e

project_config_dir=$(dirname $(type -p ${0}))
cd ${project_config_dir}/../../

count="0"
for microservice_dir in microservices/*; do
  microservice=${microservice_dir%*/}
  microservice=${microservice##*/}
  for infrastructure_dir in ${microservice_dir}/infrastructure/*; do
    if [ -d "${infrastructure_dir}" ]; then
      count=$(expr ${count} + 1)
      deployment=${infrastructure_dir%*/}
      deployment=${deployment##*/}

      if [ "${1}" == "--preview" ]; then
        echo "gcloud deployment-manager deployments create ${microservice}-${deployment} \\
    --config=microservices/${microservice}/infrastructure/${deployment}/${deployment}.yml \\
    --preview"
      elif [ "${1}" == "--commit" ]; then
        echo "gcloud deployment-manager deployments update ${microservice}-${deployment}"
      elif [ "${1}" == "--cancel" ]; then
        echo "gcloud deployment-manager deployments cancel-preview ${microservice}-${deployment}"
      else
        echo "You must specify one of: --preview, --commit, --cancel"
        exit 1
      fi
    fi
  done
done

if [ "${count}" -gt "0" ]; then
  read -p "The commands above will be executed. Continue? [y/N]: " approve
else
  echo "No deployments found. Exiting"
  exit 1
fi

if echo "${approve}" | grep -iqF "y"; then
  for microservice_dir in microservices/*; do
    microservice=${microservice_dir%*/}
    microservice=${microservice##*/}
    for infrastructure_dir in ${microservice_dir}/infrastructure/*; do
      if [ -d "${infrastructure_dir}" ]; then
        deployment=${infrastructure_dir%*/}
        deployment=${deployment##*/}

        if [ "${1}" == "--preview" ]; then
          gcloud deployment-manager deployments create ${microservice}-${deployment} \
            --config=microservices/${microservice}/infrastructure/${deployment}/${deployment}.yml \
            --preview
        elif [ "${1}" == "--commit" ]; then
          gcloud deployment-manager deployments update ${microservice}-${deployment}
        elif [ "${1}" == "--cancel" ]; then
          gcloud deployment-manager deployments cancel-preview ${microservice}-${deployment}
        else
          echo "You must specify one of: --preview, --commit, --cancel"
          exit 1
        fi
      fi
    done
  done
fi
