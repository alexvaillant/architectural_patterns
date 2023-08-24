from models.domain_models.batch_model import Batch
from models.domain_models.order_lines_model import OrderLines

def test_1_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch(reference_id='reference_id', sku='SMALL-TABLE', quantity=20)
    order_line = OrderLines(order_refernce='order_reference', sku="SMALL-TABLE", quantity=2)

    batch.allocate(order_line)

    assert batch.available_quantity == 18