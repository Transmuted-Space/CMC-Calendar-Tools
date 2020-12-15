#!/bin/sh

echo "gcloud services enable
  deploymentmanager.googleapis.com, \\
  cloudbuild.googleapis.com, \\
  compute.googleapis.com, \\
  cloudfunctions.googleapis.com, \\
  pubsub.googleapis.com, \\
  cloudscheduler.googleapis.com, \\
  firestore.googleapis.com, \\
  storage-component.googleapis.com, \\
  storage.googleapis.com"

read -p "The command above will be executed. Continue? [y/N]" approve

if echo "${approve}" | grep -iqF "y"; then
  gcloud services enable \
    deploymentmanager.googleapis.com, \
    cloudbuild.googleapis.com, \
    compute.googleapis.com, \
    cloudfunctions.googleapis.com, \
    pubsub.googleapis.com, \
    cloudscheduler.googleapis.com, \
    firestore.googleapis.com, \
    storage-component.googleapis.com, \
    storage.googleapis.com
fi
