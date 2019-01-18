import os
import re
from shutil import copyfile

class CheckSql:
    def __init__(self, dpath):
        self.dpath = dpath

    # def findSbinsh(self, templateDir, shname):
    #     """
    #     :param templateDir:
    #     :param shname:
    #     :describe:根据传入的shname确定需要修改的脚本名
    #     :return: filename
    #     """
    #     filedic = {"tfile": "3.mkafadir.sh",
    #                "fofile": "4.mkafedir.sh",
    #                "pybakfile": "6.afa_workspace_pybak.sh",
    #                "copyfile": "7.cppy_update.sh",
    #                "fbapDB": "51.db2_insert_fbap_auto.sh",
    #                "bsmsDB": "52.db2_insert_bsms.sh",
    #                "cfg": "cfgadd.sh",
    #                "cfgadd": "fbap_afa_afe_comm.conf.add"
    #     }
    #     pybak = "pybak"
    #     print("根据shname, 确定需要被拼接的脚本名")
    #     print("shname=[%s]" % shname)
    #
    #     if re.match("TS_\d{5}_X_\d{8}.sh", shname):
    #         print("属于DB部署脚本")
    #         filename = os.path.join(templateDir, filedic["fbapDB"])
    #         with open(filename, "rw+") as fn:
    #             pass
    #
    #         print(filename)
    #         return filename
    #     elif pybak in shname:
    #         filename = os.path.join(templateDir, filedic["pybakfile"])
    #         print("filename")
    #         return filename


    def __SpliceAdd(self):
        """
        :function:自动添加fbap_afa_afe_comm.conf.add
        :return:
        """
        pass

    def __SpliceSh(self, filename, lpath, fdir, shname):
        """
        name:__SpliceSh
        function:查看拼接指令是否在sh脚本中存在，如果不存在，则拼接操作指令
        """
        print("【------开始组装sh脚本[%s]------】" % filename)
        print("任务编号[%s]" % fdir)
        print('脚本名:[%s]' % shname)
        ppath = os.path.join(lpath, fdir)
        print(ppath)

        flag = True
        startflag = "satrtflag"
        install = "install "

        os.chdir(ppath)
        nfilename = "22222222222.txt"
        os.rename(filename, nfilename)
        with open(nfilename, "r") as f:
            with open(filename, 'w+') as fn:
                for dd in f:
                    # 拼接：tmp = 'install XQ-2018-791 TR_45871_X_20181210.sh'
                    tmp = install + fdir + " " + shname
                    print('tmp = [%s]' % tmp)
                    if startflag in dd:
                        fn.write(tmp)
                    elif install in dd and flag == True:
                        fn.write(dd)
                        fn.write(tmp)
                        flag = False
                    else:
                        fn.write(dd)

        os.remove(nfilename)            #删除nfielname,防止处理下个文件报错

    def __FindSbin(self, lpath, fdir, shname):

        """
        name:__FindSbin
        function:查找sbin目录是否存在，如果不存在，则创建目录，并添加sh脚本
        """
        templateDir = "F:\\黄小宝的宝\\script\\sbin"         #sbin模板的路径
        print("***********开始查找[%s]下是否存在sbin目录***********" % lpath)
        sbin = "sbin"
        delete = "delete"
        if sbin not in os.listdir(lpath):
            os.chdir(lpath)
            os.mkdir(sbin)
            os.chdir(fdir)
            sbindir = os.path.join(lpath, sbin)

            if re.match("TS_\d{5}_X_\d{8}.sh", shname):

                #检查8.AMICInit.sh脚本是否存在,如果不存在，则将文件拷贝过来
                if "8.AMICInit.sh" not in os.listdir(sbindir):
                    copyfile(os.path.join(templateDir, "8.AMICInit.sh"), os.path.join(sbindir, "8.AMICInit.sh"))

                """判断shname安装手册是否提示部署"""
                """此处调用函数判断"""
                with open(shname, 'r') as f:
                    for dd in f:
                        if ".sql" in dd:
                            #从"db2 -tvf ./TS_75760_FBAP_D_20190117_01.sql|tee -a $LOGSNAME"切割出.sql文件名
                            sqlfile = dd.split("./")[1].split("|")[0]
                            print(sqlfile)
                            """判断sqlfile是否存在"""
                            if sqlfile not in os.listdir(os.getcwd()):
                                print("[%s]调用的[%s]不存在，请确认" % (shname, sqlfile))
                                raise EOFError
                            else:   #检查部署的sql文件中是否包含delete语句
                                with open(sqlfile) as fsql:
                                    for tmp in fsql:
                                        if delete in tmp or delete.upper() in tmp:
                                            print("部署的[%s]文件中包含delete语句，请开发人员确认" % sqlfile)
                                            raise EOFError
                sbinShName = "51.db2_insert_fbap_auto.sh"
            elif "pybak" in shname:
                sbinShName = "6.afa_workspace_pybak.sh"

            t = os.path.join(templateDir, sbinShName)
            filename = os.path.join(os.path.jion(lpath, sbin), sbinShName)

            if os.path.isfile(t) and sbinShName not in os.listdir(os.path.jion(lpath, sbin)):
                copyfile(t, filename)
                #查找需要被拼接的脚本
                # 开始拼接sh脚本
                self.__SpliceSh(filename, lpath, fdir, shname)

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
                        # if t[1] == ".sh" and pybak in t[0]:
                        if t[1] == ".sh":
                            self.__FindSbin(lpath, fdir, ffile)


    def checkSh(filename):
        pass