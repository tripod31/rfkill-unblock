#!/bin/sh
cp rfkill-unblock.py /usr/local/bin/
cp rfkill-unblock.service /etc/systemd/system/
systemctl enable rfkill-unblock

