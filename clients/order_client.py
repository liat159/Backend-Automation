from core.api.base_client import BaseClient


class OrderClient(BaseClient):

    def create_order(self, product: str, quantity: int):
        payload = {
            "product": product,
            "quantity": quantity
        }

        return self.post("/orders", json=payload)

    def get_order(self, order_id: int):
        return self.get(f"/orders/{order_id}")

    def update_order(self, order_id: int, status: str):
        payload = {
            "status": status
        }

        return self.put(f"/orders/{order_id}", json=payload)

    def delete_order(self, order_id: int):
        return self.delete(f"/orders/{order_id}")
