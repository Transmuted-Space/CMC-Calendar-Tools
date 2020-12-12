#!/bin/sh
project_config_dir=$(dirname $(type -p ${0}))
${project_config_dir}/enable-services.sh
${project_config_dir}/create-containers.sh --commit
set -e
${project_config_dir}/create-deployments.sh --preview
${project_config_dir}/create-deployments.sh --commit
