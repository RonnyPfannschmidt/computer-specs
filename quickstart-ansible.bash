#!/bin/bash
([ -d .env ] || python3 -m venv .env) &&
.env/bin/pip install -Uq pip setuptools setuptools_scm wheel &&
.env/bin/pip install -Uq ansible~=2.7.0 mitogen "pywinrm>=0.1.1" click
