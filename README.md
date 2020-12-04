# cmc-calendar-tools

## Development Setup

1. Install `Python 3.8`
2. `pip install pipenv`
3. [Install `gcloud`](https://cloud.google.com/sdk/docs/install)
4. [Install `nvm` and `v12.x` of Node](https://github.com/nvm-sh/nvm#installing-and-updating)
5. Clone and navigate to the project in your shell
6. `npm i`

## Running Cloud Functions locally

### Python Function

```
pipenv run functions-framework --source=domains/{domain}/src/ --function={function}
```

### Node Function

```
npm start {domain} {function}
```

## Testing

### Running Tests

All testing is run using the `test.sh` script.

TODO This will probably change a lot when we want to run functions for
integration tests

**Synopsis**

```
./test.sh [domain="*"] [suite="unit"]
```

**Run all unit tests**

```
./test.sh
```

**Run unit tests for `domains/foo/`**

```
./test.sh foo
```

**Run integration tests for `domains/foo/`**

```
./test.sh foo integration
```

### Writing Tests

Unit tests are colocated with the code they test.

- in TypeScript, `MyThing.ts` should have `MyThing.spec.ts`
- in Python, TODO (???)
