
class OrderLines():

    def __init__(self, order_refernce: str, sku: str, quantity: int) -> None:
        self.order_reference = order_refernce
        self.sku = sku # sku := Stock-Keeping-Unit
        self.quantity = quantity