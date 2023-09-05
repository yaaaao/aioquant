# -*- coding:utf-8 -*-

# 策略实现

from aioquant import const
from aioquant.utils import logger
from aioquant.configure import config
from aioquant.market import Market
from aioquant.trade import Trade
from aioquant.const import BINANCE
from aioquant.order import Order
from aioquant.market import Orderbook
from aioquant.order import ORDER_ACTION_BUY, ORDER_STATUS_FAILED, ORDER_STATUS_CANCELED, ORDER_STATUS_FILLED

class MyStrategy:

    def __init__(self):
        """ 初始化
        """
        self.strategy = "my_strategy"
        self.platform = BINANCE
        self.symbol = config.symbol

        # 订阅行情
        Market(const.MARKET_TYPE_ORDERBOOK, BINANCE, self.symbol, self.on_event_orderbook_view)

    async def on_event_orderbook_view(self, orderbook: Orderbook):
        """ 订单状态更新
        """
        logger.info("order update:", Orderbook, caller=self)
