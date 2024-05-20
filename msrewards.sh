#!/bin/bash

read -p "Please define a sleep interval: " user_input
cwd=$(dirname "$0")
python3 $cwd/web.py "$user_input"
echo "Completed web searches. Going to sleep for $user_input min"
sleep $(($user_input))m
python3 $cwd/mobile.py "$user_input"
