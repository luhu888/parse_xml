# coding=utf-8
# author:luhu

from xml.dom.minidom import parse
import xml.dom.minidom


# dom解析：将XML数据在内存中解析成一个树，通过对树的操作来操作XML
# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("movie.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element : %s" % collection.getAttribute("shelf"))

movies = collection.getElementsByTagName("movie")
# 在集合中获取所有电影

# 打印每部电影的详细信息
for movie in movies:
    print("*****Movie*****")
    if movie.hasAttribute("title"):
        print("Title: %s" % movie.getAttribute("title"))

    type = movie.getElementsByTagName('type')[0]
    print("Type: %s" % type.childNodes[0].data)
    format = movie.getElementsByTagName('format')[0]
    print("Format: %s" % format.childNodes[0].data)
    rating = movie.getElementsByTagName('rating')[0]
    print("Rating: %s" % rating.childNodes[0].data)
    description = movie.getElementsByTagName('description')[0]
    print("Description: %s" % description.childNodes[0].data)
for elem in DOMTree.iter(tag='API'):
    print(elem.tag, elem.attrib)
