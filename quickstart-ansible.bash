#!/bin/bash
([ -d .env ] || python3 -m venv .env) &&
.env/bin/pip install -Uq pip setuptools wheel &&
.env/bin/pip install -Uq ansible "pywinrm>=0.1.1" click
