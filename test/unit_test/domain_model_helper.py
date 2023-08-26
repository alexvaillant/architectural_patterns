from models.domain_models.batch_model import Batch
from models.domain_models.order_lines_model import OrderLines

def create_same_sku_batch_line(sku: str, batch_quantity: int, line_quantity: int):
    batch = Batch(reference_id='reference_id', sku=sku, quantity=batch_quantity)
    order_line = OrderLines('order_reference', sku, line_quantity)

    return batch, order_line


def create_different_sku_batch_line(batch_sku: str, line_sku: str, batch_quantity: int, line_quantity: int):
    batch = Batch(reference_id='reference_id', sku=batch_sku, quantity=batch_quantity)
    order_line = OrderLines('order_reference', line_sku, line_quantity)

    return batch, order_line