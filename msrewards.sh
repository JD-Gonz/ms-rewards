#!/bin/bash

read -p "Please define a sleep interval: " user_input
cwd=$(dirname "$0")
python3 $cwd/web.py "$user_input"
sleep 900
python3 $cwd/mobile.py "$user_input"
