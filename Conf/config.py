# 读取config.ini
import os
from configparser import ConfigParser
# 使用相对目录确定文件位置
_conf_dir = os.path.dirname(__file__)
_conf_file = os.path.join(_conf_dir,'config.ini')

# 继承ConfigParser,写一个将结果转化为dict的方法
class MyParser(ConfigParser):
    def as_dict(self):
        d = dict(self._sections)#在 ConfigParser 类中，self._sections 是一个内部属性，用于存储配置文件中所有的部分（sections）及其对应的键值对。
        for k in d:
            d[k] = dict(d[k])
        return d


# 读取所有配置,以字典的方式输出结果
def _get_all_conf():
    _config = MyParser()
    result = {}
    if os.path.isfile(_conf_file):
        try:
            _config.read(_conf_file,encoding='UTF-8')
            result = _config.as_dict()
        except OSError:
            raise ValueError("Read config file failed: %s" % OSError)
        return result


# 将各配置读取出来,放在变量中,后续其他文件直接引用这些变量
config = _get_all_conf()
sys_cfg = config['sys']
smtp_cfg = config['smtp']
email_cfg = config['email']
#把Log相关的配置放在一个变量中,方便使用
log_cfg = config['Log']

print(sys_cfg)
print(smtp_cfg)
print(smtp_cfg['host'])
print(log_cfg)



