from func import *
from func import checkCode,checkFile,checkSqlAndShell,runShell,spliceShell

funcdic = {
    "1": checkCode.checkcode,
    "2": checkSqlAndShell.checkss,
}

def func1(i):
    func = funcdic[i]
    print("************** :      ", funcdic[i])
    print(func)
    func()

def main():
    print("................................开始执行main.................................")
    print("""
    ******************************输入1:开始检查代码*********************************
    ******************************输入2:开始检查文件*********************************
    ******************************输入3:开始检查代码*********************************
    ******************************输入4:开始检查代码*********************************
    ******************************输入5:开始检查代码*********************************
    ******************************输入    6:    结束*********************************
    """)
    funclist = ["1", "2", "3", "4", "5"]
    while True:
        inp = input(">>>>>>>:")

        if inp in funclist:
            func1(inp)
        elif inp == '6':
            print("任务结束，再贱")
            break

if __name__ == '__main__':
    main()