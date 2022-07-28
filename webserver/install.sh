#!/bin/bash

### Get directory where this script is installed
BASEDIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

sudo systemctl disable joystick
sudo systemctl disable robot
sudo apt install -y supervisor
sudo cp $BASEDIR/Supervisor/run_webcontroller.conf /etc/supervisor/conf.d/
sudo cp $BASEDIR/Supervisor/run_webcontroller.sh /etc/supervisor/conf.d/
sudo cp $BASEDIR/Supervisor/run_robot.conf /etc/supervisor/conf.d/
sudo cp $BASEDIR/Supervisor/run_robot.sh /etc/supervisor/conf.d/
sudo pip uninstall -y backend
sudo rm -rf $BASEDIR/backend/backend.egg-info
sudo rm -rf $BASEDIR/backend/build
sudo PBR_VERSION=1.2.3 pip install $BASEDIR/backend
