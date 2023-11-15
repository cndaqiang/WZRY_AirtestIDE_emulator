# 王者熟练度工具使用方法

## 后续更新
https://github.com/cndaqiang/AirTest_MobileAuto_WZRY

## 代码开发airtest

### 安装

1. 打开网页 https://airtest.netease.com/ 下载安装
2. 打开软件 软件最上面有一个 Options 点击 出现 `Language` 选择 `简体中文`
3. 打开软件 软件最上面有一个 `文件` 点击 `打开脚本`

## airtest修改代码和运行
1. 显示手机画面
2. 使用`touch`,截取手机画面上的图片(代码格式)
3. 是用截取的图片替换原有代码中的图片

### airtest版终端运行
通过观察airtest的运行日志发现可以
```
#
"/Applications/AirtestIDE.app/Contents/MacOS/AirtestIDE" pyrunner "/Users/cndaqiang/Desktop/WZRY_AirtestIDE-main/XiaoMI11.py" 
```

### python版终端运行
- `duokai.py` 模拟器并行多开,分辨率960*540,2G运行,5帧画面
- `ln -s duokai.py monizhan.py; ./monizhan.py` 模拟战刷信誉分
- `ln -s duokai.py debug.py; ./debug.py` debug模式
- XiaoMI11.py 以前的脚本,小米11专用

```
#多线程模式
python -u .\duokai.py -totalnode
#手动执行多线程,每个终端(共totalnode个终端)均执行下面的命令
python -u .\duokai.py totalnode
```


## 模拟器推荐
- Windows Bluestack 多开adb都可以,还兼容hyper-v(Pie 64bit).  不兼容hyper-v的**Nougat模式**好像更省电，适合不用开wsl的笔记本,而且adb的端口也不会变
- Linux使用[remote-android](https://github.com/remote-android/),支持arm服务器
- Mac .没发现好用还能无线adb调试的.

## 其他
### 连接手机(无线ADB调试)
ADB连接
```
(base) cndaqiang@macmini mac$ pwd
/Applications/AirtestIDE.app/Contents/Resources/plugins/firebase_plugin/tool/copy_app/airtest/core/android/static/adb/mac
(base) cndaqiang@macmini mac$ ./adb devices
List of devices attached
8553e6ac	device

(base) cndaqiang@macmini mac$ ./adb tcpip 5555
adb server version (40) doesn't match this client (39); killing...
* daemon started successfully *

restarting in TCP mode port: 5555
```

### mac模拟器[不推荐]
```
#parallel desktop安装bliss
#bliss 开始adb
#kernelSu 授予termux root权限
#termux 执行(因为bliss无法识别wifi，把网络识别成了有线网卡，不能利用安卓本文的无线调试，所以只能这样)
su
setprop service.adb.tcp.port 5555
stop adbd
start adbd
#就可以用局域网调试了
wm size 960x540
wm density 120
#上面这样设置完成后,重启也能保存,不用重新输入命令
(base) cndaqiang@macmini ChromeDownload$ adb shell
Parallels Virtual Platform:/ $ wm size
Physical size: 1024x768
Override size: 960x540
#重启后需要断开pc的adb重新连接
adb kill-server
adb connect 10.211.55.19:5555
#安装游戏
adb install 10040714_com.tencent.tmgp.sgame_a2680838_8.4.1.6_fL2tC9.apk
```

注有些手机连接不上,找找原因
