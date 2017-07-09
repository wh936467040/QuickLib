#导入CTP交易库
from CTPTrader import *
trader = CTPTrader()   #交易接口类赋值给变量 


#------------------------------------------TD回调函数、相关变量结束----------------------------------------------
#回调类型
TD_EMPTY                    = 8000 #登录成功
TD_LOGIN_SCUESS             = 8001 #登录成功
TD_LOGIN_DENIED             = 8002 #登录被拒绝
TD_LOGIN_ERRORPASSWORD      = 8003 #密码错误
TD_LOGINOUT_SCUESS          = 8004 #登出成功
TD_NETCONNECT_SCUESS        = 8005 #连接成功
TD_NETCONNECT_BREAK         = 8006 #断开连接
TD_NETCONNECT_FAILER        = 8007 #连接失败
#TD_SUBCRIBE_SCUESS         = 8008 #订阅成功
#TD_UNSUBCRIBE_SCUESS       = 8009 #取消订阅成功 
#TD_NEWTICK                 = 8010 #新Tick到来 
TD_ERROR                    = 8011 #错误应答 
TD_ORDER_INFO               = 8012 #订单回报
TD_SETTLEMENTINFOCONFIRM    = 8013 #结算单确认回调
TD_MAXORDERVOLUME           = 8014 #最大允许报单数量回调

def TD_OnEmptyCmd():
    #回调指令缓冲区已为空（因为短时间获得多个指令，时间间隔态度，在下面的for i in range(market.GetUnGetCmdSize()):循环执行了多次已经完成了）
    print "---------------TD_OnEmptyCmd---------------"
    
def TD_OnUserLogin():
    #登录成功
    print "---------------TD_OnUserLogin---------------"   
    data = cast(trader.GetCmdContent_LoginScuess(), POINTER(QL_CThostFtdcRspUserLoginField))
    print "TradingDay %s"%(str(data[0].TradingDay))              #交易日
    print "LoginTime %s"%(str(data[0].LoginTime))                #登录成功时间
    print "BrokerID %s"%(str(data[0].BrokerID))                  #经纪公司代码
    print "UserID %s"%(str(data[0].UserID))                      #用户代码        
    print "SystemName %s"%(str(data[0].SystemName))              #交易系统名称
    print "FrontID %s"%(str(data[0].FrontID))                    #前置编号     
    print "SessionID %s"%(str(data[0].SessionID))                #会话编号
    print "MaxOrderRef %s"%(str(data[0].MaxOrderRef))            #最大报单引用
    print "SHFETime %s"%(str(data[0].SHFETime))                  #上期所时间
    print "DCETime %s"%(str(data[0].DCETime))                    #大商所时间
    print "CZCETime %s"%(str(data[0].CZCETime))                  #郑商所时间
    print "FFEXTime %s"%(str(data[0].FFEXTime))                  #中金所时间       
    print "INETime %s"%(str(data[0].INETime))                    #能源中心时间
    
def TD_OnUserLoginDenied():
    #登录被拒绝
    print "---------------TD_OnUserLoginDenied---------------"       
    
def TD_OnUserLoginErrPassword():
    #登录密码错误
    print "---------------TD_OnUserLoginErrPassword---------------"       
    
def TD_OnUserLogout():
    #登出成功
    print "---------------TD_OnUserLogout---------------"    

def TD_OnFrontConnected():
    #连接成功
    print "---------------TD_OnFrontConnected---------------"       
    
def TD_OnFrontDisconnected():
    #断开连接
    print "---------------TD_OnFrontDisconnected---------------"    
    
def TD_OnFrontConnectedFailer():
    #连接失败
    print "---------------TD_OnFrontConnectedFailer---------------"
    
def TD_OnError():
    #错误信息回报
    print "---------------TD_OnRspError---------------"   
    data = cast(trader.GetCmdContent_Error(), POINTER(QL_CThostFtdcRspInfoField))
    print "ErrorID %s"%(str(data[0].ErrorID))              #错误代码
    print "ErrorMsg %s"%(str(data[0].ErrorMsg))            #错误信息

def TD_OnOrder():
    #订单回报
    print "---------------TD_OnRspOrder---------------"
    data = cast(trader.GetCmdContent_Order(), POINTER(QL_CThostFtdcOrderField))    
    print "BrokerID %s"%(str(data[0].BrokerID))            #经纪公司代码
    print "InvestorID %s"%(str(data[0].InvestorID))
    print "InstrumentID %s"%(str(data[0].InstrumentID))
    print "OrderRef %s"%(str(data[0].OrderRef))    
    print "UserID %s"%(str(data[0].UserID))
    print "OrderPriceType %s"%(str(data[0].OrderPriceType))
    print "Direction %s"%(str(data[0].Direction))
    print "CombOffsetFlag %s"%(str(data[0].CombOffsetFlag))    
    print "CombHedgeFlag %s"%(str(data[0].CombHedgeFlag))
    print "LimitPrice %s"%(str(data[0].LimitPrice))    
    print "VolumeTotalOriginal %s"%(str(data[0].VolumeTotalOriginal))
    print "TimeCondition %s"%(str(data[0].TimeCondition))    
    print "GTDDate %s"%(str(data[0].GTDDate))        
    print "MinVolume %s"%(str(data[0].MinVolume))    
    print "ContingentCondition %s"%(str(data[0].ContingentCondition))        
    print "StopPrice %s"%(str(data[0].StopPrice))    
    print "ForceCloseReason %s"%(str(data[0].ForceCloseReason))
    print "IsAutoSuspend %s"%(str(data[0].IsAutoSuspend))    
    print "BusinessUnit %s"%(str(data[0].BusinessUnit))
    print "RequestID %s"%(str(data[0].RequestID))    
    print "OrderLocalID %s"%(str(data[0].OrderLocalID))
    print "ExchangeID %s"%(str(data[0].ExchangeID))    
    print "ParticipantID %s"%(str(data[0].ParticipantID))
    print "ClientID %s"%(str(data[0].ClientID))    
    print "ExchangeInstID %s"%(str(data[0].ExchangeInstID))
    print "TraderID %s"%(str(data[0].TraderID))    
    print "InstallID %s"%(str(data[0].InstallID))
    print "OrderSubmitStatus %s"%(str(data[0].OrderSubmitStatus))    
    print "NotifySequence %s"%(str(data[0].NotifySequence))  
    print "TradingDay %s"%(str(data[0].TradingDay))    
    print "SettlementID %s"%(str(data[0].SettlementID))      
    print "OrderSysID %s"%(str(data[0].OrderSysID))    
    print "OrderSource %s"%(str(data[0].OrderSource))          
    print "OrderStatus %s"%(str(data[0].OrderStatus))
    print "OrderType %s"%(str(data[0].OrderType))    
    print "VolumeTraded %s"%(str(data[0].VolumeTraded))          
    print "VolumeTotal %s"%(str(data[0].VolumeTotal))
    
def TD_OnSettlementInfoConfirm():
    #结算确认回报
    print "---------------TD_OnRspSettlementInfoConfirm---------------"   
    data = cast(trader.GetCmdContent_Settlement(), POINTER(QL_CThostFtdcSettlementInfoConfirmField))
    print "BrokerID %s"%(str(data[0].BrokerID))              #经纪公司代码
    print "InvestorID %s"%(str(data[0].InvestorID))          #投资者代码
    print "ConfirmDate %s"%(str(data[0].ConfirmDate))        #确认日期
    print "ConfirmTime %s"%(str(data[0].ConfirmTime))        #确认时间
    
def TD_OnMaxOrderVolume():
    #查询最大报单数量响应
    print "---------------TD_OnRspSettlementInfoConfirm---------------"   
    data = cast(trader.GetCmdContent_Settlement(), POINTER(QL_CThostFtdcQueryMaxOrderVolumeField))
    print "BrokerID %s"%(str(data[0].BrokerID))              #经纪公司代码
    print "InvestorID %s"%(str(data[0].InvestorID))          #投资者代码
    print "InstrumentID %s"%(str(data[0].InstrumentID))      #合约代码
    print "Direction %s"%(str(data[0].Direction))            #买卖方向      
    print "OffsetFlag %s"%(str(data[0].OffsetFlag))          #开平标志
    print "HedgeFlag %s"%(str(data[0].HedgeFlag))            #投机套保标志
    print "MaxVolume %s"%(str(data[0].MaxVolume))            #最大允许报单数量
tddict={
          TD_EMPTY:TD_OnEmptyCmd,
          TD_LOGIN_SCUESS:TD_OnUserLogin,
          TD_LOGIN_DENIED:TD_OnUserLoginDenied,
          TD_LOGIN_ERRORPASSWORD:TD_OnUserLoginErrPassword,
          TD_LOGINOUT_SCUESS:TD_OnUserLogout,
          TD_NETCONNECT_SCUESS:TD_OnFrontConnected,
          TD_NETCONNECT_BREAK:TD_OnFrontDisconnected,
          TD_NETCONNECT_FAILER:TD_OnFrontConnectedFailer,
          TD_ERROR:TD_OnError,
          TD_ORDER_INFO:TD_OnOrder,
          TD_SETTLEMENTINFOCONFIRM:TD_OnSettlementInfoConfirm,
          TD_MAXORDERVOLUME:TD_OnMaxOrderVolume
        }

#------------------------------------------TD回调函数、相关变量结束----------------------------------------------

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
        print(u"Wait for a New Cmd\n");
        #消息驱动，包括了各种回调，在没有消息到来时，一直处于阻塞状态，不占用CPU。当回调函数内有大量耗时的CPU计算时，建议回调函数内采用多进程或进程池来进行计算处理，以免阻塞消息驱动线程。
        tddict[trader.OnCmd()]()
        print(u"Get A New cmd\n");
        OrderRef2 = trader.InsertOrder('ag1706', QL_D_Buy, QL_OF_Open, QL_OPT_LimitPrice, 22450, 1)    
        #如果值为-999999999（初始值），则表示尚未获得数据
        '''
        print (u'(1)动态权益：%0.02f'%trader.QryBalance(True))
        print (u'(2)静态权益：%0.02f'%trader.QryBalance(False))      
        print (u'(3)可用资金：%0.02f'%trader.QryAvailable())
        print (u'(4)zn1701今日空单持仓：%d'%trader.QryPosition('rb1701',QL_POSITION_Sell_Today))   
        print (u'(5)zn1701今日多单持仓：%d'%trader.QryPosition('rb1701',QL_POSITION_Buy_Today))   
        print (u'(6)zn1701非今日空单持仓：%d'%trader.QryPosition('rb1701',QL_POSITION_Sell_History))   
        print (u'(7)zn1701非今日多单持仓：%d'%trader.QryPosition('rb1701',QL_POSITION_Buy_History))   
        print (u'(8)zn1701空单持仓总计：%d'%trader.QryPosition('rb1701',QL_POSITION_Sell_All))   
        print (u'(9)zn1701多单持仓总计：%d'%trader.QryPosition('rb1701',QL_POSITION_Buy_All))   
        '''
        #print '--------------------------------------------------------'
        #time.sleep(3)  #sleep1秒，防止死循环导致CPU占有率过高，1即可，不宜过大，若过大会导致程序进程长时间无响应，丢失行情数据

if __name__ == '__main__':
    main()
    

    
 
    
    
    