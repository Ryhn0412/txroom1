import os
import zipfile


# 通用工具类，压缩文件方法
# 压缩方法
def make_zip(source_dir, output_filename):
    '''
    用于将测试报告打包成zip格式
    :param source_dir: 测试报告路径
    :param output_filename: 打包的文件名
    :return: 打包文件
    '''
    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)
            zipf.write(pathfile, arcname)
    zipf.close()
