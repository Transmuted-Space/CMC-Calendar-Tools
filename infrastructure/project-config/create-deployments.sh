#!/bin/sh
# SYNOPSIS: ./create-deployments.sh [--preview|--commit|--cancel] [--dry-run]
#
# Creates preview deployments and commits previously-created previews for the
# entire project stack. It does this by finding and executing
# `infrastructure/ci/ci.yml` and `infrastructure/runtime/runtime.yml`
# for each microservice.
#
# If --preview is specified, preview deployments are created.
# If --commit is specified, previously-created previews are executed.
# If --cancel is specified, previously-created previews are deleted.
#
# If --dry-run is specified as the second positional argument, the commands to
# be run will be emitted to the console, but no `gcloud` commands will actually
# be executed.
#
# This cannot (currently) be run by CI; it has interactive prompts and can only
# be run in interactive mode.
#
# You MUST start with --preview. This script does not create deployments without
# previewing first.
#
# This command does not do actual option parsing. Only the first two positional
# arguments are recognized. They cannot be specified in alternate order. There
# are no shorthands.
set -e

project_config_dir=$(dirname $(type -p ${0}))
cd ${project_config_dir}/../../

for microservice_dir in microservices/*; do
  microservice=${microservice_dir%*/}
  microservice=${microservice##*/}

  if [ "${1}" == "--preview" ]; then
    echo "gcloud deployment-manager deployments create ${microservice}-cd \\
  --config=microservices/${microservice}/infrastructure/cd/cd.yml \\
  --preview"
    if [ "${2}" != "--dry-run" ]; then
      gcloud deployment-manager deployments create ${microservice}-cd \
        --config=microservices/${microservice}/infrastructure/cd/cd.yml \
        --preview
    fi
    echo "gcloud deployment-manager deployments create ${microservice}-microservice \\
  --config=microservices/calendar/infrastructure/runtime/runtime.yml \\
  --preview"
    if [ "${2}" != "--dry-run" ]; then
      gcloud deployment-manager deployments create ${microservice}-microservice \
        --config=microservices/calendar/infrastructure/runtime/runtime.yml \
        --preview
    fi

  elif [ "${1}" == "--commit" ]; then
    echo "gcloud deployment-manager deployments update ${microservice}-cd"
    if [ "${2}" != "--dry-run" ]; then
      gcloud deployment-manager deployments update ${microservice}-cd
    fi
    echo "gcloud deployment-manager deployments update ${microservice}-microservice"
    if [ "${2}" != "--dry-run" ]; then
      gcloud deployment-manager deployments update ${microservice}-microservice
    fi

  elif [ "${1}" == "--cancel" ]; then
    echo "gcloud deployment-manager deployments cancel-preview ${microservice}-cd"
    if [ "${2}" != "--dry-run" ]; then
      gcloud deployment-manager deployments cancel-preview ${microservice}-cd
    fi
    echo "gcloud deployment-manager deployments cancel-preview ${microservice}-microservice"
    if [ "${2}" != "--dry-run" ]; then
      gcloud deployment-manager deployments cancel-preview ${microservice}-microservice
    fi

  else
    echo "You must specify one of: --preview|--commit|--cancel"
    exit 1
  fi
done
