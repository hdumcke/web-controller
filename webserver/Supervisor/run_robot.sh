#!/bin/bash

# wait util services are up
sleep 10
# make sure joystick is nit running
systemctl stop joystick
/usr/bin/python3 /home/ubuntu/Robotics/QuadrupedRobot/StanfordQuadruped/run_robot.py
