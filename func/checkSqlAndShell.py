#encoding=utf-8
import os

def checkss(dpath):
    print("----------start chech sh and sql-----------[%s]" % dpath)

    if os.path.isdir(dpath):
        for shfile in os.listdir(dpath):
            if os.path.splitext(shfile)[1] == ".sh":
                pass