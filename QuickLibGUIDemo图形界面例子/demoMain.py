# encoding: UTF-8

"""
该文件中包含的是交易平台的主函数，
将底层、中层、上层的功能导入，并运行。
"""

import ctypes
import sys

from demoEngine import MainEngine
from demoUi import *

 


#----------------------------------------------------------------------
def main():
    """主程序入口"""
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('QucikLib')  # win7以下请注释掉该行   
    
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('main.ico'))
    
    me = MainEngine()
    
    mw = MainWindow(me.ee, me)

 
 
 
    mw.setFixedSize(1000,620)  #设置窗体固定大小 
 
  
    mw.showMaximized()
 
    #窗口居中
    mw.screen = QtGui.QDesktopWidget().screenGeometry()
    mw.size = mw.geometry()
    mw.move((mw.screen.width()-mw.size.width())/2, (mw.screen.height()-mw.size.height())/2)   
    mw.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
