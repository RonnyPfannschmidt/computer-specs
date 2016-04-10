#!/bin/bash
([ -f .env/bin/activate ] || virtualenv -p python2 .env) &&

. .env/bin/activate &&

pip install -U pip setuptools wheel &&
pip install -U ansible "pywinrm>=0.1.1" 
