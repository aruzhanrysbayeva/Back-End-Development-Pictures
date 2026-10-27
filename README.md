# Back-End-Development-Pictures

Public README URL: https://github.com/aruzhanrysbayeva/Back-End-Development-Pictures/blob/main/README.md

Public repository: https://github.com/aruzhanrysbayeva/Back-End-Development-Pictures

Environment Setup: Python 3.14; create a virtual environment with `python -m venv .venv`, activate it, then run `python -m pip install -r requirements.txt`. Service configuration and verification commands are documented below.

Pictures URLs REST service, completed from the official [IBM starter](https://github.com/ibm-developer-skills-network/luggb-Back-End-Development-Pictures).
Original starter attribution and license are retained. Changes were prepared with AI assistance and should be reviewed by the learner before submission.

## Environment Setup

Tested locally with Python 3.14. Flask/Django dependency versions are pinned in requirements.txt. Run from this repository:

```sh
python -m venv .venv
# Linux/macOS: source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

The original course bin/setup.sh is preserved as supplied by IBM; it targets the course Cloud IDE. Local verification used the Python setup described above, rather than claiming that the Cloud IDE setup script ran.

## Implemented work

Health and count endpoints, GET /picture, GET /picture/<id>, POST /picture, PUT /picture/<id>, and DELETE /picture/<id>. JSON validation, missing-id handling and duplicate-id behavior follow the lab contract (including the course-required 302 on duplicates).

```sh
python -m pytest -v tests/test_api.py
python -m flask --app backend run --host 127.0.0.1 --port 5002
```

## Verification

11 original IBM pytest tests passed. Data is held in memory per the starter design; restarting resets it.

## Submission status

Prepared and tested locally. Published to https://github.com/aruzhanrysbayeva/Back-End-Development-Pictures. IBM Cloud deployment was verified; local and cloud evidence are identified separately.


## Verified cloud deployment

IBM Code Engine, port 8000, provided icr-secret; minimum scale 1. Public /health returned status OK.

Application: https://pictures.2ggnmp3ielrx.us-south.codeengine.appdomain.cloud

The course lab is temporary. MongoDB and SQLite use demonstration storage; do not treat this environment as a persistent production deployment. No administrator password or service secret is committed.
