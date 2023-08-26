import pendulum
from typing import Optional
from models.domain_models.order_lines_model import OrderLines

class Batch():

    def __init__(self, reference_id: str, sku: str, quantity: int, eta: Optional[pendulum.DateTime] = None):
        self.reference_id = reference_id
        self.sku = sku
        self.available_quantity = quantity
        self.eta = eta

    def allocate(self, order: OrderLines):
        self.available_quantity -= order.quantity

    def can_allocate(self, order: OrderLines) -> bool:
        if order.sku == self.sku and order.quantity <= self.available_quantity:
            return True
        return False