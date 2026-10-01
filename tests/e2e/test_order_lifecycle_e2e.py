
import pytest
import allure


@pytest.mark.e2e
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Order Lifecycle")
@allure.story("Create and Update Order")
@allure.description(
    "Verify the complete order lifecycle by creating an order, "
    "validating its initial database status, updating the status via API, "
    "and verifying the updated status in the database."
)
def test_order_lifecycle(api_client, db):

    # 1. CREATE
    with allure.step("Create order via API"):
        product = "MacBook"
        quantity = 1

        create_res = api_client.create_order(
            product=product,
            quantity=quantity
        )

        allure.attach(
            f"POST /orders\n\n"
            f"Request:\n"
            f"product: {product}\n"
            f"quantity: {quantity}\n\n"
            f"Response:\n"
            f"{create_res.text}",
            name="Create Order - Request and Response",
            attachment_type=allure.attachment_type.TEXT
        )

        assert create_res.status_code == 200

        order_id = create_res.json()["id"]

        allure.attach(
            str(order_id),
            name="Created Order ID",
            attachment_type=allure.attachment_type.TEXT
        )

    # 2. VERIFY DB
    with allure.step("Verify order status in database"):
        db_order = db.fetch_one(
            "SELECT status FROM orders WHERE id = %s",
            (order_id,)
        )

        allure.attach(
            str(db_order),
            name="Database Result - After Create",
            attachment_type=allure.attachment_type.TEXT
        )

        assert db_order[0] == "created"

    # 3. UPDATE
    with allure.step("Update order status via API"):
        update_res = api_client.update_order(
            order_id,
            status="shipped"
        )

        allure.attach(
            f"PUT /orders/{order_id}\n\n"
            f"Request:\n"
            f"status: shipped\n\n"
            f"Response:\n"
            f"{update_res.text}",
            name="Update Order - Request and Response",
            attachment_type=allure.attachment_type.TEXT
        )

        assert update_res.status_code == 200

    # 4. VERIFY DB UPDATE
    with allure.step("Verify updated order status in database"):
        updated = db.fetch_one(
            "SELECT status FROM orders WHERE id = %s",
            (order_id,)
        )

        allure.attach(
            str(updated),
            name="Database Result - After Update",
            attachment_type=allure.attachment_type.TEXT
        )

        assert updated[0] == "shipped"
