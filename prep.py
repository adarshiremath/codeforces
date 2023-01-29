import os
with open('./test.txt') as f:
    lines = f.readlines()
    dir = "./Contest-1/"
    os.mkdir(dir)
    for line in lines:
        f1 = open(dir+"_".join(line.split(" ")).strip()+".py","x")
        f1.close()
