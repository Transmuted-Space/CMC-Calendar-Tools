#!/bin/sh
gcloud deployment-manager deployments create calendar-deploy \
  --config=microservices/calendar/infrastructure/deploy/deploy.yml
gcloud deployment-manager deployments create calendar-microservice \
  --template=microservices/calendar/infrastructure/runtime/runtime.jinja \
  --properties=artifactsBucket:calendar-artifacts
