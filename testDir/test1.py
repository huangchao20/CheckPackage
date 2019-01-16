

def openfile(filename):
    flag = True
    with open(filename, 'r+') as f:
        for dd in f:
            if "install" in dd and flag == True:
                ndd = "\n" + filename
                print("*********************" + ndd)
                # f.
                flag = False

if __name__ == '__main__':
    filename = "F:\\黄小宝的宝\\测试目录\\1111111111.txt"
    openfile(filename)