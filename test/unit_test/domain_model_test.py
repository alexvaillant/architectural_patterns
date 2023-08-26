import domain_model_helper as dm_helper
from models.domain_models.batch_model import Batch

def test_1_allocating_to_a_batch_reduces_the_available_quantity():
    batch, order_line = dm_helper.create_same_sku_batch_line('LARGE-TABLE', 20, 2)
    batch.allocate(order_line)

    assert batch.available_quantity == 18


def test_2_can_allocate_if_required_smaller_than_available():
    batch, order_line = dm_helper.create_same_sku_batch_line('LARGE-TABLE', 20, 2)
    assert batch.can_allocate(order_line)


def test_3_can_allocate_if_available_equal_required():
    batch, order_line = dm_helper.create_same_sku_batch_line('LARGE-TABLE', 2, 2)
    assert batch.can_allocate(order_line)


def test_4_cannot_allocate_if_available_smaller_than_required():
    batch, order_line = dm_helper.create_same_sku_batch_line('LARGE-TABLE', 2, 20)
    assert not batch.can_allocate(order_line)


def test_5_cannot_allocate_if_sku_different():
    batch, order_line = dm_helper.create_different_sku_batch_line('LARGE-TABLE', 'RED-CHAIR', 20, 2)
    assert not batch.can_allocate(order_line)