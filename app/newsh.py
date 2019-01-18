import os
import re

def createNewSh(str1):
    print("开始组建sh脚本")
    print("str1=[%s]" % str1)
    if os.path.isfile(str1):
        pass

def openfile(dpath, filename):
    """
    :function:将命令添加到sh脚本里面
    :param dpath:
    :param filename:
    :return:
    """
    if os.path.splitext(filename)[1] == ".sh":
        flag = True
        startflag = "satrtflag"
        install = "install "

        os.chdir(dpath)
        nfilename = "22222222222.sh"
        os.rename(filename, nfilename)

        with open(nfilename, "r") as f:
            with open(filename, 'w+') as fn:
                for dd in f:
                    # 拼接：tmp = 'install XQ-2018-791 TR_45871_X_20181210.sh'
                    tmp = install + dpath.split("\\").pop() + " " + filename + "\n"
                    if startflag in dd:
                        print(tmp)
                        fn.write(tmp)
                    elif install in dd and flag == True:
                        print(tmp)
                        fn.write(tmp)
                        flag = False
                    else:
                        fn.write(dd)
    else:
        os.chdir(dpath)
        with open(filename, 'r+') as f:
            tmp = 'test massage'
            f.write(tmp)

if __name__ == '__main__':
    dpath = "F:\\黄小宝的宝\\测试目录"
    filename = "1111111111.sh"