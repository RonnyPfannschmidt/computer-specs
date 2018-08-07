#!/bin/bash
([ -d .env ] || python3 -m venv .env) &&
.env/bin/pip install -U pip setuptools wheel &&
.env/bin/pip install -U ansible "pywinrm>=0.1.1"
