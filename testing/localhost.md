Somehow we gotta figure out how to run all the cloud functions at once in a way
that lets integration specs know how to invoke them.

This project doesn't have Cloud Endpoints or API Gateway, so maybe a clean API
when developing locally that matches up with what the GCP project will have
isn't necessary.

Each function could just be run on a different port and the route passed to the
specs somehow.

If each spec is named for the Cloud Function it tests, maybe we can determine
the functions to run that way, then start each one, pass the port to the spec,
then kill it.

For function discovery of a function named `bar` in domain `foo`, check
`domains/foo/src/main.py#bar` and `domains/foo/.build/index.js#bar`
