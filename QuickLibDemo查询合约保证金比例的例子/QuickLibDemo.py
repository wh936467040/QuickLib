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
        result=trader.QryExchangeMarginRate(u'rb1701',QL_Long);
        if result==-1:
            print (u'CTPTrader初始化未完成\n')
        elif result==-2:
            print (u'没找到该合约多单保证金比例数据\n') 
        elif result==-3:
            print (u'查询超时\n')
        else:
            print (u'rb1701 多单保证金比例：%0.02f'%result)      
        time.sleep(1)  #sleep1秒，防止死循环导致CPU占有率过高，1即可，不宜过大，若过大会导致程序进程长时间无响应，丢失行情数据
        result=trader.QryExchangeMarginRate('rb1701',QL_Short);
        if result==-1:
            print (u'CTPTrader初始化未完成\n')
        elif result==-2:
            print (u'没找到该合约空单保证金比例\n') 
        elif result==-3:
            print (u'查询超时\n')
        else:
            print (u'rb1701 空单保证金比例：%0.02f'%result)              
        time.sleep(1)  #sleep1秒，防止死循环导致CPU占有率过高，1即可，不宜过大，若过大会导致程序进程长时间无响应，丢失行情数据
        print '--------------------------------------------------------'

if __name__ == '__main__':
    main()
    

    
 
    
    
    