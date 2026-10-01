
import pytest
import allure


@pytest.mark.db
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Orders Database")
@allure.story("Order Persistence")
@allure.description("Verify that an order created through the API is correctly persisted in the database with the expected product and quantity.")
def test_order_exists_in_db(db, api_client):

    # 1. CREATE ORDER VIA API
    with allure.step("Create order via API"):
        product = "iPhone"
        quantity = 2

        response = api_client.create_order(
            product=product,
            quantity=quantity
        )

        allure.attach(
            f"POST /orders\n\n"
            f"Request:\n"
            f"product: {product}\n"
            f"quantity: {quantity}\n\n"
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

    # 2. QUERY DATABASE
    with allure.step("Query order from database"):
        result = db.fetch_one(
            "SELECT product, quantity FROM orders WHERE id = %s",
            (order_id,)
        )

        allure.attach(
            str(result),
            name="Database Query Result",
            attachment_type=allure.attachment_type.TEXT
        )

    # 3. VALIDATE DATABASE STATE
    with allure.step("Validate order data in database"):
        assert result is not None
        assert result[0] == product
        assert result[1] == quantity
