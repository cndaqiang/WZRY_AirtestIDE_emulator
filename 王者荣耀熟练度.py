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


次数 = 20  # 对战次数设置 一次大概27点经验

想玩位置 = Template(r"tpl1685434789273.png", record_pos=(-0.339, -0.041), resolution=(2400, 1080))


 # `对战` -> `5v5 王者峡谷` -> `人机` -> `开始练习` 组队页面修改想玩的位置


参战英雄 = Template(r"tpl1685434702783.png", record_pos=(-0.412, 0.107), resolution=(2400, 1080))
 # `对战` -> `5v5 王者峡谷` -> `人机` -> `开始练习` -> `开始匹配` -> `英雄页面选择你想用的英雄`


参战英雄线路 =Template(r"tpl1685434683721.png", record_pos=(-0.275, -0.207), resolution=(2400, 1080)) # `对战` -> `5v5 王者峡谷` -> `人机` -> `开始练习` -> `开始匹配` -> `英雄页面选择你想用的英雄的线路`


备战英雄 =Template(r"tpl1685434749789.png", record_pos=(-0.112, -0.065), resolution=(2400, 1080))

 # `对战` -> `5v5 王者峡谷` -> `人机` -> `开始练习` -> `开始匹配` -> `英雄页面选择你想用的备选英雄`

备战英雄线路 = Template(r"tpl1685434760253.png", record_pos=(0.07, -0.209), resolution=(2400, 1080))
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


def 异常处理():
    logger.warning("进入异常处理")

    if 大厅中():
        return
    if 对战中():
        游戏结束()
    # 健康系统
    健康系统()
    # 广告直播
    for i in range(5):
        if exists(Template(r"关闭广告.png", record_pos=(0.429, -0.205), resolution=(2400, 1080))):
            logger.warning("第 {} 次关闭广告".format(i + 1))
            touch(Template(r"关闭广告.png", record_pos=(0.431, -0.203), resolution=(2400, 1080)))
        else:
            break
    # 点击屏幕继续
    if exists(Template(r"点击屏幕继续.png", record_pos=(0.002, 0.287), resolution=(2400, 1080))):
        logger.warning("点击屏幕继续")
        touch(Template(r"点击屏幕继续.png", record_pos=(0.002, 0.287), resolution=(2400, 1080)))


def 邀请辅助():
    if 辅助:
        for i in range(10):
            logger.warning("第 %s 次 等待邀请通过" % (i + 1))

            if exists(Template(r"邀请成功.png", record_pos=(-0.245, -0.072), resolution=(2400, 1080))):
                logger.warning("邀请成功")
                sleep(5)
                return
            if exists(Template(r"邀请按钮.png", threshold=0.9, record_pos=(0.463, -0.195), resolution=(2400, 1080))):
                logger.warning("邀请米莱狄")
                touch(Template(r"邀请按钮.png", record_pos=(0.463, -0.195), resolution=(2400, 1080)))
                continue

            if exists(Template(r"微信邀请按钮.png", threshold=0.9, record_pos=(0.462, -0.195), resolution=(2400, 1080))):
                logger.warning("对方未上线")

            if exists(Template(r"对方组队中.png", record_pos=(0.462, -0.195), resolution=(2400, 1080))):
                touch(Template(r"对方组队中.png", record_pos=(0.462, -0.195), resolution=(2400, 1080)))
                if wait(Template(r"邀请组队中的队友.png", record_pos=(0.348, -0.206), resolution=(2400, 1080))):
                    logger.warning("邀请组队中的队友")
                    touch(Template(r"组队中的队友邀请按钮.png", record_pos=(0.364, -0.221), resolution=(2400, 1080)))
                    sleep(5)
                    continue

            if exists(Template(r"已被健康系统禁止.png", record_pos=(-0.014, -0.025), resolution=(2400, 1080))):
                logger.warning("对方已禁赛")
                touch(Template(r"确定3.png", record_pos=(0.097, 0.117), resolution=(2400, 1080)))
                return
            if exists(Template(r"是否在微信邀请.png", record_pos=(-0.077, -0.015), resolution=(2400, 1080))):
                logger.warning("对方未上线")
                # touch(Template(r"取消按钮.png", record_pos=(-0.098, 0.117), resolution=(2400, 1080)))
            sleep(5)


def 启动游戏():
    # 开始人机对局
    #Template图像识别代码
    #threshold：识别阈值，浮点类型，范围是[0.0, 1.0]，默认0.7
    #record_pos: pos in screen when recording
    #resolution: screen resolution when recording
    #小米11 1440x3200 
    #获得分辨率 adb shell dumpsys window display
    #record_pos和resolution只是为了加速，都可以识别的

    if 英雄属性["type"]:
        #wait等待元素出现，没出现就执行intervalfunc
        btn_pos = wait(Template(r"tpl1685425252726.png", record_pos=(-0.08, 0.106), resolution=(2400, 1080)), intervalfunc=异常处理)
        touch(Template(r"tpl1685425252726.png", record_pos=(-0.08, 0.106), resolution=(2400, 1080)))

        try:
            if btn_pos:
                touch(btn_pos)
                logger.warning("选择对战")
        except:
            logger.error("选择对战失败")

        # 5v5
        
        btn_pos = wait(Template(r"tpl1685431293206.png", record_pos=(-0.315, 0.078), resolution=(2400, 1080))
, intervalfunc=异常处理)
        try:
            if btn_pos:
                touch(btn_pos)
                logger.warning("选择 5v5王者峡谷")
        except:
            logger.error("选择 5v5王者峡谷 失败")

        # 人机
        btn_pos = wait(Template(r"tpl1685431315731.png", record_pos=(0.049, 0.071), resolution=(2400, 1080))
, intervalfunc=异常处理)
        try:
            if btn_pos:
                touch(btn_pos)
                logger.warning("选择 人机")
        except:
            logger.error("选择 人机 失败")

        # 快速模式
        btn_pos = wait(Template(r"tpl1685431620909.png", record_pos=(-0.246, -0.017), resolution=(2400, 1080))

, intervalfunc=异常处理)
        try:
            if btn_pos:
                touch(btn_pos)
                logger.warning("选择 快速模式")
        except:
            logger.error("选择 快速模式 失败")

        # 选择难度
        if exists(Template(r"tpl1685431397853.png", record_pos=(0.009, -0.117), resolution=(2400, 1080))

):
            logger.warning("选择 倔强青铜难度")
            touch(Template(r"tpl1685431397853.png", record_pos=(0.009, -0.117), resolution=(2400, 1080)))

        # 开始练习
        btn_pos = Template(r"tpl1685431440002.png", record_pos=(0.253, 0.128), resolution=(2400, 1080))

        if exists(btn_pos):
            logger.warning("开始练习")
            touch(btn_pos)
        sleep(2)
        if exists(btn_pos) and False:
            logger.warning("次数用完")
            os.kill(os.getpid(), signal.SIGINT)  # 退出程序
            if exists(Template(r"倔强青铜难度.png", record_pos=(-0.03, -0.149), resolution=(2400, 1080))):
                logger.warning("选择 青铜难度")
                touch(Template(r"倔强青铜难度.png", record_pos=(-0.03, -0.149), resolution=(2400, 1080)))
                touch(btn_pos)

        if False: #没必要
            # 选择路线
            btn_pos = wait(Template(r"tpl1685431774988.png", record_pos=(-0.312, -0.073), resolution=(2400, 1080))
, intervalfunc=异常处理)
            try:
                if btn_pos:
                    touch(Template(r"tpl1685431774988.png", record_pos=(-0.312, -0.073), resolution=(2400, 1080)))
                if exists(英雄属性["想玩位置"]):
                    logger.warning("选择 想玩的位置")
                    touch(英雄属性["想玩位置"])
            except:
                logger.error("选择 想玩的位置 失败")

        #>  邀请辅助()
        # 开始匹配
        while True:
            if exists(Template(r"tpl1685431840269.png", record_pos=(0.127, 0.187), resolution=(2400, 1080))):
                logger.warning("开始匹配")
                touch(Template(r"tpl1685431840269.png", record_pos=(0.127, 0.187), resolution=(2400, 1080)))
                break
            sleep(1)
        while True:
            # 确认匹配
            if exists(Template(r"tpl1685431876071.png", record_pos=(-0.004, 0.122), resolution=(2400, 1080))):
                logger.warning("确认匹配")
                touch(Template(r"tpl1685431876071.png", record_pos=(-0.004, 0.122), resolution=(2400, 1080)))
                break
            sleep(1)
        if False: #原来的代码
            while True:
                if exists(Template(r"选英雄页面.png", record_pos=(-0.41, -0.305), resolution=(2400, 1080))):
                    logger.warning("已确认匹配")
                    break
            # 显示所有英雄
            if exists(Template(r"显示全部英雄.png", record_pos=(-0.291, -0.021), resolution=(2400, 1080))):
                logger.warning("选择 显示所有英雄")
                touch(Template(r"显示全部英雄.png", record_pos=(-0.291, -0.021), resolution=(2400, 1080)))
            else:
                logger.error("未找到 显示所有英雄")
    
            # 选择分路
            #wait()和exists()有什么区别？
            #都是传入一张图片(template实例)，然后判断图片是否存在；
            #如果图片存在，两者均会返回图片坐标。
            #wait()找不到图片会报错TargetNotFoundError，而exists()找不到则返回False。
            if exists(英雄属性["参战英雄线路"]):
                logger.warning("选择 英雄线路 {}".format(英雄属性["参战英雄线路"].filename.split(".")[0]))
                touch(英雄属性["参战英雄线路"])
            else:
                logger.error("未找到 英雄线路")
    
            # 选择英雄
            if exists(英雄属性["参战英雄"]):
                logger.warning("选择 英雄 {}".format(英雄属性["参战英雄"].filename.split(".")[0]))
                touch(英雄属性["参战英雄"])
                if exists(Template(r"分路重复.png", record_pos=(-0.001, -0.157), resolution=(2400, 1080))):
                    logger.warning("分路冲突，切换英雄")
                    touch(Template(r"分路重复取消按钮.png", record_pos=(-0.095, 0.19), resolution=(2400, 1080)))
                    if exists(Template(r"显示全部英雄.png", record_pos=(-0.291, -0.021), resolution=(2400, 1080))):
                        logger.warning("选择 英雄类型")
                        touch(Template(r"显示全部英雄.png", record_pos=(-0.291, -0.021), resolution=(2400, 1080)))
                    if exists(英雄属性["备战英雄线路"]):
                        logger.warning("选择 备战英雄线路 {}".format(英雄属性["备战英雄线路"].filename.split(".")[0]))
                        touch(英雄属性["备战英雄线路"])
    
                    if exists(英雄属性["备战英雄"]):
                        logger.warning("选择 备战英雄 {}".format(英雄属性["备战英雄"].filename.split(".")[0]))
                        touch(英雄属性["备战英雄"])
            else:
                logger.error("未找到 英雄")
        else: #采用的代码
            while True:
                #选择英雄按钮
                if exists(Template(r"tpl1685425713708.png", record_pos=(-0.371, -0.206), resolution=(2400, 1080))):
                #    #显示全部英雄.png
                    touch(Template(r"tpl1685425741770.png", record_pos=(-0.285, -0.012), resolution=(2400, 1080)))
                    logger.warning("展开英雄界面")
                    break
            touch(英雄属性["参战英雄线路"])
            logger.warning("参战英雄线路")
            touch(英雄属性["参战英雄"])
            logger.warning("参战英雄")
            #分路重复.png
            if exists(Template(r"tpl1685426207941.png", record_pos=(0.005, -0.126), resolution=(2400, 1080))):
                logger.warning("分路冲突，切换英雄")
                #分路重复取消按钮.png
                touch(Template(r"tpl1685426213846.png", record_pos=(-0.073, 0.152), resolution=(2400, 1080)))
                #选择英雄
                if exists(Template(r"tpl1685425741770.png", record_pos=(-0.285, -0.012), resolution=(2400, 1080))):
                    logger.warning("选择 英雄类型")
                    touch(Template(r"tpl1685425741770.png", record_pos=(-0.285, -0.012), resolution=(2400, 1080)))
                if exists(英雄属性["备战英雄线路"]):
                    logger.warning("选择 备战英雄线路 {}".format(英雄属性["备战英雄线路"].filename.split(".")[0]))
                    touch(英雄属性["备战英雄线路"])
    
                    if exists(英雄属性["备战英雄"]):
                        logger.warning("选择 备战英雄 {}".format(英雄属性["备战英雄"].filename.split(".")[0]))
                        touch(英雄属性["备战英雄"])
            #   确定
            if exists(Template(r"tpl1685425856227.png", record_pos=(0.389, 0.192), resolution=(2400, 1080))):
                touch(Template(r"tpl1685425856227.png", record_pos=(0.389, 0.192), resolution=(2400, 1080)))
                sleep(1)
            #万一是房主
            if exists(Template(r"tpl1685425856227.png", record_pos=(0.389, 0.192), resolution=(2400, 1080))):
                touch(Template(r"tpl1685425856227.png", record_pos=(0.389, 0.192), resolution=(2400, 1080)))
                sleep(1)
        sleep(1)
        #加油拳头
        if exists(Template(r"tpl1685432367512.png", record_pos=(0.34, 0.0), resolution=(2400, 1080))):
            touch(Template(r"tpl1685432367512.png", record_pos=(0.34, 0.0), resolution=(2400, 1080)))

        sleep(300) #游戏时间很长的
        游戏结束()
    else:
        # 等待邀请
        异常处理()
        logger.warning("等待邀请")
        global nums
        nums = 0

        while True:
            nums += 1
            logger.warning("第 %s 次 等待邀请" % nums)
            if exists(Template(r"实战模拟邀请.png", record_pos=(-0.083, 0.018), resolution=(2400, 1080))):
                logger.warning("接受邀请")
                touch(Template(r"实战模拟邀请确认.png", record_pos=(0.158, 0.09), resolution=(2400, 1080)))
                break
            健康系统()
            if nums > 100:
                logger.warning("没人邀请, 退出")
                stop_app(设备信息["王者应用ID"])
                process_list[1].terminate()

        # 选择路线
        if exists(Template(r"辅助英雄切换线路按钮.png", record_pos=(-0.255, -0.092), resolution=(2400, 1080))):
            touch(Template(r"辅助英雄切换线路按钮.png", record_pos=(-0.255, -0.092), resolution=(2400, 1080)))
            if exists(英雄属性["想玩位置"]):
                logger.warning("选择 想玩的位置")
                touch(英雄属性["想玩位置"])

        while True:
            # 确认匹配
            if exists(Template(r"确认5.png", record_pos=(-0.004, 0.148), resolution=(2400, 1080))):
                logger.warning("确认匹配")
                touch(Template(r"确认5.png", record_pos=(-0.004, 0.148), resolution=(2400, 1080)))
                break

        while True:
            if exists(Template(r"选英雄页面.png", record_pos=(-0.41, -0.305), resolution=(2400, 1080))):
                logger.warning("已确认匹配")
                break

        # 显示所有英雄
        if exists(Template(r"显示全部英雄.png", record_pos=(-0.291, -0.021), resolution=(2400, 1080))):
            logger.warning("选择 显示所有英雄")
            touch(Template(r"显示全部英雄.png", record_pos=(-0.291, -0.021), resolution=(2400, 1080)))
        else:
            logger.error("未找到 显示所有英雄")

        # 选择英雄线路
        if exists(英雄属性["参战英雄线路"]):
            logger.warning("选择 英雄线路 {}".format(英雄属性["参战英雄线路"].filename.split(".")[0]))
            touch(英雄属性["参战英雄线路"])
        else:
            logger.error("未找到 英雄线路")

        # 选择英雄
        if exists(英雄属性["参战英雄"]):
            logger.warning("选择 英雄 {}".format(英雄属性["参战英雄"].filename.split(".")[0]))
            touch(英雄属性["参战英雄"])
            if exists(Template(r"分路重复.png", record_pos=(-0.001, -0.157), resolution=(2400, 1080))):
                logger.warning("分路冲突，切换英雄")
                touch(Template(r"分路重复取消按钮.png", record_pos=(-0.095, 0.19), resolution=(2400, 1080)))
                if exists(Template(r"显示全部英雄.png", record_pos=(-0.291, -0.021), resolution=(2400, 1080))):
                    logger.warning("选择 英雄类型")
                    touch(Template(r"显示全部英雄.png", record_pos=(-0.291, -0.021), resolution=(2400, 1080)))
                if exists(英雄属性["备战英雄线路"]):
                    logger.warning("选择 备战英雄线路 {}".format(英雄属性["备战英雄线路"].filename.split(".")[0]))
                    touch(英雄属性["备战英雄线路"])

                if exists(英雄属性["备战英雄"]):
                    logger.warning("选择 备战英雄 {}".format(英雄属性["备战英雄"].filename.split(".")[0]))
                    touch(英雄属性["备战英雄"])
        else:
            logger.error("未找到 英雄")

        sleep(15)
        游戏结束()


def 启动王者荣耀():
    logger.warning("连接设备")
    if device:
        logger.warning("设备连接成功")
    else:
        logger.warning("设备连接失败")
        return
    logger.warning("启动 王者荣耀")
    异常处理()
    if 大厅中() or 对战中():
        return
    for i in range(10):
        if exists(Template(r"返回.png", record_pos=(-0.444, -0.299), resolution=(2400, 1080))):
            logger.warning("返回")
            touch(Template(r"返回.png", record_pos=(-0.444, -0.299), resolution=(2400, 1080)))
        else:
            break
    start_app(设备信息["王者应用ID"])
    if exists(Template(r"软件更新.png", threshold=0.8, record_pos=(-0.365, 0.293), resolution=(2400, 1080))):
        logger.warning("软件更新")
        sleep(600)
        if exists(Template(r"更新完成.png", record_pos=(-0.162, -0.017), resolution=(2400, 1080))):
            touch(Template(r"更新完成确认.png", record_pos=(-0.003, 0.115), resolution=(2400, 1080)))
            start_app(设备信息["王者应用ID"])

    if exists(Template(r"更新公告.png", record_pos=(0.087, -0.202), resolution=(2400, 1080))):
        logger.warning("关闭更新公告")
        touch(Template(r"关闭更新公告.png", record_pos=(0.353, -0.205), resolution=(2400, 1080)))

    sleep(20)

    btn_pos = wait(Template(r"静音按钮.png", record_pos=(0.456, -0.101), resolution=(2400, 1080)), intervalfunc=异常处理)
    try:
        if btn_pos:
            touch(btn_pos)
            logger.warning("静音")
    except:
        logger.warning("静音失败")
    btn_pos = wait(Template(r"开始游戏按钮.png", threshold=0.9, record_pos=(-0.003, 0.16), resolution=(2400, 1080)), interval=4, intervalfunc=异常处理)
    try:
        if btn_pos:
            touch(btn_pos, times=2)
            logger.warning("登录")
    except:
        logger.warning("登录失败")


def 大厅中():
    if exists(Template(r"对战.png", threshold=0.9, record_pos=(-0.1, 0.188), resolution=(2400, 1080))):
        logger.warning("正在大厅中")
        return True


def 对战中():
    if exists(Template(r"对战中.png", record_pos=(0.422, 0.245), resolution=(2400, 1080))):
        logger.warning("正在对战中")
        return True


def 健康系统():
    if exists(Template(r"健康系统.png", record_pos=(0.119, -0.099), resolution=(2400, 1080))):
        logger.warning("您已禁赛")
        touch(Template(r"确定1.png", record_pos=(0.201, 0.079), resolution=(2400, 1080)))
        stop_app(设备信息["王者应用ID"])
        # start_app(设备信息["王者应用ID"])
        sleep(900)
        启动王者荣耀()
        raise Exception("您已禁赛")

    if exists(Template(r"健康系统1.png", record_pos=(-0.158, -0.028), resolution=(2400, 1080))):
        touch(Template(r"确定2.png", record_pos=(0.098, 0.119), resolution=(2400, 1080)))
        stop_app(设备信息["王者应用ID"])
        # start_app(设备信息["王者应用ID"])
        sleep(900)
        启动王者荣耀()
        raise Exception("您已禁赛")


def 游戏结束():
    while True:
        # 继续
        logger.warning("等待对战结束")
        if exists(Template(r"确定6.png", record_pos=(0.102, 0.117), resolution=(2400, 1080))):
            logger.warning("确定")
            touch(Template(r"确定6.png", record_pos=(0.102, 0.117), resolution=(2400, 1080)))
        for loop in range(5):
            if exists(Template(r"tpl1685432883720.png", record_pos=(-0.077, 0.175), resolution=(2400, 1080))):
                logger.warning("继续")
                touch(Template(r"tpl1685432883720.png", record_pos=(-0.077, 0.175), resolution=(2400, 1080)))

                sleep(2)
            else:
                break
        for loop in range(5):
            if exists(Template(r"tpl1685433017267.png", record_pos=(0.004, 0.182), resolution=(2400, 1080))):
                touch(Template(r"tpl1685433017267.png", record_pos=(0.004, 0.182), resolution=(2400, 1080)))
                sleep(2)
            else:
                break
        for loop in range(5):
            if exists(Template(r"tpl1685433115639.png", record_pos=(0.002, 0.183), resolution=(2400, 1080))):
                touch(Template(r"tpl1685433115639.png", record_pos=(0.002, 0.183), resolution=(2400, 1080)))

                sleep(2)
            else:
                break            
        # 返回大厅
        # 因为不能保证返回辅助账户返回房间，所以返回大厅更稳妥
        if exists(Template(r"tpl1685433152517.png", record_pos=(-0.063, 0.182), resolution=(2400, 1080))):
            logger.warning("返回大厅")
            touch(Template(r"tpl1685433152517.png", record_pos=(-0.063, 0.182), resolution=(2400, 1080)))

            if exists(Template(r"tpl1685433175620.png", record_pos=(0.078, 0.093), resolution=(2400, 1080))):
                logger.warning("确定")
                touch(Template(r"tpl1685433175620.png", record_pos=(0.078, 0.093), resolution=(2400, 1080)))

            break
        sleep(15)


def handler2(signum, frame):
    logger.warning("关闭王者荣耀 {}".format(设备信息["链接"]))
    stop_app(设备信息["王者应用ID"])


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
    signal.signal(signal.SIGUSR1, handler2)
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
        "链接": format("{}:///{}:{}".format(设备类型, 设备IP地址, 5555)),
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

    if 次数 <= 0:
        return
    for k in range(次数):
        次数2 -= 1
        logger.warning("第 {} 次运行子程序".format(次数 - 次数2))
        #-------------------
        print("device info in restartgame")
        print(设备信息["链接"])
        device = connect_device(设备信息["链接"])
        #-------------------
        logger.warning("设备信息: {}".format(设备信息))
        启动王者荣耀()
        启动游戏()
        logger.warning("游戏结束进入下层循环--------%i"%(k))


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







