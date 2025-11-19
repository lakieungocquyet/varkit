#! /bin/bash

pixi install --manifest-path /opt/varkit/pixi.toml -e varkit

python3 /opt/varkit/src/reference_preparation/download_reference.py