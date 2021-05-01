import sys
import random

def main():
    f = open("去重", "r")
    e = open("是什么", "r")
    all = f.readlines()
    what = e.readlines()
    # 随机取
    length = int(sys.argv[1]) # 行长
    lines = int(sys.argv[2]) # 个数

    for i in range(0, lines):
        out = "该生"
        while len(out) < length:
            out += all[random.randint(0, len(all) - 1)].rstrip("\n")
            if random.random() > 0.5:
                out += "，"
            else:
                out += "。"
        out += what[random.randint(0, len(what) - 1)].rstrip("\n")
        print(out)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("参数：行长 行数")
    else:
        main()