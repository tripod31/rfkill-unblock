#!/usr/bin/env python3
import argparse
import subprocess
import sys

SERVICE="rfkill-unblock"
ACTION = "enable,disable,start,stop,status"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action',help=ACTION)
    args=parser.parse_args()

    if not args.action in ACTION.split(","):
        print(f"いずれかの操作を指定して下さい({ACTION})")
        sys.exit()

    subprocess.run(f"systemctl {args.action} {SERVICE}.service",shell=True)
