# -*- encoding=utf8 -*-
__author__ = "xr"

import logging
import signal
import sys
import traceback
from multiprocessing import Process
from airtest.core.api import *
from airtest.core.settings import Settings as ST
import atexit

ST.OPDELAY = 1
auto_setup(__file__)
logger = logging.getLogger("airtest")
logger.setLevel(logging.WARNING)
global 辅助
# 版本检测 信号处理
if sys.version < '3':
    print("请使用 Python3 运行此脚本")

try:
    import airtest.core.api  # XXX 要验证是否安装的库名
except ImportError:
    print("模块不存在, 尝试安装")
    import pip

    try:
        pip.main(['install', 'airtest', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple'])
    except:
        print("安装失败")
        exit(1)
'''
小技巧:
    在人机试炼选英雄界面，显示全部英雄，选择你想用的英雄线路页面，别点击英雄, 截图, 王者放后台，打开相册
'''
# --------------------- 自定义信息 --------------------->
设备类型 = "Android"  # 设备类型？(Android/Windows/iOS)
设备IP地址 = "192.168.12.164"  # 设备IP地址:端口号 默认: (IOS: IP地址:8100 Android: IP地址:5555)

phone='Android:///192.168.12.164:5555'
logger.warning('主英雄pid')
sleep(0.5)
logger.warning('主英雄pid')


