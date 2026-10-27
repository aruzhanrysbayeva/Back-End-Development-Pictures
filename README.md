# Back-End-Development-Pictures

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

Prepared and tested locally. Published to https://github.com/aruzhanrysbayeva/Back-End-Development-Pictures. IBM Cloud deployment is pending. Local screenshots and execution reports document local execution.
