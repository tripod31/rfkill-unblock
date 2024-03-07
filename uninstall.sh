#!/bin/sh
if [ -f /usr/local/bin/rfkill-unblock.py ]; then
    rm /usr/local/bin/rfkill-unblock.py
fi
if [ -f /etc/systemd/system/rfkill-unblock.service ]; then
    systemctl disable rfkill-unblock
    rm /etc/systemd/system/rfkill-unblock.service
fi
