#!/bin/sh
# SYNOPSIS: ./test-unit.sh [microservice="*"]
#
# The commands that this script ultimately runs are printed to the console, so
# you can see what is actually going on.
#
# EXAMPLE: run unit tests for all microservices
# ./test-unit.sh
#
# EXAMPLE: run unit tests for the `foo` microservice
# ./test-unit.sh foo

testfn() {
  if [ $# -gt 0 ] && [ "${1##*-*}" ]; then
    microservice=${1};
    shift;
  fi
  microservice=${microservice-"*"};

  # Run Python unit tests
  if test -n "$(find microservices/${microservice} -name tests.py -print -quit)"; then
    python_spec="microservices/${microservice}/**/tests.py"
    echo "pipenv run python -m unittest ${python_spec}";
    pipenv run python -m unittest ${python_spec};
  fi

  # Run Mocha unit tests
  if test -n "$(find microservices/${microservice} -name '*.spec.ts' -print -quit)"; then
    mocha_config="mocha/mocha.unit.json";
    mocha_spec="microservices/${microservice}/**/*.spec.ts";
    echo "npx mocha --config ${mocha_config} ${mocha_spec}";
    npx mocha --config ${mocha_config} ${mocha_spec};
  fi
};
testfn $@;
