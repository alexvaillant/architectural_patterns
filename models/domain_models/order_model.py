from typing import List

from models.domain_models.order_lines_model import OrderLines

class Order():

    def __init__(self, order_reference: str, order_lines_list: List[OrderLines]):
        self.order_reference = order_reference
        self.order_lines_list = order_lines_list