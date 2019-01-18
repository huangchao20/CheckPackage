import docx
from docx import Document#导入库

def getdocxTable(dpath):
    # path = "E:\\python_data\\1234.docx"#文件路径
    print(dpath)
    document = Document(dpath)#读入文件
    tables = document.tables #获取文件中的表格集
    print('-0-0-0-0-0-0-0-0-0-0-0-0-')
    # for t in tables:
    #     print(t)
    # print('-0-0-0-0-0-0-0-0-0-0-0-0-')
    # try:
    #     table = tables[3]#获取文件中的第一个表格
    #     for i in range(1, len(table.rows)):  # 从表格第二行开始循环读取表格数据
    #         result = table.cell(1, 0).text
    #         print(result)
    # except Exception as e:
    #     print(e)
    for table in tables:
        for i in range(1, len(table.rows)):
            result = table.cell(1, 0).text
            if "PORT" in result:
                print(result)


if __name__ == '__main__':
    dpath = "E:\\SVN\\2019\\20190117w\特色业务产品\\fbap.20190117rw.t10\\XQ-2018-852\\TS_76756_安装操作手册.docx"
    getdocxTable(dpath)