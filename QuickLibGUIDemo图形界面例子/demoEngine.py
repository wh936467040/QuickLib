# encoding: UTF-8

"""
该文件中包含的是交易平台的中间层，
将API和事件引擎包装到一个主引擎类中，便于管理。

当客户想采用服务器-客户机模式，实现交易功能放在托管机房，
而图形控制功能在本地电脑时，该主引擎负责实现远程通讯。
"""

import sys
from datetime import date
from time import sleep
import shelve

from PyQt4 import QtCore
 
from eventEngine import EventEngine


########################################################################
class MainEngine:
    """主引擎，负责对API的调度"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.ee = EventEngine()         # 创建事件驱动引擎
        
 
        self.ee.start()                 # 启动事件驱动引擎
        
        # 循环查询持仓和账户相关
        self.countGet = 0               # 查询延时计数
        self.lastGet = 'Account'        # 上次查询的性质
 
        
        # 合约储存相关
        self.dictInstrument = {}        # 字典（保存合约查询数据）
 
        
    #----------------------------------------------------------------------
  
    #----------------------------------------------------------------------
    def exit(self):
        """退出"""
        # 销毁API对象
        self.td = None
        self.md = None
        
        # 停止事件驱动引擎
        self.ee.stop()
        
 