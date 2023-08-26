from dataclasses import dataclass

@dataclass(frozen=True)
class OrderLines:
    order_reference: str
    sku: str # sku := Stock-Keeping-Unit
    quantity: int