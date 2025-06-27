from src.backtester import Order, OrderBook
from typing import List

class Trader:
    '''
    state: 
    - state.timestamp: Int
    - state.order_depth: OrderBook
    current_position: Int
    '''
    def run(self, state, current_position):
        result = {} # stores your orders

        orders: List[Order] = [] # append Order objects to the list
        order_depth: OrderBook = state.order_depth # get orderbook (has sell and buy orders)
        '''if len(order_depth.sell_orders) != 0:
            best_ask, best_ask_amount = list(order_depth.sell_orders.items())[0] # assuming it is already sorted, you can sort it using sorted()
            if int(best_ask) < 10000:
                orders.append(Order("PRODUCT", 9998, 10)) # buy order

        if len(order_depth.buy_orders) != 0:
            best_bid, best_bid_amount = list(order_depth.buy_orders.items())[0]
            if int(best_bid) > 10000:
                orders.append(Order("PRODUCT", 10002, -10)) # sell order'''
        orders.append(Order("PRODUCT", 9998, 10))
        orders.append(Order("PRODUCT", 10002, -10))
        result["PRODUCT"] = orders
        return result