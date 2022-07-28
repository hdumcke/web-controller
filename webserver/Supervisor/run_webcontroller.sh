#!/bin/bash

# wait util services are up
sleep 10
# make sure joystick is nit running
systemctl stop joystick
/usr/local/bin/web-controller
