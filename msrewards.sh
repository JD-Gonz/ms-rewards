#!/bin/bash

read -p "Please define a sleep interval: " user_input
python3 /home/josgon/msrewards/web.py "$user_input"
sleep 900
python3 /home/josgon/msrewards/mobile.py "$user_input"