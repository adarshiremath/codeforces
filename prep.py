import os
with open('./test.txt') as f:
    lines = f.readlines()
    lines = lines[0].strip().split("  ")
    dir = "./Contest-" + lines[1] + "/"
    os.mkdir(dir)
    f1 = open(dir+"_".join(lines[0].split(" ")).strip()+".py","x")
    f1.close()
