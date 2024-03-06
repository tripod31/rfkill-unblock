#!/usr/bin/env python3
# coding:utf-8

import time
import os
from stat import *

class Process:
    def __init__(self):
        self.path           = "/var/log/syslog"     #監視対象ファイル
        self.keyword        = "rfkill-unblock.py"   #監視対象キーワード
        self.interval_sec   = 1                     #ファイルを監視する秒間隔
        self.timeout_sec    = 70                    #タイムアウトする秒数

        self.file = open(self.path,'r')

        #ファイル末尾へ移動
        st_results = os.stat(self.path)
        st_size = st_results[ST_SIZE]
        self.file.seek(st_size)

        self.start_time = time.time()  # 開始時刻

    def __del__(self):
        self.file.close()

    def tail_f(self):
        """
        ファイルの末尾を監視
        """
        while True:
            fpos = self.file.tell()
            line = self.file.readline()
            if not line:
                time.sleep(self.interval_sec)
                self.file.seek(fpos)    #スリープ前の位置に戻す

                #タイムアウトチェック
                now = time.time()
                diff = int(now - self.start_time)
                print(f"\r{diff:02}秒経過",end="",flush=True)
                if diff > self.timeout_sec:
                    print(f"\nsyslogに{self.keyword}が確認できませんでした")
                    break

                continue

            if line.find(self.keyword)>0:
                print(f"\nsyslogに{self.keyword}を確認しました")
                print(line.strip())
                break


if __name__ == '__main__':
    proc = Process()
    proc.tail_f()
