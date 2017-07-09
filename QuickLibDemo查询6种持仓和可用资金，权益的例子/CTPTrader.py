# -*- coding=utf-8 -*-
from ctypes import *
from CTPTraderType import *
import time


class CTPTrader(object):
	def __init__(self):

		self.d2 = CDLL('QuickLibTD.dll')

		self.fLogin = self.d2.Login
		self.fLogin.argtypes = []
		self.fLogin.restype = c_int32
		
		self.fInsertOrder = self.d2.InsertOrder
		self.fInsertOrder.argtypes = [c_char_p, c_char, c_char,c_char, c_double, c_int32]
		self.fInsertOrder.restype = c_int32

		self.fInsertOrderByRate = self.d2.InsertOrderByRate
		self.fInsertOrderByRate.argtypes = [c_char_p, c_char, c_char,c_char, c_double, c_double,c_int32,c_int32]
		self.fInsertOrderByRate.restype = c_int32

		self.fDeleteOrder = self.d2.DeleteOrder
		self.fDeleteOrder.argtypes = [c_char_p, c_int32]
		self.fDeleteOrder.restype = c_int32

		self.fQryTradedVol = self.d2.QryTradedVol
		self.fQryTradedVol.argtypes = [c_int32]
		self.fQryTradedVol.restype = c_int32
		
		self.fQryPosition = self.d2.QryPosition
		self.fQryPosition.argtypes = [c_char_p,c_int32]
		self.fQryPosition.restype = c_int32		
		
		self.fQryPositionList = self.d2.QryPositionList
		self.fQryPositionList.argtypes = [c_int32]
		self.fQryPositionList.restype = c_void_p
		
		self.fQryBalance = self.d2.QryBalance
		self.fQryBalance.argtypes = [c_bool]
		self.fQryBalance.restype = c_double	
		
		self.fQryAvailable = self.d2.QryAvailable
		self.fQryAvailable.argtypes = []
		self.fQryAvailable.restype = c_double
		
		self.fSetShowPosition = self.d2.SetShowPosition
		self.fSetShowPosition.argtypes = [c_bool]
		self.fSetShowPosition.restype = c_void_p	
		
		self.fQryExchangeMarginRate = self.d2.QryExchangeMarginRate
		self.fQryExchangeMarginRate.argtypes = [c_char_p,c_int32]
		self.fQryExchangeMarginRate.restype = c_double		
		
		self.fQryUnderlyingMultiple = self.d2.QryUnderlyingMultiple
		self.fQryUnderlyingMultiple.argtypes = [c_char_p]
		self.fQryUnderlyingMultiple.restype = c_double		
		
		self.fQryQueryMaxOrderVolume = self.d2.QryQueryMaxOrderVolume
		self.fQryQueryMaxOrderVolume.argtypes = [c_char_p,c_char_p,c_char_p,c_char,c_char,c_char,c_int32]
		self.fQryQueryMaxOrderVolume.restype = c_int32				
			
		self.fOnCmd = self.d2.OnCmd
		self.fOnCmd.argtypes = []
		self.fOnCmd.restype = c_int32
	
		self.fGetCmd = self.d2.GetCmd
		self.fGetCmd.argtypes = []
		self.fGetCmd.restype = c_int32
	
		self.fGetCmdContent = self.d2.GetCmdContent
		self.fGetCmdContent.argtypes = []
		self.fGetCmdContent.restype = c_char_p
		
		
		self.fGetCmdContent_Order = self.d2.GetCmdContent_Order
		self.fGetCmdContent_Order.argtypes = []
		self.fGetCmdContent_Order.restype = c_void_p
		
		self.fGetCmdContent_Settlement = self.d2.GetCmdContent_Settlement
		self.fGetCmdContent_Settlement.argtypes = []
		self.fGetCmdContent_Settlement.restype = c_void_p	
		
		self.fGetCmdContent_Error = self.d2.GetCmdContent_Error
		self.fGetCmdContent_Error.argtypes = []
		self.fGetCmdContent_Error.restype = c_void_p			
		
		#self.fGetCmdContent_Error = self.d2.GetCmdContent_Error
		#self.fGetCmdContent_Error.argtypes = []
		#self.fGetCmdContent_Error.restype = c_void_p			
		
		self.fGetCmdContent_LoginScuess = self.d2.GetCmdContent_LoginScuess
		self.fGetCmdContent_LoginScuess.argtypes = []		
		self.fGetCmdContent_LoginScuess.restype = c_int32	
		
		self.fGetCmdContent_Connected = self.d2.GetCmdContent_Connected
		self.fGetCmdContent_Connected.argtypes = []		
		self.fGetCmdContent_Connected.restype = c_int32
		
		self.fGetCmdContent_ProductGroupMargin = self.d2.GetCmdContent_ProductGroupMargin
		self.fGetCmdContent_ProductGroupMargin.argtypes = []	
		self.fGetCmdContent_ProductGroupMargin.restype = c_int32
		
		self.fGetCmdContent_CommissionRate = self.d2.GetCmdContent_CommissionRate
		self.fGetCmdContent_CommissionRate.argtypes = []		
		self.fGetCmdContent_CommissionRate.restype = c_int32				
		
	def Login(self):
		return self.fLogin()

	def InsertOrder(self, instrumentID, direction, offsetFlag, priceType, price, num):
		return self.fInsertOrder(instrumentID, direction, offsetFlag, priceType,
								 c_double(price), c_int32(num))
	
	#根据资金比例下单
	def InsertOrderByRate(self, instrumentID, direction, offsetFlag, priceType, price, rate, BalanceType, multiplier):
		return self.fInsertOrderByRate(instrumentID, direction, offsetFlag, priceType,
								 c_double(price), rate, BalanceType, multiplier)


	def DeleteOrder(self, instrumentID, orderRef):
		return self.fDeleteOrder(instrumentID, orderRef)

	def QryTradedVol(self, orderRef):
		return self.fQryTradedVol(orderRef)
	
	#查询品种持仓
	def QryPosition(self, instrumentID,positiontype):
		return self.fQryPosition(instrumentID,positiontype)
	
	#查询持仓列表
	def QryPositionList(self, orderRef):
		return self.fQryPositionList(orderRef)


        #查询权益   BalanceType=True动态权益    BalanceType=False静态权益
	def QryBalance(self, BalanceType):
		return self.fQryBalance(BalanceType)
	
	#查询可用资金
	def QryAvailable(self):
		return self.fQryAvailable()
			
	#设置更新持仓数据时显示,仅对控制台有效
	def SetShowPosition(self,showstate):
		self.fSetShowPosition(showstate)
		
 
	#查询保证金比例
	def QryExchangeMarginRate(self,Instrument,Type):
		return self.fQryExchangeMarginRate(Instrument,Type)
	
	#查询合约乘数
	def QryUnderlyingMultiple(self,Instrument):
		return self.fQryUnderlyingMultiple(Instrument)
	
	#查询
	def QryQueryMaxOrderVolume(self,BrokerID,InvestorID,Instrument,Direction,OffsetFlag,HedgeFlag,MaxVolume):
		return self.fQryQueryMaxOrderVolume(BrokerID,InvestorID,Instrument,Direction,OffsetFlag,HedgeFlag,MaxVolume)	
	
	def OnCmd(self):
		return self.fOnCmd()

	def GetCmd(self):
		return (self.fGetCmd(),self.fGetCmdContent()) 	

	def GetUnGetCmdSize(self):
		return self.fGetUnGetCmdSize()	
	
	def GetCmdContent_Order(self):
		#订单回报回调
		return self.fGetCmdContent_Order()
		
	def GetCmdContent_Settlement(self):
		#结算单确认回调
		return self.fGetCmdContent_Settlement()
	
	def GetCmdContent_Error(self):
		#错误信息回调
		return self.fGetCmdContent_Error()
	
	def GetCmdContent_LoginScuess(self):
		#登录回调
		return self.fGetCmdContent_LoginScuess()
	
	def GetCmdContent_Connected(self):
		#连接成功回调
		return self.fGetCmdContent_Connected()
	
	def GetCmdContent_ProductGroupMargin(self):
		#请求查询合约保证金率响应回调
		return self.fGetCmdContent_ProductGroupMargin()	
	
	def GetCmdContent_CommissionRate(self):
		#请求查询合约手续费率响应回调
		return self.fGetCmdContent_CommissionRate()		
	
	