# Google Cloud Microservice Infrastructure

- [`infrastructure/build/`](infrastructure/build/): Build the microservice when
  source code changes and publish an artifact
- [`infrastructure/deploy/`](infrastructure/deploy/): Deploy the microservice
  when a new artifact is published
- [`infrastructure/runtime/`](infrastructure/runtime/): The actual **Api
  Gateway**, **Cloud Functions**, **Data Sources**, **Pub/Sub Topics** that
  comprise this microservice
