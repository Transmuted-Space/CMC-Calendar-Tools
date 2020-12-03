#!/bin/sh
# SYNOPSIS: npm test [domain="*"] [suite="unit"]
#
# EXAMPLE: run unit tests for all domains
# ./test.sh
#
# EXAMPLE: run unit tests for the `foo` domain
# ./test.sh foo
#
# EXAMPLE: run integration tests for the `foo` domain
# ./test.sh foo integration

testfn() {
  if [ $# -gt 0 ] && [ "${1##*-*}" ]; then
    domain=${1};
    shift;
  fi
  if [ $# -gt 0 ] && [ "${1##*-*}" ]; then
    suite=${1};
    shift;
  fi
  domain=${domain-"*"};
  suite=${suite-unit};

  # Run Python unittest
  if [ ${suite} -eq "unit" ]; then
    python_spec="domains/${domain}/**/tests.py"
    echo "pipenv run python -m unittest ";
    pipenv run python -m unittest domains/${domain}/**/tests.py;
  fi

  # Run Mocha unit or integration tests
  if [ ${suite} -eq "unit" ]; then
    mocha_spec="domains/${domain}/**/*.spec.ts";
  else
    mocha_spec="domains/${domain}/${suite}/**/*.spec.ts";
  fi
  mocha_config="testing/mocha/mocha.${suite}.json";
  echo "mocha ${mocha_spec} --config ${mocha_config}";
  mocha ${mocha_spec} --config ${mocha_config};
};
testfn $@;
