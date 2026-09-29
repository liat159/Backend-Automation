from faker import Faker
import random

fake = Faker()


class OrderFactory:

    @staticmethod
    def build(overrides: dict = None, trait: str = None):

        base = {
            "product": fake.word(),
            "quantity": random.randint(1, 10)
        }

        if trait == "empty_product":
            base["product"] = ""

        elif trait == "zero_quantity":
            base["quantity"] = 0

        elif trait == "large_quantity":
            base["quantity"] = 999

        elif trait == "invalid":
            return {
                "product": None,
                "quantity": "invalid"
            }

        if overrides:
            base.update(overrides)

        return base
