
import json
import sys


def hello():
    dic = ['1','2','3']
    return json.dumps(dic)


if __name__ == "__main__":
    print(hello())

