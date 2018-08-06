#!/bin/bash
([ -f .env/bin/activate ] || python3 -m venv .env) &&

. .env/bin/activate &&

pip install -U pip setuptools wheel &&
pip install -U ansible "pywinrm>=0.1.1" 
