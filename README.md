# cmc-calendar-tools

Google Cloud Platform project that provides some nice utilities for the CMC
calendar, such as interest-based email notifications and Google Calendar export.

This project is patterned after
[template-microservices-monorepo](https://github.com/wild-surmise/template-microservices-monorepo).

## Table of Contents

- [Roadmap](#roadmap)
- [Architecture](#architecture)
- [Development Setup](#development-setup)
- [Running Locally](#running-locally)
- [Testing](#testing)
- [Deploying](#deploying)

## Roadmap

See the [Trello board](https://trello.com/b/YOMHIKfR/cmc-calendar-tools).

## Architecture

See the
[Architecture Diagram](https://drive.google.com/file/d/1CBbCz63O9MWSKpEF6RXBWa0ZRnHGH2h1/view)
for a high-level view of the cloud infrastructure and dependency graph.

## Development Setup

Clone and navigate to the project in your shell.

### `gcloud` Setup

1. [Install `gcloud`](https://cloud.google.com/sdk/docs/install)
2. Configure `gcloud`:
   - `gcloud components install beta`
   - `gcloud components update`
   - `gcloud config configurations create {project-name}`
   - `gcloud config set project {project-id}`
   - `gcloud auth login`
     - login to run `gcloud` project management commands
   - `gcloud auth application-default login`
     - login again to give locally-run **Cloud Functions** necessary credentials

### Node Setup

1. [Install `nvm`](https://github.com/nvm-sh/nvm#installing-and-updating) and a
   [gcloud-compatible version of Node](https://cloud.google.com/functions/docs/concepts/nodejs-runtime)
2. `npm i`

### Python Setup

1. Install `Python 3.8`
2. `pip install pipenv`
3. `pipenv install --dev`

### Firestore Setup

1. `gcloud components install cloud-firestore-emulator`

### Pub/Sub Setup

1. `gcloud components install pubsub-emulator`
2. [Install a JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
   ([required](https://cloud.google.com/pubsub/docs/emulator#prereq) to emulate
   **Pub/Sub** locally 😞)

## Running Locally: `start.sh`

```
./start.sh
```

The [`start.sh`](blob/master/start.sh) script runs emulators for
[**Firestore**](https://cloud.google.com/sdk/gcloud/reference/beta/emulators/firestore)
and [**Pub/Sub**](https://cloud.google.com/pubsub/docs/emulator), mirroring the
deployed configuration in the current GCP project.

It then starts up each of the **Cloud Functions** in the project in a different
thread:

- Functions with an `http` trigger will each be run on a different port, and the
  resulting endpoints will be emitted to the console. The endpoints can be
  invoked with `curl` or [Postman](https://www.postman.com/)
- Functions with a `pub/sub` trigger will emit the name of their subscribed
  topic. Events can be published to a Pub/Sub topic with
  [`gcloud pubsub topics publish`](https://cloud.google.com/sdk/gcloud/reference/pubsub/topics/publish)

## Testing

### Unit Tests

#### Running Unit Tests

```
./test-unit.sh [microservice=*]
```

Unit tests are run using the [`test-unit.sh`](blob/master/test-unit.sh) script.
It runs both Python and Mocha unit tests in the specified microservice
directory. For usage, look at the script file; documentation is in its header.

#### Writing Unit Tests

Unit tests are colocated with the code they test.

- in TypeScript, `MyThing.ts` should have `MyThing.spec.ts`
- in Python, tests for a package should be defined in `tests.py` in that
  package.

### Integraion Tests

**TODO**

## Deploying

### Updating a single CI stack

Use
[`gcloud deployment-manager deployments update`](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/update).

### Deploying a single runtime stack

You should not have to do this for existing microservices - runtime
infrastructure is automatically updated by the code change trigger.

New microservices will reqiure an initial deploy. Use
[`gcloud deployment-manager deployments create`](https://cloud.google.com/sdk/gcloud/reference/deployment-manager/deployments/create)
to create both the deployment stack and the runtime stack. See existing
microservices for infrastructure examples.

### Deploying to a new GCP Project

This entire project stack can be deployed in a brand-new Google Cloud Platform
project with the following steps:

- [Create the project](https://console.cloud.google.com/projectcreate) using the
  Google Cloud Console
- Configure `gcloud` to work with the new project:
  - `gcloud config configurations create {project-name}`
  - `gcloud config set project {project-id}`
- Cross your fingers
- Run the genesis script:
  [`infrastructure/project-config/genesis.sh`](blob/master/infrastructure/project-config/genesis.sh)
