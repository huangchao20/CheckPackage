#encoding=utf-8
import os
import xlrd

class checkCode:
    def __init__(self):
        print("checkCode")

    def foo1(self):
        print("foo1")
# 获取目标目录里面所有代码文件清单.xlsx/.xls
filenamelist = []
pylist = []

def getXlsxFile(dpath):
    for filename in os.listdir(dpath):
        flist = []
        os.chdir(dpath)
        if os.path.isfile(filename) and \
                filename.startswith("TS") and \
                (os.path.splitext(filename)[1] == ".xlsx" or os.path.splitext(filename)[1] == ".xls"):
            if filename not in filenamelist:
                p = os.getcwd().split("\\").pop()
                filename = dpath + "\\" + filename
                print("开始处理【%s】任务的【%s】文件!!!!!" % (p, filename))
                filenamelist.append(filename)
                flist = readxlrd(filename)
                pylist.append(flist)  # 将所有文件清单中的py文件名都添加到列表中，方便对比远程桌面代码是否存在多提或漏提
                print("处理结果:[%s]" % flist)
                print("【%s】任务的【%s】文件处理完成!!!!!" % (p, filename))

        elif os.path.isfile(filename):
            pass
        else:
            filepath = os.path.join(dpath, filename)
            getXlsxFile(filepath)
    return filenamelist, pylist


"""
功能：将excel文件中文件名放到对应的目录下面
入参：[['./workspace/PyTrade_fbap/TBATCH_Proc_M0001.py', './workspace/PyTrade_fbap/TBATCH_Proc_M0002.py'],[...],[...]]
出参：[['TBATCH_Proc_M0001.py', 'TBATCH_Proc_M0002.py', 'TCHCP_C0008.py'],[],[],[]]
"""


def getpath(pathlist):
    PyTrade_fbap = []
    PyComponent_fbap = []
    component_fbap = []
    PyTrade_ABOP = []
    listlist = []
    listlist = [PyTrade_fbap, PyComponent_fbap, component_fbap, PyTrade_ABOP]
    listp = ["PyTrade_fbap", "PyComponent_fbap", "component_fbap", "PyTrade_ABOP"]

    for i in range(len(pathlist)):
        for files in pathlist[i]:
            ff = files.split("/")
            listlist[listp.index(ff[2])].append(ff[3])
    return listlist


"""
功能：获取远程桌面的py文件名，并将文件名放置到对应的目录下面
"""


def getcwdfile(workspacepath):
    os.chdir(workspacepath)
    listp = ["PyTrade_fbap", "PyComponent_fbap", "component_fbap", "PyTrade_ABOP"]
    PyTrade_fbap = []
    PyComponent_fbap = []
    component_fbap = []
    PyTrade_ABOP = []
    listlist1 = []
    listlist1 = [PyTrade_fbap, PyComponent_fbap, component_fbap, PyTrade_ABOP]

    for path1 in listp:
        pathp = os.path.join(workspacepath, path1)
        print(pathp)
        os.chdir(pathp)
        listlist1[listp.index(path1)] = os.listdir(os.getcwd())
    return listlist1


"""
*****function name: movfile
*****input:dpath, flist
*****output:xlsx文件、workspace目录
"""


def movfile(dpath, flist):
    # 思路：将flist中的lfilelist[2]，lfilelist[3]都取出来再与pflist比较
    for lfile in flist:
        # lfile = "./workspace/PyTrade_ABOP/T0283000005_D0201.py"

        os.chdir(dpath)
        lfilelist = lfile.split("/")
        pathlist.append(lfilelist[2])  # 文件的上一级目录，如：“PyTrade_ABOP”
        paf.append(lfile.split("/", 2))[2]

        # 检查目录是否存在，如果不存在，则创建目录
        if not os.path.isdir(lfilelist[1]):
            os.mkdir(lfilelist[1])  # 创建workspace
            os.chdir(lfilelist[1])
            if not os.path.isdir(lfilelist[2]):
                os.mkdir(lfilelist[2])  # 创建存放代码的上一级目录
        # 取从远程桌面取下来的文件清单
        os.chdir(dpath)
        for lpath in os.path.listdir(dpath):
            pflist = []  # 远程桌面取下来对应的文件名
            if lpath.startswith("REL"):  # 获取REL开头的文件夹并cd进去
                os.chdir(lpath)
                if os.path.isdir(lfilelist[2]):
                    os.chdir(lfilelist[2])
                    pflist = os.path.listdir(os.getcwd())  # 将当前路径下的所有文件名都存放到pflist列表中


def readxlrd(filename):
    # os.chdir("F:\\TFS\\特色业务平台\\文档&DB&AFEjar包\\2018常规\\20180712\\TR-2018-233" )
    s = "服务器路径"
    workbook = xlrd.open_workbook(filename)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    t = 0
    filelist = []
    for i in range(0, worksheet.nrows):
        row = worksheet.row(i)
        for j in range(0, worksheet.ncols):
            if s in str(worksheet.cell_value(i, j)):  # 找到含有关键字段“服务器路径”所在列t
                t = j
        rolij = worksheet.cell_value(i, t).strip().strip(
            "-+")  # rstrip()字符串右去空	str.lstrip()左去空；str.strip().strip("-+") 两边去空
        if rolij.endswith(".py"):
            filelist.append(rolij)  # 将第t列数据添加到列表filelist中
    return filelist  # 返回fillelist ['./workspace/PyTrade_fbap/TBATCH_Proc_M0001.py', './workspace/PyTrade_fbap/TBATCH_Proc_M0002.py']

"""
功能：将excel文件中或者远程桌面取下来的文件的文件名放到对应的目录下面
入参：abs	pathlist [['./workspace/PyTrade_fbap/TBATCH_Proc_M0001.py', './workspace/PyTrade_fbap/TBATCH_Proc_M0002.py'],[...],[...]]
	或者"F:\\TFS\\特色业务平台\\文档&DB&AFEjar包\\2018常规\\20180712"
出参：listlist	[['TBATCH_Proc_M0001.py', 'TBATCH_Proc_M0002.py'],[],[]]
"""
def getcwdfile(abs):  # 传入文件列表或者路径
    listp = ["PyTrade_fbap", "PyComponent_fbap", "component_fbap", "PyTrade_ABOP"]
    PyTrade_fbap = []
    PyComponent_fbap = []
    component_fbap = []
    PyTrade_ABOP = []
    listlist = []
    listlist = [PyTrade_fbap, PyComponent_fbap, component_fbap, PyTrade_ABOP]
    if abs == None:
        print("请检查您输入是否为空")
        return None
    if type(abs) is list:  # 获取将xcel文件中文件名放到对应的目录下面
        for i in range(len(abs)):
            for files in abs[i]:
                ff = files.split("/")
                listlist[listp.index(ff[2])].append(ff[3])
    else:  # 获取远程桌面获取的文件
        print("A" * 150)
        print("V" * 150)
        os.chdir(abs)
        for i in range(len(listp)):
            pathp = os.path.join(abs, listp[i])
            os.chdir(pathp)
            listlist[listp.index(listp[i])] = os.listdir(os.getcwd())
    return listlist

# 查询获取的文件是否重复
def checkrepeat(listlist):
    for i in range(len(listlist)):
        for t in listlist[i]:
            for m in listlist:
                if listlist[i] != m and t in m:
                    print("%s 中的【%m】文件在【%m】中也存在， 请检查" % (s[i], t, m))

if __name__ == '__main__':
    Path = "E:\\SVN\\20180913\\特色业务平台"
    workspacepath = "F:\\TFS\\特色业务平台\\文档&DB&AFEjar包\\2018常规\\20180816"
    filename = "F:\\TFS\\特色业务平台\\文档&DB&AFEjar包\\2018常规\\20180712\\TR-2018-233\\TS_69935_AFA_20180712.xlsx"
    filename1 = "F:\\TFS\\特色业务平台\\文档&DB&AFEjar包\\2018常规\\20180712\\XQ-2018-167\\TS_69600_FBAP_O_20180712.xlsx"
    f, py = getXlsxFile(Path)
    print("*" * 100)
    print(f)
    print("*" * 100)
    print(py)
"""
fl = readxlrd( filename1 )
print( fl )
"""