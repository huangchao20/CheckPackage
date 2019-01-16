import os
import re

def createNewSh(str1):
    print("开始组建sh脚本")
    print("str1=[%s]" % str1)
    if os.path.isfile(str1):
        pass