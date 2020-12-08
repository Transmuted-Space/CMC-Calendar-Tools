# project-level integration tests

Integration tests that run the entire project and test that it works go here.

Only external dependencies (such as the CMC calendar requests) are mocked.

## notes on how to actually achieve this

`gcloud` now has emulators for
[firestore](https://cloud.google.com/sdk/gcloud/reference/beta/emulators/firestore)
and [pub/sub](https://cloud.google.com/pubsub/docs/emulator). Presumably, we can
run both of these to get everything set up that the cloud functions need.

From there, we need a way to run all the cloud functions at once in a way that
lets integration specs know how to invoke them. That may mean discovering and
running all of them in separate threads, storing the addresses in environment
variables that can then be used by tests or the developer.

Since the pubsub-triggered functions _subscribe_ to pubsub, pubsub doesn't need
to know their locations. So, only the HTTP-triggered functions actually need to
be addressable.

Certainly, the easiest thing to do would be to just hardcode all the
`function-framework` and emulator calls in the `start.sh`.
