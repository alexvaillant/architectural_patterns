import pendulum
from typing import Optional, Set
from models.domain_models.order_lines_model import OrderLines

class Batch():

    def __init__(self, reference_id: str, sku: str, quantity: int, eta: Optional[pendulum.DateTime] = None):
        self.reference_id = reference_id
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = quantity
        self._allocated_orders = set() # type: Set[OrderLines]

    @property
    def allocated_quantity(self) -> int:
        return sum(order.quantity for order in self._allocated_orders)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, order: OrderLines) -> bool:
        if order.sku == self.sku and order.quantity <= self.available_quantity:
            return True
        return False

    def allocate(self, order: OrderLines):
        if self.can_allocate(order) is True and order.order_reference not in [order.order_reference for order in self._allocated_orders]:
            self._allocated_orders.add(order)

    def deallocate(self, order: OrderLines):
        if order.order_reference in [order.order_reference for order in self._allocated_orders]:
            self._allocated_orders.remove(order)