import json
import sys


def hello(test):

    dic = ['1','2','3']
    dic.append(test)
    return json.dumps(dic)


if __name__ == "__main__":
    print(hello(sys.argv[1]))


