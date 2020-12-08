# cmc-calendar-tools

## Development Setup

1. Install `Python 3.8`
2. `pip install pipenv`
3. [Install `nvm` and `v12.x` of Node](https://github.com/nvm-sh/nvm#installing-and-updating)
4. [Install a JDK](https://www.oracle.com/java/technologies/javase-downloads.html)
   ([required](https://cloud.google.com/pubsub/docs/emulator#prereq) to emulate
   **Pub/Sub** locally 😞)
5. [Install `gcloud`](https://cloud.google.com/sdk/docs/install)
6. Configure `gcloud`
   - `gcloud config configurations create cmc-calendar-tools`
   - `gcloud config set project {project-id}`
   - `gcloud components install beta cloud-firestore-emulator pubsub-emulator`
   - `gcloud components update`
   - `gcloud auth login`
     - login to run `gcloud` project management commands
   - `gcloud auth application-default login`
     - login again to give locally-run **Cloud Functions** necessary credentials
7. Clone and navigate to the project in your shell
8. `pipenv install --dev`
9. `npm i`

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
