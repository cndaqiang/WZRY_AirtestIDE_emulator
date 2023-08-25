# -*- encoding=utf8 -*-
#可以这样命令行中运行
'''
(base) cndaqiang@macmini mac$ 
/Applications/AirtestIDE.app/Contents/Resources/plugins/firebase_plugin/tool/copy_app/airtest/core/android/static/adb/mac/adb devices
List of devices attached
adb server version (40) doesn't match this client (39); killing...
* daemon started successfully *
8553e6ac	device

(base) cndaqiang@macmini mac$ 
/Applications/AirtestIDE.app/Contents/Resources/plugins/firebase_plugin/tool/copy_app/airtest/core/android/static/adb/mac/adb tcpip 5555
restarting in TCP mode port: 5555

"/Applications/AirtestIDE.app/Contents/MacOS/AirtestIDE" pyrunner "/Users/cndaqiang/Desktop/WZRY_AirtestIDE-main/XiaoMI11.py" 
#windows， cmd可以，powershell不行
#C:\\Users\cndaqiang\Videos\AirtestIDE\airtest\core\android\static\adb\windows\adb.exe devices
#"C:\\Users\cndaqiang\Videos\AirtestIDE\AirtestIDE" pyrunner #"C:\\Users\cndaqiang\Desktop\WZRY_AirtestIDE-main 2\WZRY_AirtestIDE-main\XiaoMI11.py"
'''
__author__ = "xr"

import logging
import signal
import sys
import os
import traceback
from multiprocessing import Process
from airtest.core.api import *
from airtest.core.settings import Settings as ST
import atexit
import numpy as np

port=5555
ST.OPDELAY = 1
# 全局阈值的范围为[0, 1]
ST.THRESHOLD_STRICT = 0.7  # assert_exists语句的默认阈值，一般比THRESHOLD更高一些
ST.THRESHOLD = 0.7  # 其他语句的默认阈值
#@如何设置minicap https://www.jianshu.com/p/71fa5c81246d
auto_setup(__file__)
logger = logging.getLogger("airtest")
logger.setLevel(logging.WARNING)
global 辅助
global 青铜段位
global 返回房间
global 快速点击
global 保存位置
青铜段位=False
快速点击=True #如果自己已经提前预选好了很多东西,就不用再加以判断了
返回房间=True #第二次运行后直接返回房间
保存位置=True #当为Flase时,清空保存结果


#一些变量可以保存,重复运行不用读入
global position_dict
global position_dict_file
position_dict={}
import pickle
position_dict_file="position_dict.txt"
if os.path.exists(position_dict_file):
    logger.warning("读取"+position_dict_file)
    with open(position_dict_file, 'rb') as f:
        position_dict = pickle.load(f)
def save_dict():
    #保存变量
    global position_dict
    global position_dict_file
    f = open(position_dict_file, "wb") 
    pickle.dump(position_dict, f)
    f.close

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
设备IP地址 = "192.168.12.152"  # 设备IP地址:端口号 默认: (IOS: IP地址:8100 Android: IP地址:5555)


次数 = 20  # 对战次数设置 一次大概27点经验

想玩位置 = Template(r"tpl1686048521443.png", record_pos=(-0.34, 0.063), resolution=(2400, 1080))
#不要设置这个


# `对战` -> `5v5 王者峡谷` -> `人机` -> `开始练习` 组队页面修改想玩的位置


参战英雄=Template(r"tpl1689218509411.png",threshold=0.4, record_pos=(0.107, 0.011), resolution=(2400, 1080))
#Template(r"tpl1689175760820.png",  threshold=0.4, record_pos=(0.25, -0.064), resolution=(2400, 1080))



参战英雄线路 =Template(r"tpl1688913050073.png", record_pos=(-0.163, -0.209), resolution=(2400, 1080))




备战英雄 =Template(r"tpl1688912981272.png", record_pos=(-0.052, 0.105), resolution=(2400, 1080))

 # `对战` -> `5v5 王者峡谷` -> `人机` -> `开始练习` -> `开始匹配` -> `英雄页面选择你想用的备选英雄`

备战英雄线路 = Template(r"tpl1688913020289.png", record_pos=(-0.276, -0.21), resolution=(2400, 1080))


  # `对战` -> `5v5 王者峡谷` -> `人机` -> `开始练习` -> `开始匹配` -> `英雄页面选择你想用的备选英雄的线路`


# <--------------------- 辅助 --------------------->
辅助 = False

辅助设备类型 = "Android"  # 设备类型？(Android/Windows/iOS)
辅助设备IP地址 = "127.0.0.1"  # 设备IP地址:端口号 默认: (IOS: IP地址:8100 Android: IP地址:5555)
辅助次数 = 20  # 对战次数设置 一次大概27点经验

辅助想玩位置 = Template(r"中路位置.png", record_pos=(-0.429, -0.009), resolution=(2400, 1080))  # `对战` -> `5v5 王者峡谷` -> `人机` -> `开始练习` 组队页面修改想玩的位置
辅助参战英雄 = Template(r"米莱狄.png", record_pos=(-0.452, -0.133), resolution=(2400, 1080))  # `对战` -> `5v5 王者峡谷` -> `人机` -> `开始练习` -> `开始匹配` -> `英雄页面选择你想用的英雄`
辅助参战英雄线路 = Template(r"中路线路.png", record_pos=(-0.07, -0.305), resolution=(2400, 1080))  # `对战` -> `5v5 王者峡谷` -> `人机` -> `开始练习` -> `开始匹配` -> `英雄页面选择你想用的英雄的线路`
辅助备战英雄 = Template(r"刘禅.png", record_pos=(-0.454, -0.126), resolution=(2400, 1080))  # `对战` -> `5v5 王者峡谷` -> `人机` -> `开始练习` -> `开始匹配` -> `英雄页面选择你想用的备选英雄`
辅助备战英雄线路 = Template(r"辅助线路.png", record_pos=(0.177, -0.306), resolution=(2400, 1080))  # `对战` -> `5v5 王者峡谷` -> `人机` -> `开始练习` -> `开始匹配` -> `英雄页面选择你想用的备选英雄的线路`


# <--------------------- 自定义信息 ---------------------
def existsTHENtouch(png=Template(r"1.png"),str="",savepos=False):
    savepos=savepos and len(str) > 0
    global position_dict
    global 保存位置
    if not 保存位置: position_dict={}
    if savepos:
        if str in position_dict.keys():
            touch(position_dict[str])
            logger.warning("touch (saved) "+str)
            sleep(0.1)
            return True
    pos=exists(png)
    if pos:
        touch(pos)
        if len(str) > 0: logger.warning("touch "+str)
        if savepos: position_dict[str]=pos
        return True
    else:
        if len(str) > 0:
            logger.warning("NotFound "+str)
        return False
def 异常处理_返回大厅():
    logger.warning("进入异常处理")

    logger.warning("[异常]检测大厅")
    if 大厅中():
        return
    logger.warning("[异常]检测对战")
    if 对战中():
        sleep(60)
        while 对战中(): sleep(60)
        游戏结束()
        异常处理_返回大厅()
        return
    # 健康系统
    #> 先不考虑健康系统 
    健康系统()
    # 返回
    logger.warning("[异常]检测返回")
    if exists(Template(r"tpl1685443444352.png", record_pos=(-0.42, -0.203), resolution=(2400, 1080))):
        logger.warning("返回")
        touch(Template(r"tpl1685443444352.png", record_pos=(-0.42, -0.203), resolution=(2400, 1080)))
    #
    # 广告直播
    logger.warning("[异常]检测广告")
    for i in range(5):
        if exists(Template(r"关闭广告.png", record_pos=(0.429, -0.205), resolution=(2400, 1080))):
            logger.warning("第 {} 次关闭广告".format(i + 1))
            touch(Template(r"关闭广告.png", record_pos=(0.431, -0.203), resolution=(2400, 1080)))
        else:
            break
    # 点击屏幕继续
    logger.warning("[异常]检测点解屏幕继续")
    if exists(Template(r"点击屏幕继续.png", record_pos=(0.002, 0.287), resolution=(2400, 1080))):
        logger.warning("点击屏幕继续")
        touch(Template(r"点击屏幕继续.png", record_pos=(0.002, 0.287), resolution=(2400, 1080)))
    #
    sleep(10)


def 进入房间(times=1):
    global 返回房间
    global 快速点击
    if 房间中():
        return
    times=times+1
    if times > 10:
        logger.warning("无法进入房间")
        os.kill(os.getpid(), signal.SIGINT)  # 退出程序
    #
    异常处理_返回大厅()
    #wait等待元素出现，没出现就执行intervalfunc
    if not existsTHENtouch(Template(r"tpl1688913288211.png", record_pos=(-0.081, 0.11), resolution=(2400, 1080)),"对战",savepos=True):
        #touch()

        logger.error("选择对战失败")
        进入房间(times); return
    sleep(2)
    if not existsTHENtouch(Template(r"tpl1685431293206.png", record_pos=(-0.315, 0.078), resolution=(2400, 1080)),"5v5王者峡谷",savepos=True):
        进入房间(times); return
    sleep(2)
    if not existsTHENtouch(Template(r"tpl1685431315731.png", record_pos=(0.049, 0.071), resolution=(2400, 1080)),"人机"):
        进入房间(times); return        
    sleep(2)
    if not 快速点击:
        if not existsTHENtouch(Template(r"tpl1685431620909.png", record_pos=(-0.246, -0.017), resolution=(2400, 1080)),"快速模式"):
        #if not existsTHENtouch(Template(r"tpl1685671589634.png", record_pos=(-0.245, -0.108), resolution=(2400, 1080)),"标准模式"):
            进入房间(times); return         
        #
        # 选择难度
        global 青铜段位
        青铜段位=True
        if 青铜段位:
            段位=Template(r"tpl1685431397853.png", record_pos=(0.009, -0.117), resolution=(2400, 1080))
        else:
            段位=Template(r"tpl1685515575284.png", record_pos=(-0.031, 0.092), resolution=(2400, 1080))
        existsTHENtouch(段位,"选择段位")
    #
    # 开始练习
    开始练习 = Template(r"tpl1685431440002.png" ,threshold=0.8, record_pos=(0.253, 0.128), resolution=(2400, 1080))
    if not existsTHENtouch(开始练习,"开始练习"): os.kill(os.getpid(), signal.SIGINT)  # 退出程序
    sleep(2)
    #
    #当没有弹出确定匹配时
    if not exists(Template(r"tpl1685431840269.png", record_pos=(0.127, 0.187), resolution=(2400, 1080))):
        sleep(2) 
        #如果还有快速模式，次数用光
        if not 快速点击:
            if exists(Template(r"tpl1685671644385.png", threshold=0.8, record_pos=(-0.319, -0.202), resolution=(2400, 1080))):
                logger.warning("次数用完")
                青铜段位=True
                existsTHENtouch(Template(r"tpl1685431397853.png", record_pos=(0.009, -0.117), resolution=(2400, 1080)),"青铜段位")
                # 
                if not existsTHENtouch(开始练习,"开始练习"): os.kill(os.getpid(), signal.SIGINT)  # 退出程序
        #有时候长时间不进去被禁赛了
        while existsTHENtouch(Template(r"tpl1685687139718.png", threshold=0.8, record_pos=(-0.006, 0.091), resolution=(2400, 1080))):
            logger.warning("不同意被禁赛了")
            sleep(30)
            if not existsTHENtouch(开始练习,"开始练习"): os.kill(os.getpid(), signal.SIGINT)
        
        #


        if False: #没必要
            # 选择路线
            btn_pos = wait(Template(r"tpl1685431774988.png", record_pos=(-0.312, -0.073), resolution=(2400, 1080)), intervalfunc=异常处理)
            try:
                if btn_pos:
                    touch(Template(r"tpl1685431774988.png", record_pos=(-0.312, -0.073), resolution=(2400, 1080)))
                if exists(英雄属性["想玩位置"]):
                    logger.warning("选择 想玩的位置")
                    touch(英雄属性["想玩位置"])
            except:
                logger.error("选择 想玩的位置 失败")

        #>  邀请辅助()
        if not 房间中():
            进入房间(times)
            return
    
def 匹配游戏():
    # 开始人机对局
    #Template图像识别代码
    #threshold：识别阈值，浮点类型，范围是[0.0, 1.0]，默认0.7
    #record_pos: pos in screen when recording
    #resolution: screen resolution when recording
    #小米11 1440x3200 
    #获得分辨率 adb shell dumpsys window display
    #record_pos和resolution只是为了加速，都可以识别的
    if 英雄属性["type"]:
        #
        进入房间()
        # 开始匹配
        looptimes=5
        logger.warning("开始匹配")
        for loop in range(looptimes):
            if existsTHENtouch(Template(r"tpl1685431840269.png", record_pos=(0.127, 0.187), resolution=(2400, 1080))):
                break
            sleep(1)
        
        logger.warning("确认匹配")
        队友确认匹配=False
        # 确认匹配
        for loop in range(60*5*10):#等待时间太长
            if existsTHENtouch(Template(r"tpl1685431876071.png", record_pos=(-0.004, 0.122), resolution=(2400, 1080))):
                #英雄和皮肤按钮出来才可以
                for loop2 in range(60*5*2): #等待进入英雄界面
                    if exists(Template(r"tpl1685425713708.png", record_pos=(-0.371, -0.206), resolution=(2400, 1080))):
                         队友确认匹配=True
                         break
                    sleep(1)
                if 队友确认匹配: break
            sleep(1)
        #选择英雄
        if True:
            #显示全部英雄.png
            existsTHENtouch(Template(r"tpl1685425741770.png", record_pos=(-0.285, -0.012), resolution=(2400, 1080)),"展开英雄",savepos=True)
            existsTHENtouch(英雄属性["参战英雄线路"],"参战英雄线路",savepos=True)
            existsTHENtouch(英雄属性["参战英雄"],"参战英雄",savepos=True)
            #分路重复.png
            if exists(Template(r"tpl1685426207941.png", record_pos=(0.005, -0.126), resolution=(2400, 1080))):
                logger.warning("分路冲突，切换英雄")
                #分路重复取消按钮.png
                existsTHENtouch(Template(r"tpl1685426213846.png", record_pos=(-0.073, 0.152), resolution=(2400, 1080)),"冲突取消英雄",savepos=True)
                #选择备选英雄
                existsTHENtouch(英雄属性["备战英雄线路"],"备战英雄线路",savepos=True)
                existsTHENtouch(英雄属性["备战英雄"],"备战英雄",savepos=True)
            #确定英雄后一般要等待队友确定，这需要时间
            sleep(5)
            #   确定
            existsTHENtouch(Template(r"tpl1685425856227.png", record_pos=(0.389, 0.192), resolution=(2400, 1080)),"确定英雄",savepos=True) #这里是用savepos的好处就是那个英雄的熟练度低点哪个英雄
            sleep(5)
            #万一是房主
            existsTHENtouch(Template(r"tpl1685425856227.png", record_pos=(0.389, 0.192), resolution=(2400, 1080)),"确定阵容",savepos=True)
            sleep(5)
        sleep(20)
        #加油拳头
        existsTHENtouch(Template(r"tpl1685432367512.png", record_pos=(0.34, 0.0), resolution=(2400, 1080)),"加油按钮",savepos=True)
        logger.warning("等待游戏结束...倒计时")
        #sleep(350) #游戏时间很长的,倒计时转移到游戏结束()



def 启动王者荣耀():
    logger.warning("连接设备")
    if device:
        logger.warning("设备连接成功")
    else:
        logger.warning("设备连接失败")
        return
    logger.warning("启动 王者荣耀")
    #   我们提前打开软件了就直接return了
    if 大厅中():
        return
    elif 房间中():
        return
    else:
       for i in range(5): #尝试异常处理
           异常处理_返回大厅()
           sleep(1)
           if 大厅中():
               return
    if not 大厅中():
        logger.warning("无法进入大厅")
        os.kill(os.getpid(), signal.SIGINT)
    #暂时不进行重启游戏
    return


def 大厅中():
    if exists(Template(r"tpl1685498765938.png", threshold=0.9, record_pos=(-0.142, 0.115), resolution=(2400, 1080))):
        logger.warning("正在大厅中")
        return True


def 对战中():
    if exists(Template(r"tpl1685442267997.png", threshold=0.9, record_pos=(0.34, 0.163), resolution=(2400, 1080))):
        logger.warning("正在对战中")
        return True

def 房间中():
    if exists(Template(r"tpl1686109413605.png", record_pos=(-0.003, -0.024), resolution=(2400, 1080))):
        logger.warning("正在房间中")
        return True
    else:
        return False

def 健康系统():
    #呵护双眼，请您休息
    if exists(Template(r"tpl1685521273063.png", record_pos=(0.1, -0.08), resolution=(2400, 1080))):
        logger.warning("您已禁赛")
        touch(Template(r"tpl1685521315211.png", record_pos=(0.158, 0.066), resolution=(2400, 1080)))
        stop_app(设备信息["王者应用ID"])
        os.kill(os.getpid(), signal.SIGINT)  # 退出程序
        # start_app(设备信息["王者应用ID"])
        sleep(900)
        启动王者荣耀()
        raise Exception("您已禁赛")
    return


def 游戏结束():
    jixu=False
    global 返回房间
    while True:
        # 
        健康系统()
        #分享和返回房间的按键有些冲突
        #
        #有时候会莫名进入分享界面
        if exists(Template(r"tpl1686118081785.png", record_pos=(0.12, 0.186), resolution=(2400, 1080))):
            logger.warning("分享界面")
            existsTHENtouch(Template(r"tpl1685521173525.png", threshold=0.9, record_pos=(-0.453, -0.2), resolution=(2400, 1080)))
            jixu=True
            sleep(2)
        
        #有时候会莫名进入MVP分享界面
        pos=exists(Template(r"tpl1685521150370.png", record_pos=(0.186, -0.13), resolution=(2400, 1080)))
        if pos:
            logger.warning("mvp分享界面")
            existsTHENtouch(Template(r"tpl1685521173525.png", threshold=0.9, record_pos=(-0.453, -0.2), resolution=(2400, 1080)))
            jixu=True
            sleep(2)
        #
        #都尝试一次返回
        if existsTHENtouch(Template(r"tpl1685521173525.png", threshold=0.9, record_pos=(-0.453, -0.2), resolution=(2400, 1080))):
            sleep(2)
        
        # 继续
        #logger.warning("等待对战结束")
        #没遇到过这个情况
        #if exists(Template(r"确定6.png", record_pos=(0.102, 0.117), resolution=(2400, 1080))):
        #    logger.warning("确定")
        #    touch(Template(r"确定6.png", record_pos=(0.102, 0.117), resolution=(2400, 1080)))
        if existsTHENtouch(Template(r"tpl1685498461310.png", record_pos=(-0.075, 0.175), resolution=(2400, 1080))):
            logger.warning("MVP继续")
            jixu=True
            sleep(2)
        if existsTHENtouch(Template(r"tpl1685432883720.png", record_pos=(-0.077, 0.175), resolution=(2400, 1080))):                        
            logger.warning("继续1/3")
            jixu=True
            sleep(2)
        if existsTHENtouch(Template(r"tpl1685433017267.png", record_pos=(0.004, 0.182), resolution=(2400, 1080))):
            logger.warning("继续2/3")
            jixu=True
            sleep(2)
        if existsTHENtouch(Template(r"tpl1685433115639.png", record_pos=(0.002, 0.183), resolution=(2400, 1080))):
            logger.warning("继续3/3")
            jixu=True
            sleep(2)
        #
        #
        if not jixu:
            logger.warning("未监测到继续,sleep...")
            sleep(20)
            continue
        #
        # 返回大厅
        # 因为不能保证返回辅助账户返回房间，所以返回大厅更稳妥
        if exists(Template(r"tpl1686108933966.png", record_pos=(0.002, 0.18), resolution=(2400, 1080))):
            if 返回房间:
                if existsTHENtouch(Template(r"tpl1686108966830.png", record_pos=(0.065, 0.18), resolution=(2400, 1080)),"返回房间",savepos=True):
                    sleep(2)
                    if 房间中(): break
        if existsTHENtouch(Template(r"tpl1685433152517.png", threshold=0.9, record_pos=(-0.063, 0.182), resolution=(2400, 1080)),"返回大厅"):
            sleep(5)
            if existsTHENtouch(Template(r"tpl1685433175620.png", threshold=0.9, record_pos=(0.078, 0.093), resolution=(2400, 1080)),"确定返回大厅",savepos=True):
                sleep(5)
            #
            if 大厅中():
                break
            else:
                异常处理_返回大厅()
                break
        logger.warning("等待对战结束")
        sleep(5)
        #
        #万一各种原因导致已经返回了
        if 大厅中():
            break
    


def handler2(signum, frame):
    logger.warning("关闭王者荣耀 {}".format(设备信息["链接"]))
    # 这个命令会强制停止 
    # stop_app(设备信息["王者应用ID"])


def handler(signum, frame):
    if not 辅助:
        os.kill(os.getpid(), signal.SIGUSR1)
    else:
        for p in process_list:
            os.kill(p.pid, signal.SIGUSR1)
        sleep(3)
        for p in process_list:
            p.terminate()
    logger.warning("程序退出")
    os.kill(os.getpid(), signal.SIGTERM)


def 王者子进程(type, 设备类型, 设备IP地址):
    print(设备类型)
    print(设备IP地址)
    global 英雄属性
    global 设备信息
    global device
    global 次数
    global 次数2
    #signal.signal(signal.SIGUSR1, handler2)
    if type:
        英雄属性 = {
            "type": type,
            "想玩位置": 想玩位置,
            "参战英雄": 参战英雄,
            "参战英雄线路": 参战英雄线路,
            "备战英雄": 备战英雄,
            "备战英雄线路": 备战英雄线路,
        }
    else:
        英雄属性 = {
            "type": type,
            "想玩位置": 辅助想玩位置,
            "参战英雄": 辅助参战英雄,
            "参战英雄线路": 辅助参战英雄线路,
            "备战英雄": 辅助备战英雄,
            "备战英雄线路": 辅助备战英雄线路,
        }
    设备信息 = {
        "链接": format("{}:///{}:{}".format(设备类型, 设备IP地址, port)),
        "王者应用ID": "com.tencent.tmgp.sgame"
    }
    if 设备类型 == "iOS":
        设备信息 = {
            "链接": format("{}:///{}:{}".format(设备类型, 设备IP地址, 8100)),
            "王者应用ID": "com.tencent.smoba"
        }
    次数2 = 次数
    atexit.register(重启游戏) #----------
    #exit()
    #device = connect_device("Android:///192.168.12.211:43069")
    重启游戏()


def 重启游戏():
    logger.warning("重启游戏")
    global 次数
    global 次数2
    global device
    #
    device = False
    #
    if 次数 <= 0:
        return
    for k in range(次数):
        次数2 -= 1
        logger.warning("第 {} 次运行子程序".format(次数 - 次数2))
        if not device:
            #-------------------
            device = connect_device(设备信息["链接"])
            #-------------------
            logger.warning("设备信息: {}".format(设备信息))
            启动王者荣耀()
        匹配游戏()
        sleep(3*60)
        sleep_time=60
        sleeploop=0
        while 对战中(): 
            sleep_time=max(10,sleep_time/2*1.7)
            sleep(sleep_time)
            sleeploop =sleeploop +1
            if sleeploop > 10: break #虚拟机王者程序卡住了
        #device.disconnect()
        #device = connect_device(设备信息["链接"])
        游戏结束()
        save_dict()
        logger.warning("游戏已结束. sleep一段时间进入下层循环")
        sleep(1.3)


if len(sys.argv) > 1:
    if sys.argv[1] == "-f":
        辅助 = True
        logger.warning("辅助英雄 启用")

if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)
    global process_list
    process_list = []
    if not 辅助:
        王者子进程(True, 设备类型, 设备IP地址)
        # 王者子进程(False, 辅助设备类型, 辅助设备IP地址)
    else:
        p1 = Process(target=王者子进程, args=(True, 设备类型, 设备IP地址))
        p2 = Process(target=王者子进程, args=(False, 辅助设备类型, 辅助设备IP地址))
        process_list.append(p1)
        process_list.append(p2)
        p1.start()
        p2.start()
        logger.warning('主英雄pid: {}'.format(p1.pid))
        logger.warning('辅助英雄pid: {}'.format(p2.pid))



#touch(Template(r"tpl1685687139718.png", record_pos=(-0.006, 0.091), resolution=(2400, 1080)))
#touch(Template(r"tpl1685972839109.png", record_pos=(0.003, 0.129), resolution=(2480, 1116)))
































#touch(Template(r"tpl1689044185527.png", record_pos=(-0.173, -0.053), resolution=(2400, 1080)))


#touch(Template(r"tpl1689218509411.png", record_pos=(0.107, 0.011), resolution=(2400, 1080)))
