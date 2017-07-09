#导入CTP行情库
from CTPMarket import *
market = CTPMarket()   #行情接口类赋值给变量

# main()为程序入口函数，所有的行情、交易订阅、指标调用、下单的逻辑均写在此函数内执行
def main():
    #打印交易日    
    #print today
    #设置程序标题
    market.SetTitle(u"QucikLib CTP接口期货Tick数据采集器，保存csv格式 QQ群 5172183")
    #打印信息到控制台窗口
    print(u"官方QQ群 5172183 \n");
    
    #设置拒绝接收行情服务器数据的时间，有时候（特别是模拟盘）在早晨6-8点会发送前一天的行情数据，若不拒收的话，会导致历史数据错误，本方法最多可以设置4个时间段进行拒收数据
    #market.SetRejectdataTime(0.0400, 0.0840, 0.1530, 0.2030, NULL, NULL, NULL, NULL); 
    
    #从配置文件Instrument.ini  读取订阅的合约，每行写一个要订阅行情的合约，用调用ReadInstrument()的方式就无需通过调用Subcribe系列函数方式来订阅合约了，编译成exe后，也方便通过更改配置文件来更改合约
    market.ReadInstrumentIni()
    
    market.SaveTick(2)
    
    print ('number:',  market.InstrumentNum)
 
    #每次循环sleep休眠 10秒死循环导致CPU占有率过高,死循环，防止程序退出
    while(1):
        time.sleep(1000)

if __name__ == '__main__':
    main()
    

    
 
    
    
    