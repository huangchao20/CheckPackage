#coding=utf-8
import os

def testfunc(dpath, filename):
    os.chdir(dpath)
    nfilename = "22222222222.sh"

    nfilename = os.rename(filename, nfilename)
    print('-----------------------')
    print(nfilename)
    print('-----------------------')
    print(filename)

def openfile(dpath,filename):
    if os.path.splitext(filename)[1] == ".sh":
        flag = True
        startflag = "startflag"
        os.chdir(dpath)
        nfilename = "22222222222.sh"
        os.rename(filename, nfilename)
        with open(nfilename, "r") as f:
            with open(filename, 'w+') as fn:
                for dd in f:
                    tmp = "install " + dpath.split("\\").pop() + " " + filename + "\n"
                    if "install" in dd and flag == True:
                        tmp = "install " + dpath.split("\\").pop() + " " + filename + "\n"
                        fn.write(dd)
                        fn.write(tmp)
                        flag = False
                    elif startflag in dd:
                        print(dd)
                        print("会删除“startflag吗？”")
                        fn.write(tmp)
                    else:
                        fn.write(dd)
        os.remove(nfilename)

    else:
        os.chdir(dpath)
        with open(filename, 'r+') as f:
            print(f.read())

            tmp = 'test massage'
            f.write("\n")
            f.write(tmp)

if __name__ == '__main__':
    dpath = "F:\\黄小宝的宝\\测试目录"
    filename = '1111111111.sh'
    # filename = '22222222222.txt'
    openfile(dpath, filename)
    # testfunc(dpath, filename)