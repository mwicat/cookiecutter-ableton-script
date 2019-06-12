#!/bin/bash

set -o nounset
set -o errexit

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd '/Applications/Ableton Live 10 Suite.app/Contents/App-Resources/MIDI Remote Scripts'
sudo ln -sfn "${SCRIPT_DIR}/{{cookiecutter.package_name}}"
