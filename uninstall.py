#!/usr/bin/env python3

import os
import subprocess

def uninstall():
    if os.path.exists("/usr/local/bin/rfkill-unblock.py"):
        os.remove("/usr/local/bin/rfkill-unblock.py")

    if os.path.exists("/etc/systemd/system/rfkill-unblock.service"):
        subprocess.run("systemctl stop rfkill-unblock.service",shell=True) 
        subprocess.run("systemctl disable rfkill-unblock.service",shell=True)
        os.remove("/etc/systemd/system/rfkill-unblock.service")

if __name__ == '__main__':
    try:
        uninstall()
    except PermissionError:
        print("権限がありません")
