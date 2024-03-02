#!/bin/sh
if [ -f /usr/local/bin/rfkill-unblock.py ]; then
    rm /usr/local/bin/rfkill-unblock.py
fi
if [ -f /etc/cron.d/rfkill-unblock ]; then
    rm /etc/cron.d/rfkill-unblock
fi
systemctl disable root-resume
if [ -f /etc/systemd/system/root-resume.service ]; then
    rm /etc/systemd/system/root-resume.service
fi
