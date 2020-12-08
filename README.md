# cmc-calendar-tools

## Development Setup

1. Install `Python 3.8`
2. `pip install pipenv`
3. [Install `nvm` and `v12.x` of Node](https://github.com/nvm-sh/nvm#installing-and-updating)
4. [Install `gcloud`](https://cloud.google.com/sdk/docs/install)
5. Configure `gcloud`
   - `gcloud auth login`
   - `gcloud config configurations create cmc-calendar-tools`
   - `gcloud config set project {project-id}`
6. Clone and navigate to the project in your shell
7. `pipenv install --dev`
8. `npm i`

## Running Locally

The [`start.sh`](blob/master/start.sh) script runs emulators for
[Firestore](https://cloud.google.com/sdk/gcloud/reference/beta/emulators/firestore)
and [Pub/Sub](https://cloud.google.com/pubsub/docs/emulator), mirroring the
deployed configuration in the current GCP project.

```
./start.sh
```

## Testing

### Running Tests

Unit tests are run using the [`test-unit.sh`](blob/master/test-unit.sh) script.
It runs both Python and Mocha unit tests in the specified microservice
directory. For usage, look at the script file; documentation is in its header.

### Writing Tests

Unit tests are colocated with the code they test.

- in TypeScript, `MyThing.ts` should have `MyThing.spec.ts`
- in Python, tests for a package should be defined in `tests.py` in that
  package.
