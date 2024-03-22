# 封装日志模板,定制日志
# 一是存放目录问题,我们这里使用了固定目录
# 二是日志分割,滚动问题,每天持续继承,大量用例生成大量日志,有用的日志搞个ELK把日志取走存放起来做分析,每日用的就保存几天删掉,需要实现日志分割和滚动.
# logging模块有这个功能,配置一下就可以
import os
import logging

from logging.handlers import TimedRotatingFileHandler
from Conf.config import log_cfg
# 把项目的根路径取出来,把上面config.ini中的日志配置取过来,最后拼接好日志文件存放的绝对路径
_BaseHome = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

_log_level = eval(log_cfg['log_level'])  #如果不使用eval函数,log_level取过来是字符串,没法直接使用,通过eval执行后就变成了logging定义的对象了
_log_path = log_cfg['log_path']
_log_format = log_cfg['log_format']

_log_file = os.path.join(_BaseHome,_log_path,'log.txt')


# 配置日志,TimedRotatingFileHandler这个实现滚动日志


def log_init():
    logger = logging.getLogger('main')
    logger.setLevel(level=_log_level)
    formatter = logging.Formatter(_log_format)
# handler用于向日志文件打印日志
    handler = TimedRotatingFileHandler(filename=_log_file,when="D",interval=1,backupCount=7)
    handler.setLevel(_log_level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# console用于向终端打印日志
    console = logging.StreamHandler()
    console.setLevel(_log_level)
    console.setFormatter(formatter)
    logger.addHandler(console)

# TimedRotatingFileHandler参数简介
# filename 日志文件
# when 切割条件 按周(W),天(D),时(H),分(M),秒(S)切割
# interval 间隔 就是几个when切割一次,when是W,interval是3的话就是代表3周切割一次
# backupCount 日志备份数量 就是保留几个日志文件,超过 这个数量就把最早的删除掉,从而滚动删除
# 这里配置的是每天生成一个日志文件,保留七天的日志

#测试
# log_init()
# logger = logging.getLogger('main')
# logger.info('log test ______________________')

# 其他文件使用日志:
# 先在main.py里面引入这个log_init(),在最开始的时候初始化一下,日志就配置好了
# 再在各个要使用的日志文件中,直接按下面方法使用:
# import logging
# logger = logging.getLogger('main.jd')
# 注意各个模块自己getLogger的时候，直接main后面加上“.模块名”，就能使用同一个logger区分模块了。

# 截图功能,截图文件也需要滚动删除,这个待补充
from PIL import ImageGrab
import time
# 先定义截图文件存放路径,这里在Log目录下建个screen目录,按天存放截图
_today = time.strftime("%Y%m%d")
_screen_path = os.path.join(_BaseHome,_log_path,'Screen',_today)

# 使用PIL的ImageGrab实现截图
def screen(name):
    t = time.time()
    png = ImageGrab.grab()
    if not os.path.exists(_screen_path):
        os.makedirs(_screen_path)
    image_name = os.path.join(_screen_path,name)
    png.save('%s_%s.png'%(image_name,str(round(t*1000))))#文件名后面加了时间戳避免重名

# 调用screen函数对当前屏幕截图
# screen("screenshot")