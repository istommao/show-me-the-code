"""
第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
"""
import random
import string


def random_str(length=8):
    lst = list(string.ascii_letters)
    random.shuffle(lst)
    return ''.join(lst[:length])


def main(n):
    dataset = {random.randint}
    while 1:
        if len(dataset) > n:
            break
        data = random_str()
        if data in dataset:
            continue
        else:
            dataset.add(data)

    print(dataset)


if __name__ == '__main__':
    main(200)
