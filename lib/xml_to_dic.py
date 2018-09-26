# coding=utf-8
# author:luhu
import time
import xml.etree.ElementTree as ET
start = time.clock()  # 记录处理开始时间；与最后一行一起使用，来判断输出运行时间。

tree = ET.ElementTree(file='API/API.xml')
root = tree.getroot()   # 获取根元素


def xml_to_url():
    for elem in tree.iter(tag='URL'):
        url = elem.text
    return url


def xml_to_body():
    data = {}
    for elem in tree.iterfind('*body/'):
        data[elem.tag] = elem.text
    return data


end = time.clock()
if __name__ == '__main__':
    body = xml_to_body()
    print(xml_to_body())
    url = xml_to_url()
    print(url)
    print("read: %f s" % (end - start))
