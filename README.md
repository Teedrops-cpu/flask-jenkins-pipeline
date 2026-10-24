# flask-jenkins-pipeline

A small Flask app with a jenkins CI/CD pipeline (Build, Test, Deploy).

## Additional evidence

**Stage names, build #6:** Build, Test and Deploy all green.

![Pipeline overview](docs/screenshots/build-6-pipeline-overview.png)

**First successful run (build #1):**

![Build 1 console](docs/screenshots/build-1-console-success.png)

**Automatic trigger:** build #3 shows `Started by an SCM change`, so no manual click was needed.

![SCM trigger](docs/screenshots/scm-trigger.png)

**Test report from the JUnit plugin:**

![Tests passing](docs/screenshots/tests-passing.png)

**Credential stored in Jenkins (the secret value is never shown):**

![Credentials](docs/screenshots/credentials.png)

**Build history stage by stage:** #5 is the deliberate failure, where Test failed and Deploy was skipped.

![Stages history](docs/screenshots/build-6-stages.png)
