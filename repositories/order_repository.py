from sqlalchemy import text
from database import engine


class OrderRepository:

    def __init__(self):
        self.engine = engine

    def get_order_by_id(self, order_id: int):

        query = text("SELECT * FROM orders WHERE id = :id")

        with self.engine.connect() as conn:
            result = conn.execute(query, {"id": order_id})
            row = result.fetchone()

            return row

    def clear_orders(self):
        pass
