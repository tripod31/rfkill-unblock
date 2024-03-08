#!/usr/bin/env python3
#rfkill-unblock daemon

import syslog
import subprocess
import json
import time
import argparse

MSG_TITLE='rfkill-unblock'
DEV_TYPES=('wlan','bluetooth')
KEY='rfkilldevices'

class Process:

    def __init__(self):
        pass

    def get_states(self):
        """
        get rfkill softblock state
        returns:{dev_type:unblock or block}
        """
        ret = {}
        proc = subprocess.run("rfkill -J", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if proc.returncode != 0:
            raise Exception("rfkill exec err")

        info = json.loads(proc.stdout)
        if not KEY in info:
            raise Exception(f"rfkill parse err:key('{KEY}')not exists")
        for dev in info[KEY]:
            if not 'type' in dev:
                raise Exception("rfkill parse err:key('type') not exists")
            for type in DEV_TYPES:
                if dev['type'] == type:
                    ret[type] = dev['soft']
        return ret

    def unblock(self,type):
        proc = subprocess.run("rfkill unblock {}".format(type), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if proc.returncode != 0:
            raise Exception("rfkill exec err")

    def main(self):
        syslog.openlog(MSG_TITLE)
        while True:
            states = self.get_states()
            for type in DEV_TYPES:
                if type in states and states[type] == 'blocked':
                    self.unblock(type)
                    syslog.syslog("unblocked {}".format(type))
            time.sleep(args.interval_sec)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--interval_sec',default=10, help="state checking interval(seccond).default=10")
    args=parser.parse_args()

    obj = Process()
    obj.main()
