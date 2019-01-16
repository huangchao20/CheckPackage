import os
import re
from shutil import copyfile

class CheckSql:
    def __init__(self, dpath):
        self.dpath = dpath

    def findSbinsh(self, templateDir, shname):
        """
        :param templateDir:
        :param shname:
        :describe:根据传入的shname确定需要修改的脚本名
        :return: filename
        """
        filedic = {"tfile": "3.mkafadir.sh",
                   "fofile": "4.mkafedir.sh",
                   "pybakfile": "6.afa_workspace_pybak.sh",
                   "copyfile": "7.cppy_update.sh",
                   "fbapDB": "51.db2_insert_fbap_auto",
                   "bsmsDB": "52.db2_insert_bsms.sh",
                   "cfg": "cfgadd.sh",
                   "cfgadd": "fbap_afa_afe_comm.conf.add"
        }
        pybak = "pybak"
        print("根据shname, 确定需要被拼接的脚本名")
        print("shname=[%s]" % shname)

        if re.match("TS_\d{5}_X_\d{8}.sh", shname):
            print("属于DB部署脚本")
            filename = os.path.join(templateDir, filedic["fbapDB"])
            with open(filename, "rw+") as fn:
                pass

            print(filename)
            return filename
        elif pybak in shname:
            filename = os.path.join(templateDir, filedic["pybakfile"])
            print("filename")
            return filename

    def __SpliceSh(self, filename, fdir, shname):
        """
        name:__SpliceSh
        function:查看拼接指令是否在sh脚本中存在，如果不存在，则拼接操作指令
        """
        print("【------开始组装sh脚本[%s]------】" % filename)
        if os.path.isfile(filename):
            pass

    def __FindSbin(self, lpath, fdir, shname):
        """
        name:__FindSbin
        function:查找sbin目录是否存在，如果不存在，则创建目录，并添加sh脚本
        """
        templateDir = "F:\\黄小宝的宝\\script\\sbin"         #sbin模板的路径
        print("***********开始查找[%s]下是否存在sbin目录***********" % lpath)
        sbin = "sbin"
        if sbin not in os.listdir(lpath):
            os.chdir(lpath)
            os.mkdir(sbin)
            t = os.path.join(templateDir, shname)
            m = os.path.jion(lpath, sbin)
            if os.path.isfile(t):
                copyfile(t, m)
                #查找需要被拼接的脚本
                filename = self.findSbinsh(templateDir, shname)
                # 开始拼接sh脚本
                self.__SpliceSh(filename, fdir, shname)

    def FindSh(self):
        print("**************开始查找sh脚本**************")
        print("dpath: ", self.dpath)
        pybak = "pybak"
        # pdir = ["TR", "BUG", "XQ"]
        if os.path.isdir(self.dpath):
            for fdir in os.listdir(self.dpath):
                if fdir.startswith(("TR", "BUG", "XQ")):
                    # 拼接目录lpath，如：dpath = "F:\TFS_l\文档&DB&AFEjar包\2019常规\20190110", fdir="BUG-2018-612"
                    lpath = os.path.join(self.dpath, fdir)
                    print("lpath:[%s]" % lpath)
                    #开始查找sh脚本
                    os.chdir(lpath)
                    #ffile存放sh脚本的文件名的临时容器
                    for ffile in os.listdir(lpath):
                        t = os.path.splitext(ffile)
                        if t[1] == ".sh" and pybak in t[0]:
                            self.__FindSbin(lpath, fdir, ffile)

    def checkSh(filename):
        pass