
import pytest
import allure


@pytest.mark.api
@pytest.mark.regression
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Orders API")
@allure.story("Create Order")
@allure.description("Verify that a valid order can be created successfully via the API.")
def test_create_order_api(api_client):

    # 1. CREATE ORDER
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

    # 2. VALIDATE RESPONSE
    with allure.step("Validate order response"):
        data = response.json()

        allure.attach(
            str(data),
            name="Parsed Response",
            attachment_type=allure.attachment_type.TEXT
        )

        assert "id" in data
        assert data["product"] == product
        assert data["quantity"] == quantity
