#!/bin/sh
cp rfkill-unblock.py /usr/local/bin/
cp rfkill-unblock /etc/cron.d/
cp rfkill-unblock.service /etc/systemd/system/
systemctl enable rfkill-unblock
