#!/bin/sh

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
