#!/usr/bin/env python3
# coding:utf-8

import unittest
import subprocess

class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def test1(self):
        """
        syslogを監視して、スクリプトが実行されていることを確認
        """
        cmd = "timeout 70 tail -n 0 -f /var/log/syslog|grep rfkill-unblock.py"
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = ""
        while proc.poll() is None:
            output = proc.stdout.readline().decode().strip()
            print(output)
            #proc.kill()

        if len(output)>0:
            print("syslogでスクリプトの出力が確認できました")
        else:
            print("syslogでスクリプトの出力が確認できませんでした")
        assert len(output)>0

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()
