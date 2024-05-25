#!/usr/bin/env python3

import shutil
import os
import subprocess


def install():
    shutil.copy("rfkill-unblock.py"             , "/usr/local/bin/")
    shutil.copy("rfkill-unblock.service"        ,"/etc/systemd/system/")
    subprocess.run("systemctl enable rfkill-unblock.service",shell=True)
    subprocess.run("systemctl start rfkill-unblock.service",shell=True)

if __name__ == '__main__':
    try:
        install()
    except PermissionError:
        print("権限がありません")
