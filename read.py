# -*-encoding=utf-8-*-
# 测试ConfigParser
import os
from configparser import ConfigParser

# 初始化
config = ConfigParser()

# 配置文件的绝对路径
config_path = os.path.dirname(os.path.realpath(__file__)) + "/config.ini"

# 读取配置文件
config.read(filenames=config_path, encoding='UTF-8')

"""
读取配置信息
"""
# 查看配置中的所有section节点【返回值以列表方式存放了所有section节点名】
sections = config.sections()
print(sections, "所有的sections")

# 返回指定section节点中的的所有option名称【返回值是列表的方式】
section_options = config.options(section="mysql")  # 返回section中option的值
print(section_options)
value = config.get(section="mysql", option="host")
print(value, 'value')

# 是否有这个section
print(config.has_section(section="ip1"))
print(config.items(section="Mail"))