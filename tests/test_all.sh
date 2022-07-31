#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0  <ip address of mini pupper>"
    exit 1
fi

# $(which python3) is used to cover the case of Python virtual environments
$(which python3) pt2.py -i $1 -f test_activate.txt
$(which python3) pt2.py -i $1 -f test_cancel_shutdown.txt
$(which python3) pt2.py -i $1 -f test_toggle_trot.txt
$(which python3) pt2.py -i $1 -f test_walk_square_slow.txt
$(which python3) pt2.py -i $1 -f test_walk_square_fast.txt
#$(which python3) pt2.py -i $1 -f test_shutdown.txt
