"""
第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
请将上述内容写到 city.xls 文件中，如下图所示：

city.xls


"""
import json


def main():
    with open('city.txt') as file_p:
        data = json.loads(file_p.read())
    print(data)

if __name__ == '__main__':
    main()
