#导入CTP交易库
from CTPTrader import *
trader = CTPTrader()   #交易接口类赋值给变量 

# main()为程序入口函数，所有的行情、交易订阅、指标调用、下单的逻辑均写在此函数内执行
def main():

    print(u"官方QQ群 5172183 \n");

    retLogin = trader.Login()  #调用交易接口元素，通过 “ 接口变量.元素（接口类内部定义的方法或变量） ” 形式调用
    # Login()，不需要参数，Login读取QuickLibTD.ini的配置信息，并登录
    # 返回0， 表示登录成功，
    # 返回1， FutureTDAccount.ini错误
    # 返回2， 登录超时
    print ('login: ', retLogin)   
    if retLogin==0:
        print u'登陆交易成功'
    else:
        print u'登陆交易失败'
    
    #持仓数据在后台更新时，参数True为显示持仓状态，False为不显示持仓状态（仅对控制台有效）   
    trader.SetShowPosition(True)
 
    #注意simnow模拟盘的交易服务器不稳定，经常会出现查询不到的情况。实盘账户绑定的交易服务器无此问题。
    
    while(1):  #死循环，反复执行
        #如果值为-999999999（初始值），则表示尚未获得数据
        print (u'(1)动态权益：%0.02f'%trader.QryBalance(True))
        print (u'(2)静态权益：%0.02f'%trader.QryBalance(False))      
        print (u'(3)可用资金：%0.02f'%trader.QryAvailable())
        print (u'(4)zn1701今日空单持仓：%d'%trader.QryPosition('rb1701',QL_POSITION_Sell_Today))   
        print (u'(5)zn1701今日多单持仓：%d'%trader.QryPosition('rb1701',QL_POSITION_Buy_Today))   
        print (u'(6)zn1701非今日空单持仓：%d'%trader.QryPosition('rb1701',QL_POSITION_Sell_History))   
        print (u'(7)zn1701非今日多单持仓：%d'%trader.QryPosition('rb1701',QL_POSITION_Buy_History))   
        print (u'(8)zn1701空单持仓总计：%d'%trader.QryPosition('rb1701',QL_POSITION_Sell_All))   
        print (u'(9)zn1701多单持仓总计：%d'%trader.QryPosition('rb1701',QL_POSITION_Buy_All))   
        
        print '--------------------------------------------------------'
        time.sleep(3)  #sleep1秒，防止死循环导致CPU占有率过高，1即可，不宜过大，若过大会导致程序进程长时间无响应，丢失行情数据

if __name__ == '__main__':
    main()
    

    
 
    
    
    