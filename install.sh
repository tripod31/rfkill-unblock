#!/bin/sh
cp rfkill-unblock.py /usr/local/bin/
cp rfkill-unblock /etc/cron.d/
cp root-resume.service /etc/systemd/system/
systemctl enable root-resume
