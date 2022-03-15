import os

import yaml as pyyaml


def get_yaml(yaml_file):
    '''
    转义yaml文件数据，使得python编辑器读得懂
    :param yaml_file: yaml路径
    :return:
    '''
    with open(yaml_file, "r", encoding="utf-8") as fp:
        # 以字符串的形势读取ymal中的数据
        f = fp.read()
        print(type(f))
    d = pyyaml.unsafe_load(f)
    print('读取到yaml文件数据')
    print(type(d))
    return d


def yaml_locator(path=None):
    '''
    获取yaml的路径（通过partition方法分割字符串）
    path:填写从text_object后的文件路径
    :return: 
    '''
    # file1 = get_yaml() 读取yaml文件
    # os.path.join() 拼接地址
    # 获取路径地址
    a = os.getcwd()
    try:
        list1 = a.partition(r'tx')
        print(list1[0])
        b = os.path.join(list1[0] + r'tx\text_object' + path)
        print(b)
        return b
    except:
        print('yaml获取路径有误')
