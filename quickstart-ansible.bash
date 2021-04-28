#!/bin/bash
([ -d .env ] || python3 -m venv .env) &&
.env/bin/pip install -Uq pip setuptools setuptools_scm wheel &&
.env/bin/pip install -Uq ansible click
