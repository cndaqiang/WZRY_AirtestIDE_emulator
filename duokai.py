# -*- encoding=utf8 -*-
#可以这样命令行中运行
'''
现在多线程，有概率无法启动主进程
夜间就不要运行了，白天容易被禁赛
(base) cndaqiang@macmini mac$ 
/Applications/AirtestIDE.app/Contents/Resources/plugins/firebase_plugin/tool/copy_app/airtest/core/android/static/adb/mac/adb devices
List of devices attached
adb server version (40) doesn't match this client (39); killing...
* daemon started successfully *
8553e6ac	device

(base) cndaqiang@macmini mac$ 
/Applications/AirtestIDE.app/Contents/Resources/plugins/firebase_plugin/tool/copy_app/airtest/core/android/static/adb/mac/adb tcpip 5555
restarting in TCP mode port: 5555
#mac
"/Applications/AirtestIDE.app/Contents/MacOS/AirtestIDE" pyrunner "/Users/cndaqiang/Desktop/WZRY_AirtestIDE-main/XiaoMI11.py" 
#windows， cmd可以，powershell不行
#运行时一个斜杠,脚本里写一个斜杠会报错
C:\\Users\cndaqiang\Videos\AirtestIDE\airtest\core\android\static\adb\windows\adb.exe devices
"C:\\Users\cndaqiang\Videos\AirtestIDE\AirtestIDE" pyrunner "C:\\Users\cndaqiang\Desktop\WZRY_AirtestIDE-main 2\WZRY_AirtestIDE-main\XiaoMI11.py" 
也可以python 1.py 但是要提前pip安装python -m pip install airtest, pathos
#bluestack问题
无法启动bluestacks 请发送问题报告，是c盘压缩的原因
2G/虚拟机
cmd执行python程序有时会卡住,需要回车,cmd默认值>属性关闭快速编辑模式
#note
多开刷机目的
1. 友情重燃币
2. 师徒任务，增加名师点，并增加师父的金币

'''

__author__ = "xr"

# --------------------- 自定义信息 --------------------->
次数 = 100 #5  # 对战次数设置 一次大概27点经验 #1次十分钟，5h~30次
加速对战= False #加速对战时，虽然会输，但是满足活动对于对战的判断
选择英雄= True #False #不选择英雄时，是手动点取，适合刷特定英雄的任务
#设备信息
设备类型_dict={}
设备IP地址_dict={}
设备类型_dict[0]="Android"
设备类型_dict[1]="Android"
设备类型_dict[2]="Android"
设备IP地址_dict[0]="127.0.0.1:"+str( 5555 ) #fashi
设备IP地址_dict[1]="127.0.0.1:"+str( 5565 )#duikang
设备IP地址_dict[2]="127.0.0.1:"+str( 5575 )#fayu


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
import time
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
if False:
    try:
        from pathos.multiprocessing import ProcessingPool
    except ImportError:
        print("模块不存在, 尝试安装")
        import pip
        try:
            pip.main(['install', 'pathos', '-i', 'https://pypi.tuna.tsinghua.edu.cn/simple'])
        except:
            print("安装pathos失败")
            exit(1)

ST.OPDELAY = 1
# 全局阈值的范围为[0, 1]
ST.THRESHOLD_STRICT = 0.8  # assert_exists语句touch(Template(r"tpl1689665366952.png", record_pos=(-0.425, -0.055), resolution=(960, 540)))的默认阈值，一般比THRESHOLD更高一些

ST.THRESHOLD = 0.8  # 其他语句的默认阈值
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
辅助=True
#一些变量可以保存,重复运行不用读入
position_dict={}
position_dict_file="position_dict.txt"

#读取变量
def read_dict(position_dict_file="position_dict.txt"):
    global 辅助
    #if 辅助: return {}
    import pickle
    position_dict={}
    if os.path.exists(position_dict_file):
        logger.warning("读取"+position_dict_file)
        with open(position_dict_file, 'rb') as f:
            position_dict = pickle.load(f)
    return position_dict
    #保存变量
def save_dict(position_dict,position_dict_file="position_dict.txt"):
    global 辅助
    #if 辅助: return True
    import pickle
    f = open(position_dict_file, "wb") 
    pickle.dump(position_dict, f)
    f.close



'''
小技巧:
    在人机试炼选英雄界面，显示全部英雄，选择你想用的英雄线路页面，别点击英雄, 截图, 王者放后台，打开相册
'''




mynode=-10
totalnode=-10
multi_run=False #使用multip运行时，关闭其他node的输出
#不要设置这个
想玩位置 = Template(r"tpl1689665383641.png", record_pos=(-0.427, -0.057), resolution=(960, 540))
辅助想玩位置 = Template(r"tpl1689667736118.png", record_pos=(-0.426, 0.034), resolution=(960, 540))

参战英雄线路_dict={}
参战英雄头像_dict={}
参战英雄线路_dict[0]=Template(r"tpl1689665455905.png", record_pos=(-0.066, -0.256), resolution=(960, 540))
参战英雄头像_dict[0]=Template(r"tpl1691818492021.png", record_pos=(-0.278, 0.029), resolution=(960, 540))

参战英雄线路_dict[1]=Template(r"tpl1689665490071.png", record_pos=(-0.315, -0.257), resolution=(960, 540))
参战英雄头像_dict[1]=Template(r"tpl1691818474653.png", record_pos=(-0.359, 0.129), resolution=(960, 540))


参战英雄线路_dict[2]=Template(r"tpl1689665540773.png", record_pos=(0.06, -0.259), resolution=(960, 540))
参战英雄头像_dict[2]=Template(r"tpl1691029073589.png", record_pos=(0.11, -0.083), resolution=(960, 540))

参战英雄线路_dict[3]=Template(r"tpl1689665577871.png", record_pos=(0.183, -0.26), resolution=(960, 540))
参战英雄头像_dict[3]=Template(r"tpl1690442560069.png", record_pos=(0.11, 0.025), resolution=(960, 540))
参战英雄线路_dict[4]=Template(r"tpl1689665540773.png", record_pos=(0.06, -0.259), resolution=(960, 540))
参战英雄头像_dict[4]=Template(r"tpl1690442530784.png", record_pos=(0.108, -0.086), resolution=(960, 540))
参战英雄线路_dict[5]=Template(r"tpl1689665577871.png", record_pos=(0.183, -0.26), resolution=(960, 540))
参战英雄头像_dict[5]=Template(r"tpl1690442560069.png", record_pos=(0.11, 0.025), resolution=(960, 540))


主TAG='.mom.'
辅助TAG='.boy.'
def getmytag(type=True,node=-1):
    endstr=""
    global totalnode
    if node >= 0:
        endstr=str(node%totalnode)+"."
    if type:
        return 主TAG+endstr
    else:
        return 辅助TAG+endstr

def removefile(filename):
    try:
        os.remove(filename)
        logger.warning("删除["+filename+"]成功") 
        return True    
    except:
        logger.warning("删除["+filename+"]失败")     
        return False
def touchfile(filename):
    try:
        f=open(filename,'w')
        logger.warning("touch["+filename+"]成功")     
    except:
        logger.warning("touch["+filename+"]失败")   
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
def 异常终止(errinfo="程序异常终止"):
    logger.warning(errinfo)
    global 设备信息
    stop_app(设备信息["王者应用ID"])
    os.kill(os.getpid(), signal.SIGTERM)
timedict={}
def timelimit(timekey="",limit=0,init=True):
    global timedict
    if len(timekey) == 0: timekey="none"
    if not timekey in timedict.keys(): init = True
    if init:
        timedict[timekey]=time.time()
    else:
        if time.time()-timedict[timekey] > limit:
            timedict[timekey]=time.time()
            return True
        else:
            return False

def autonode(totalnode):
    if totalnode < 2: return 0
    node=-10
    PID=os.getpid()
    filename="init_node."+str(totalnode)+"."+str(PID)+".txt"
    touchfile(filename)
    logger.warning("自动生成node中:"+filename)
    PID_dict={}
    for i in np.arange(60):
        for name in os.listdir("."):
            if "init_node."+str(totalnode)+"." in name:
                PID_dict[name]=name
        if len(PID_dict) == totalnode: break
        sleep(5)
    if len(PID_dict) != totalnode:
        removefile(filename)
        logger.warning("文件数目不匹配")
        return node
    #
    strname=np.array(list(PID_dict.keys()))
    PIDarr=np.zeros(strname.size)
    for i in np.arange(PIDarr.size):
        PIDarr[i]=int(strname[i].split(".")[2])
    PIDarr=np.sort(PIDarr)
    for i in np.arange(PIDarr.size):
        logger.warning("i="+str(i)+". PID="+str(PID)+". PIDarr[i]="+str(PIDarr[i]))
        if PID == PIDarr[i]: node=i
    
    if node < 0:
        logger.warning("node < 0")
        removefile(filename)
        return node
    #
    logger.warning("mynode:"+str(node))
    if barriernode(node == 0, "autonode",node):
        removefile(filename)
        return node




def barriernode(type=True,name="barrierFile",mynode_=-10):
    #互相检查状态
    #主节点建立一堆文件,其余节点负责删除, 文件都删除了,则同步完成
    #
    global totalnode
    global mynode
    if totalnode < 2: return True
    global multi_run
    global barrier
    if multi_run:
        pass
    logger.warning(".....................")
    logger.warning("同步中"+name)
    logger.warning(".....................")
    #removefile(name+getmytag(type))

    if mynode_ < 0: mynode_ = mynode
    if type: #ionode
        for i in np.arange(1,totalnode):
            touchfile(name+getmytag(True,i))
    #
    timelimit(timekey="barrier"+name,limit=60*20,init=True)
    barrieryes=0
    for loop in range(60*2): #20min
        if timelimit(timekey="barrier"+name,limit=60*20,init=False): 异常终止("结束游戏时间过长")
        if type: #如果是主节点，先等待其他节点删除主节点文件
           barrieryes=True
           for i in np.arange(1,totalnode):
               barrieryes = barrieryes and not os.path.exists(name+getmytag(True,i))
           if barrieryes:
               logger.warning("+++++MASTER:同步完成"+name)
               return True
        else:
              if removefile(name+getmytag(True,mynode_)):
                 #logger.warning("+++++node:同步完成,等待数秒")
                 #sleep(mynode_ * 2 )
                 return True
        sleep(10)
    if type: #清理文件
        for i in np.arange(1,totalnode):
            removefile(name+getmytag(True,mynode_))
        logger.warning("-----MASTER:同步失败"+name)
    异常终止("同步失败")
    return False


#防止卡顿
防止卡顿=True
#点击地图和发送消息都会中断人机。
def 点击移动(i=1):
    if existsTHENtouch(Template(r"tpl1691145668868.png", record_pos=(-0.298, 0.159), resolution=(960, 540))):
       for i in np.arange(1,i):
          if not existsTHENtouch(Template(r"tpl1691145668868.png", record_pos=(-0.298, 0.159), resolution=(960, 540)),"移动按钮",savepos=False): break
          sleep(1)
          return True
    else:
       return False
def 点击地图():
   return False
   if exists(Template(r"tpl1691126104293.png", record_pos=(-0.301, -0.106), resolution=(960, 540))):
       existsTHENtouch(Template(r"tpl1691126104293.png", record_pos=(-0.301, -0.106), resolution=(960, 540)),"展开地图",savepos=True)
       sleep(5)
       existsTHENtouch(Template(r"tpl1691126104293.png", record_pos=(-0.301, -0.106), resolution=(960, 540)),"展开地图",savepos=True)
       return True
   else:
       return False

def 发送消息():
   return False
   if exists(Template(r"tpl1691143770274.png", record_pos=(0.468, -0.066), resolution=(960, 540))):
       existsTHENtouch(Template(r"tpl1691143770274.png", record_pos=(0.468, -0.066), resolution=(960, 540)),"展开消息1",savepos=True)
       sleep(5)
       existsTHENtouch(Template(r"tpl1691126220807.png", record_pos=(0.4, -0.009), resolution=(960, 540)),"发送消息1",savepos=True)
       sleep(5)
       existsTHENtouch(Template(r"tpl1691143816075.png", record_pos=(0.471, -0.066), resolution=(960, 540))
,"关闭消息1",savepos=True)
       return True
   else:
       return False

# <--------------------- 自定义信息 ---------------------

def 异常处理_返回大厅(times=1):
    logger.warning("进入异常处理:%d"%(times))
    if 大厅中():
        return
    
    logger.warning("[异常]检测对战")
    if 对战中():
        sleep(60)
        while 对战中(): sleep(60)
        游戏结束()
        异常处理_返回大厅(times)
        return

    #登陆界面
    #更新公告
    更新公告=Template(r"tpl1692946575591.png", record_pos=(0.103, -0.235), resolution=(960, 540),threshold=0.9)
    if exists(更新公告):
        for igengxin in np.arange(30):
            logger.warning("更新中%d"%(igengxin))
            if exists(Template(r"tpl1692946702006.png", record_pos=(-0.009, -0.014), resolution=(960, 540),threshold=0.9)):
                logger.warning("更新完成")
                touch(Template(r"tpl1692946738054.png", record_pos=(-0.002, 0.116), resolution=(960, 540),threshold=0.9))
                sleep(60)
                break
            elif not exists(更新公告):
                logger.warning("找不到更新公告.break")
                break
            if exists(Template(r"tpl1692952266315.png", record_pos=(-0.411, 0.266), resolution=(960, 540),threshold=0.9)): logger.warning("正在下载资源包")
            sleep(60)
    if exists(Template(r"tpl1692946837840.png", record_pos=(-0.092, -0.166), resolution=(960, 540),threshold=0.9)):
        logger.warning("同意游戏")
        touch(Template(r"tpl1692946883784.png", record_pos=(0.092, 0.145), resolution=(960, 540),threshold=0.9))
    #这里需要重新登录了
    if exists(Template(r"tpl1692946938717.png", record_pos=(-0.108, 0.159), resolution=(960, 540),threshold=0.9)):
        异常终止("需要重新登录")
    if exists(Template(r"tpl1692951324205.png", record_pos=(0.005, -0.145), resolution=(960, 540))):
        logger.warning("关闭家长莫模式")
        touch(Template(r"tpl1692951358456.png", record_pos=(0.351, -0.175), resolution=(960, 540)))
        sleep(5)

    用户协议同意=Template(r"tpl1692952132065.png", record_pos=(0.062, 0.099), resolution=(960, 540),threshold=0.9)
    existsTHENtouch(用户协议同意,"用户协议同意")
            
    开始游戏=Template(r"tpl1692947242096.png", record_pos=(-0.004, 0.158), resolution=(960, 540),threshold=0.9)
    if existsTHENtouch(开始游戏,"登录界面.开始游戏",savepos=False): sleep(30)
    活动关闭图标=Template(r"tpl1692947351223.png", record_pos=(0.428, -0.205), resolution=(960, 540),threshold=0.9)
    while( existsTHENtouch(活动关闭图标,"活动关闭图标",savepos=False) ): sleep(15)
    登录礼物=Template(r"tpl1692951432616.png", record_pos=(0.346, -0.207), resolution=(960, 540))
    while( existsTHENtouch(登录礼物,"登录礼物图标",savepos=False) ): sleep(15)
    #更改设备图形
    existsTHENtouch(Template(r"tpl1692951507865.png", record_pos=(-0.106, 0.12), resolution=(960, 540),threshold=0.9),"关闭画面设置")
    if exists(Template(r"tpl1692951548745.png", record_pos=(0.005, 0.084), resolution=(960, 540))):
        关闭邀请=Template(r"tpl1692951558377.png", record_pos=(0.253, -0.147), resolution=(960, 540),threshold=0.9)
        while( existsTHENtouch(关闭邀请,"关闭邀请")):sleep(15)
        

    if 大厅中(): return True

    返回图标=Template(r"tpl1692949580380.png", record_pos=(-0.458, -0.25), resolution=(960, 540),threshold=0.9)

    while( existsTHENtouch(返回图标,"返回图标",savepos=False) ): sleep(10)

    if 大厅中(): return True
    times=times+1
    
    # 健康系统,或者其他问题选择重启APP
    if 健康系统():
        重启APP(设备信息["王者应用ID"],60*20)
        return 异常处理_返回大厅(times)
    
    if times < 15 and times%4 == 0:
        重启APP(设备信息["王者应用ID"],60)
    #
    if times > 15:
        异常终止("无法返回大厅")
    
    return 异常处理_返回大厅(times)


        
    
    #返回

#
def 手动返回房间(name=''):
    #手动返回房间
    for loop in range(60):
        if 房间中(): return True
        logger.warning(name+":无法进入房间,请手动操作")
        sleep(5)
    异常终止("多开无法返回房间")
    return False    
#@todo
def 邀请辅助():
    return


def 进入房间(times=1):
    global 返回房间
    global 快速点击
#
    if 对战中():
        sleep(60)
        while 对战中(): sleep(60)
        游戏结束()   
#
    if 房间中():
        return
    times=times+1
    if times > 10: 异常终止("无法进入房间")

    #
    #
    异常处理_返回大厅()
    logger.warning("大厅中.开始进入房间")
    #wait等待元素出现，没出现就执行intervalfunc
    if not existsTHENtouch(Template(r"tpl1689666004542.png", record_pos=(-0.102, 0.145), resolution=(960, 540)),"对战",savepos=False):
        logger.error("选择对战失败")
        进入房间(times); return
    sleep(2)
    if not existsTHENtouch(Template(r"tpl1689666019941.png", record_pos=(-0.401, 0.098), resolution=(960, 540)),"5v5王者峡谷",savepos=False):
        进入房间(times); return
    sleep(2)
    if not existsTHENtouch(Template(r"tpl1689666034409.png", record_pos=(0.056, 0.087), resolution=(960, 540)),"人机",savepos=False):
        进入房间(times); return        
    sleep(2)
    if not 快速点击:
        if not existsTHENtouch(Template(r"tpl1689666057241.png", record_pos=(-0.308, -0.024), resolution=(960, 540)),"快速模式"):
        #if not existsTHENtouch(Template(r"tpl1689666069306.png", record_pos=(-0.302, -0.136), resolution=(960, 540)),"标准模式"):
            进入房间(times); return         
        #
        # 选择难度
        global 青铜段位
        青铜段位=True
        if 青铜段位:
            段位=Template(r"tpl1689666083204.png", record_pos=(0.014, -0.148), resolution=(960, 540))
        else:
            段位=Template(r"tpl1689666092009.png", record_pos=(0.0, 0.111), resolution=(960, 540))
        existsTHENtouch(段位,"选择段位")
    #
    # 开始练习
    开始练习 = Template(r"tpl1689666102973.png", record_pos=(0.323, 0.161), resolution=(960, 540))

    if not existsTHENtouch(开始练习,"开始练习"): os.kill(os.getpid(), signal.SIGINT)  # 退出程序
    sleep(2)
    #
    #当没有弹出确定匹配时
    if not exists(Template(r"tpl1689666117573.png", record_pos=(0.096, 0.232), resolution=(960, 540))):
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
        while existsTHENtouch(Template(r"tpl1689667950453.png", record_pos=(-0.001, 0.111), resolution=(960, 540))):
            logger.warning("不同意被禁赛了")
            sleep(30)
            if not existsTHENtouch(开始练习,"开始练习"): os.kill(os.getpid(), signal.SIGINT)

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
            if existsTHENtouch(Template(r"tpl1689666117573.png", record_pos=(0.096, 0.232), resolution=(960, 540))):
                break
            sleep(1)
        logger.warning("确认匹配")
    else:
        logger.warning("辅助确认匹配")

    队友确认匹配=False
    # 确认匹配
    for loop in range(60*5*10):#等待时间太长
        if existsTHENtouch(Template(r"tpl1689666290543.png", record_pos=(-0.001, 0.152), resolution=(960, 540))):
            #英雄和皮肤按钮出来才可以
            for loop2 in range(60*5*2): #等待进入英雄界面
                if exists(Template(r"tpl1689666311144.png", record_pos=(-0.394, -0.257), resolution=(960, 540))):
                     队友确认匹配=True
                     break
                sleep(1)
            if 队友确认匹配: break
        sleep(1)
    #选择英雄
    if  not 队友确认匹配: logger.warning("队友未确认匹配")
    global 选择英雄
    if not 选择英雄: sleep(30)
    if 选择英雄:
        #显示全部英雄.png
        existsTHENtouch(Template(r"tpl1689666324375.png", record_pos=(-0.297, -0.022), resolution=(960, 540)),"展开英雄",savepos=True)
        sleep(1)
        existsTHENtouch(英雄属性["参战英雄线路"],"参战英雄线路",savepos=True)
        sleep(7)
        existsTHENtouch(英雄属性["参战英雄"],"参战英雄",savepos=True)
        sleep(1)
        #分路重复.png
        if exists(Template(r"tpl1689668119154.png", record_pos=(0.0, -0.156), resolution=(960, 540))):
            logger.warning("分路冲突，切换英雄")
            #分路重复取消按钮.png
            existsTHENtouch(Template(r"tpl1689668138416.png", record_pos=(-0.095, 0.191), resolution=(960, 540)),"冲突取消英雄",savepos=True)
            #选择备选英雄
            existsTHENtouch(英雄属性["备战英雄线路"],"备战英雄线路",savepos=True)
            existsTHENtouch(英雄属性["备战英雄"],"备战英雄",savepos=True)
        #确定英雄后一般要等待队友确定，这需要时间
        sleep(5)
        #   确定
        existsTHENtouch(Template(r"tpl1689666339749.png", record_pos=(0.421, 0.237), resolution=(960, 540)),"确定英雄",savepos=True) #这里是用savepos的好处就是那个英雄的熟练度低点哪个英雄
        sleep(5)
        #万一是房主
        existsTHENtouch(Template(r"tpl1689666339749.png", record_pos=(0.421, 0.237), resolution=(960, 540)),"确定阵容",savepos=True)
        sleep(5)
    sleep(20)
    #加油拳头
    existsTHENtouch(Template(r"tpl1689666367752.png", record_pos=(0.42, -0.001), resolution=(960, 540)),"加油按钮",savepos=True)
    logger.warning("等待游戏结束...倒计时")
    #sleep(350) #游戏时间很长的,倒计时转移到游戏结束()




def 启动王者荣耀():
    global 辅助
    logger.warning("连接设备")
    if device:
        logger.warning("设备连接成功")
    else:
        logger.warning("设备连接失败")
        return
    logger.warning("启动 王者荣耀")
    #   我们提前打开软件了就直接return了
    if 辅助:
        logger.warning("+++辅助模式+++")
        if 对战中(True):
            sleep(60)
            while 对战中(True): sleep(10)
            游戏结束()   
    if 大厅中():
        return
    elif 房间中():
        return
    else:
       logger.warning("未能进入房间或大厅")
       异常处理_返回大厅() #这里进行关闭程序和打开的操作
    #
    if not 大厅中():
        异常终止("无法进入大厅")
    return



def 大厅中():
    if exists(Template(r"tpl1689667333420.png", record_pos=(-0.176, 0.144), resolution=(960, 540))):
        logger.warning("正在大厅中")
        return True


def 对战中(处理=False):
    对战=Template(r"tpl1689666416575.png", record_pos=(0.362, 0.2), resolution=(960, 540))
    global 防止卡顿
    if exists(对战):
        logger.warning("正在对战中")
        if 防止卡顿: 点击移动(1)
        if 处理:
            timelimit(timekey="endgame",limit=60*20,init=True)
            while existsTHENtouch(对战):
                logger.warning("加速对战中")
                if 点击地图(): 发送消息()
                sleep(10) #
                if timelimit(timekey="endgame",limit=60*20,init=False): 异常终止("对战中游戏时间过长")
        
        return True
    #
    return False

def 房间中():
    #长平之战等满人状态时
    if exists(Template(r"tpl1691463676972.png", record_pos=(0.356, -0.258), resolution=(960, 540))):
        logger.warning("正在房间中[文字判断]")
        return True        
    if exists(Template(r"tpl1690442701046.png", record_pos=(0.135, -0.029), resolution=(960, 540))):
        logger.warning("正在房间中")
        return True
    else:
        return False

def 健康系统():
    #呵护双眼，请您休息
    if exists(Template(r"tpl1689666921933.png", record_pos=(0.122, -0.104), resolution=(960, 540))):
        logger.warning("您已禁赛")
        return True
    return False

def 重启APP(ID,time=0): #ID=设备信息["王者应用ID"]
    stop_app(ID)
    logger.warning("关闭程序")
    printtime=30
    #这个时间就是给健康系统准备的
    for i in np.arange(int(time/printtime)):
        print("sleep: %d"%(i),end='\r')
        sleep(printtime)
    start_app(ID)
    sleep(30)


def 游戏结束():
    jixu=False
    global 返回房间
    global 辅助
    global mynode
    global totalnode
    ionode = mynode == 0
    endgamefile="endgame."+str(totalnode)+".txt"
    first = totalnode > 1
    if 辅助 and ionode: removefile(endgamefile) #endgame会在此处初始化删除,后面无需删除
    #
    barriernode(type=英雄属性["type"],name="checkend_init")
    timelimit(timekey="endgame",limit=60*20,init=True)
    while True:
        if timelimit(timekey="endgame",limit=60*20,init=False): 异常终止("结束游戏时间过长")
        if 健康系统():
            if 辅助:
                异常终止("健康系统.辅助END")
            else:
                异常处理_返回大厅()
                return
        #减少判断游戏结束的资源占用
        if not jixu:
            if 防止卡顿: 点击移动(1)
        if first:
            if ionode:
               if jixu: touchfile(endgamefile)
            else:
               if os.path.exists(endgamefile):
                   jixu = True
                   logger.warning("收到主节点继续信号")
               else:
                   logger.warning("等待主节点继续信号")
                   sleep(20)
                   continue
            if jixu: first = False

        #分享和返回房间的按键有些冲突
        #
        #有时候会莫名进入分享界面
        if exists(Template(r"tpl1689667038979.png", record_pos=(0.193, 0.231), resolution=(960, 540))):
            logger.warning("分享界面")
            existsTHENtouch(Template(r"tpl1689667050980.png", record_pos=(-0.443, -0.251), resolution=(960, 540)))
            jixu=True
            sleep(2)
        
        #有时候会莫名进入MVP分享界面
        pos=exists(Template(r"tpl1689727624208.png", record_pos=(0.235, -0.125), resolution=(960, 540)))
        if pos:
            logger.warning("mvp分享界面")
            existsTHENtouch(Template(r"tpl1689667050980.png", record_pos=(-0.443, -0.251), resolution=(960, 540)))
            jixu=True
            sleep(2)
        #
        #都尝试一次返回
        if existsTHENtouch(Template(r"tpl1689667050980.png", record_pos=(-0.443, -0.251), resolution=(960, 540))):
            sleep(2)
        
        if existsTHENtouch(Template(r"tpl1689667161679.png", record_pos=(-0.001, 0.226), resolution=(960, 540))):
            logger.warning("MVP继续")
            jixu=True
            sleep(2)
            
        #胜利页面继续
        if existsTHENtouch(Template(r"tpl1689668968217.png", record_pos=(0.002, 0.226), resolution=(960, 540))):                        
            logger.warning("继续1/3")
            jixu=True
            sleep(2)
        #显示mvp继续
        if existsTHENtouch(Template(r"tpl1689669015851.png", record_pos=(-0.002, 0.225), resolution=(960, 540))):
            logger.warning("继续2/3")
            jixu=True
            sleep(2)
        if existsTHENtouch(Template(r"tpl1689669071283.png", record_pos=(-0.001, -0.036), resolution=(960, 540))):
            logger.warning("友情积分继续2/3")
            jixu=True
            existsTHENtouch(Template(r"tpl1689669113076.png", record_pos=(-0.002, 0.179), resolution=(960, 540)))
            sleep(2)

        #todo, 暂时为空
        if existsTHENtouch(Template(r"tpl1689670032299.png", record_pos=(-0.098, 0.217), resolution=(960, 540))):
            logger.warning("超神继续3/3")
            jixu=True
            sleep(2)
        #
        #
        if first and jixu : continue
        #
        if os.path.exists("EXIT.txt"):
            异常终止("监测到EXIT,停止程序")

        if os.path.exists("END.txt"):
            logger.warning("监测到END,停止程序.保留王者")
            os.kill(os.getpid(), signal.SIGINT)  # 退出程序  
        sleep(10)  
        if 辅助: sleep(10) #辅助时多停留
        if not jixu:
            logger.warning("未监测到继续,sleep...")
            continue
        #
        if 返回房间:
            if 房间中(): break
        # 返回大厅
        # 因为不能保证返回辅助账户返回房间，所以返回大厅更稳妥
        if exists(Template(r"tpl1689667212477.png", record_pos=(-0.001, 0.223), resolution=(960, 540))):
            if 返回房间:
                if existsTHENtouch(Template(r"tpl1689667226045.png", record_pos=(0.079, 0.226), resolution=(960, 540)),"返回房间",savepos=True):
                    sleep(10)
#@todo ,添加barrier
                    if 房间中(): break
                    continue
        if not 辅助:
            if existsTHENtouch(Template(r"tpl1689667243845.png", record_pos=(-0.082, 0.221), resolution=(960, 540)),"返回大厅"):
                sleep(5)
                if existsTHENtouch(Template(r"tpl1689667256973.png", record_pos=(0.094, 0.115), resolution=(960, 540)),"确定返回大厅",savepos=True):
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
    #if not 辅助:
    #    os.kill(os.getpid(), signal.SIGUSR1)
    logger.warning("程序退出")
    os.kill(os.getpid(), signal.SIGTERM)


def 王者子进程(mynode_,设备类型, 设备IP地址):
    print(设备类型)
    print(设备IP地址)
    global 英雄属性
    global 设备信息
    global device
    global 次数
    global 次数2
    global 辅助
    global totalnode
    global mynode
    global multi_run
    mynode=mynode_
    type = mynode == 0
    #signal.signal(signal.SIGUSR1, handler2)
    #
    #
    if multi_run and False:
        if not type:
            filename='out'+str(mynode)+'.txt'
            logger.warning("王者子进程"+str(mynode)+"重定向输出到"+filename)
            logfile=open(filename, 'w+')
            sys.stdout=logfile #无效，无法把logger.warning 改位置
            sys.stderrs=logfile

    logger.warning("王者子进程mynode"+str(mynode))
    英雄属性={}
    英雄属性["type"]=type
    英雄属性["想玩位置"]=想玩位置
    英雄属性["参战英雄"]=参战英雄头像_dict[mynode]
    英雄属性["参战英雄线路"]=参战英雄线路_dict[mynode]
    英雄属性["备战英雄"]=参战英雄头像_dict[(mynode+2)%totalnode]
    英雄属性["备战英雄线路"]=参战英雄线路_dict[(mynode+2)%totalnode]

    设备信息 = {
        "链接": format("{}:///{}".format(设备类型, 设备IP地址)),
        "王者应用ID": "com.tencent.tmgp.sgame"
    }
    #
    if 设备类型 == "iOS":
        设备信息 = {
            "链接": format("{}:///{}".format(设备类型, 设备IP地址)),
            "王者应用ID": "com.tencent.smoba"
        }
    次数2 = 次数
    barriernode(type,"启动游戏")
    sleep(mynode)
    #
    atexit.register(重启游戏) #----------
    #exit()
    #device = connect_device("Android:///192.168.12.211:43069")
    #重启游戏()
    if multi_run and False:
        if not type: logfile.close()


def 重启游戏():
    logger.warning("重启游戏")
    global 次数
    global 次数2
    global device
    global 英雄属性
    global position_dict
    global position_dict_file
    global 辅助
    #
    global mynode
    if 辅助:
        position_dict_file=getmytag(英雄属性["type"],mynode)+"position_dict.txt"
        position_dict=read_dict(position_dict_file)
    else:
        position_dict=read_dict(position_dict_file)
    #
    device = False
    #
    if 次数 <= 0:
        return
    for k in range(次数):
        次数2 -= 1
        logger.warning("第 {} 次运行子程序".format(k+1))
        #这里只负责打开程序
        if not device:
            #-------------------
            device = connect_device(设备信息["链接"])
            #-------------------
            logger.warning("设备信息: {}".format(设备信息))
            启动王者荣耀() 
        
        #当多人组队模式时，这里要暂时保证是房间中，因为邀请系统还没写好
        if 辅助:
            返回房间=True
            手动返回房间("startgame")
            if not barriernode(type=英雄属性["type"],name="room"):
                logger.warning("游戏房间.同步失败")
                #这里考虑，加一个退出游戏
            #此处加一个邀请系统
        else: #非辅助模式.可以暴力点，直接重启
            异常处理_返回大厅()
        #匹配游戏中包含进入房间的代码
        sleep(5)
        匹配游戏()
        global 加速对战
        if 辅助:
            #barrier
            if not barriernode(type=英雄属性["type"],name="gaming"):
                logger.warning("匹配游戏.同步失败")
                #if k >= 10: 加速对战=True
        if 加速对战:
            logger.warning("加速对战>>>>")
            for iwait in np.arange(60):
                if 对战中(True): break
                sleep(5) #等待开始游戏
        else:
            for isleep in np.arange(15):
                if 防止卡顿: 点击移动(1)
                sleep(20)
        sleep_time=60
        sleeploop=0
        logger.warning("2此加速对战")
        while 对战中(加速对战): 
            logger.warning("等待对战结束")
            sleep_time=max(10,sleep_time/2*1.7)
            sleep(sleep_time)
            sleeploop=sleeploop+1
            if 防止卡顿: 点击移动(1)
            if sleeploop > 10: break #虚拟机王者程序卡住了
        #device.disconnect()
        #device = connect_device(设备信息["链接"])
        logger.warning("对战结束")
        游戏结束()
        if 辅助:
            if not barriernode(type=英雄属性["type"],name="endgame"):
                logger.warning("游戏结束.同步失败")
        #
        save_dict(position_dict,position_dict_file)
        logger.warning("游戏已结束. sleep一段时间进入下层循环")
    异常终止("正常结束循环.关闭游戏")

if len(sys.argv) > 1:
    if sys.argv[1] == "-f":
        辅助 = True
        logger.warning("辅助英雄 启用")



if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler)
    logger.warning("len(sys.argv)="+str(len(sys.argv)))
    辅助=True

def multi_start(i):
    #可以并行，但是不可以在此处设置global变量
    #在后续函数(如王者子进程)中设置global mynode是可以的
    #这里mynode只是局域变量
    mynode=i
    logger.warning("mynode"+str(mynode))
    sleep(mynode)
    王者子进程(mynode, 设备类型=设备类型_dict[mynode],设备IP地址=设备IP地址_dict[mynode])


if len(sys.argv) > 3:  #多进程，multi_run 运行
    multi_run=True
    totalnode=int(sys.argv[1])
if len(sys.argv) == 3: #多进程，主节点
    辅助=True
    totalnode=int(sys.argv[1])
    mynode=int(sys.argv[2])
if len(sys.argv) == 2: #多进程，自动节点,根据手动执行的速度进行
    辅助=True
    totalnode=int(sys.argv[1])
    if totalnode > 0:
        mynode=autonode(totalnode)
    else:
        totalnode=-totalnode
        multi_run=True
    

if len(sys.argv) == 1:
    辅助=False
    mynode=0
    totalnode=1

removefile("EXIT.txt")
removefile("END.txt")

if  not multi_run:
    print("+++++++++++INFO++++++++++++++++")
    print("+++++++ node %d / %d ++++++++++"%(mynode,totalnode))
    王者子进程(mynode, 设备类型=设备类型_dict[mynode],设备IP地址=设备IP地址_dict[mynode])
 
else:
    #import  multiprocessing
    multi_run=True
    from pathos import multiprocessing
    m_process=totalnode
    #barrier=multiprocessing.Barrier(totalnode)
    m_cpu = [i for i in range(0, m_process)]
    if __name__ == '__main__':
        p = multiprocessing.Pool(m_process)
        out = p.map_async(multi_start,m_cpu).get()
        p.close()
        p.join()






