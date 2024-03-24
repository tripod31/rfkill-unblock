#!/usr/bin/env python3
import argparse
import subprocess
import sys

SERVICE="rfkill-unblock"
ACTIONS = ["enable","disable","start","stop","status"]

def process():
    parser = argparse.ArgumentParser()
    parser.add_argument('action',choices=ACTIONS)
    args=parser.parse_args()

    subprocess.run(f"systemctl {args.action} {SERVICE}.service",shell=True)

if __name__ == '__main__':
    process()
