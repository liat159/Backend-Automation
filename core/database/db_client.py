import psycopg2
from config.settings import settings


class DBClient:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=settings.db_host,
            dbname=settings.db_name,
            user=settings.db_user,
            password=settings.db_password,
            port=settings.db_port,
        )
        self.cursor = self.conn.cursor()

    def fetch_one(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetch_all(self, query, params=None):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def execute(self, query, params=None):
        self.cursor.execute(query, params)
        self.conn.commit()

    def get_order_by_id(self, order_id):
        query = """
            SELECT id, product, quantity, status
            FROM orders
            WHERE id = %s
        """
        row = self.fetch_one(query, (order_id,))

        if row is None:
            return None

        class OrderRecord:
            def __init__(self, row):
                self.id = row[0]
                self.product = row[1]
                self.quantity = row[2]
                self.status = row[3]

        return OrderRecord(row)

    def clear_orders(self):
        self.execute("DELETE FROM orders")

    def get_user_by_id(self, user_id):
        return None

    def close(self):
        self.cursor.close()
        self.conn.close()
