import pytest
import allure
from data.factories.order_factory import OrderFactory


@pytest.mark.e2e
@pytest.mark.smoke
@pytest.mark.regression
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Order Lifecycle")
@allure.story("Create Order")
@allure.description("Verify that an order can be created via the API and that the created order is correctly persisted in the database.")
def test_create_order_flow(api_client, db):

    # 1. BUILD TEST DATA
    with allure.step("Build order test data"):
        payload = OrderFactory.build()

        allure.attach(
            str(payload),
            name="Order Payload",
            attachment_type=allure.attachment_type.TEXT
        )

    # 2. CREATE ORDER
    with allure.step("Create order via API"):
        response = api_client.create_order(**payload)

        allure.attach(
            f"POST /orders\n\n"
            f"Request:\n"
            f"{payload}\n\n"
            f"Response:\n"
            f"{response.text}",
            name="Create Order - Request and Response",
            attachment_type=allure.attachment_type.TEXT
        )

        assert response.status_code == 200

        order_id = response.json()["id"]

        allure.attach(
            str(order_id),
            name="Created Order ID",
            attachment_type=allure.attachment_type.TEXT
        )

    # 3. VERIFY DATABASE
    with allure.step("Verify order in database"):
        db_order = db.get_order_by_id(order_id)

        allure.attach(
            f"id: {db_order.id if db_order else None}\n"
            f"product: {db_order.product if db_order else None}\n"
            f"quantity: {db_order.quantity if db_order else None}\n"
            f"status: {db_order.status if db_order else None}",
            name="Database Order",
            attachment_type=allure.attachment_type.TEXT
        )

        assert db_order is not None
        assert db_order.product == payload["product"]
        assert db_order.quantity == payload["quantity"]
