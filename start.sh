#!/bin/sh
function=${1-all}
port=${1-9999}

# TODO use this instead of a credsfile: https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login

# TODO implement this
# used by mocha/mocha.integration.ts as a default test target
export FUNCTIONS_FRAMEWORK_ENDPOINT="http://localhost:${port}"

# TODO run tsc with tsc-watch and restart functions-framework on emit
npx functions-framework --source=.build/functions --target=${function} --port=${port}

# TODO python?? https://github.com/GoogleCloudPlatform/functions-framework-python