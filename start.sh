#!/bin/sh
echo
echo "Functions manifest:"
echo "microservices/calendar.ingest: event trigger, calendar-ingest-topic"
echo
echo

npx concurrently -k \
  "gcloud beta emulators firestore start" \
  "gcloud beta emulators pubsub start" \
  "sleep 10 && $(gcloud beta emulators pubsub env-init)" \
  "pipenv run functions-framework --source=microservices/calendar --target=ingest --signature-type=event --debug"

# TODO TypeScript functions: run tsc with tsc-watch and restart functions-framework on emit
# npx functions-framework --source=microservices/???/.build --target=${function} --port=${port}
