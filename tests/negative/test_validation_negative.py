
import pytest
import allure
from data.factories.order_factory import OrderFactory


@pytest.mark.negative
def test_empty_product_validation(api_client):

    # 1. BUILD INVALID TEST DATA
    with allure.step("Build order payload with empty product"):
        payload = OrderFactory.build(trait="empty_product")

        allure.attach(
            str(payload),
            name="Empty Product Payload",
            attachment_type=allure.attachment_type.TEXT
        )

    # 2. SEND REQUEST
    with allure.step("Send order request with empty product"):
        response = api_client.create_order(**payload)

        allure.attach(
            f"POST /orders\n\n"
            f"Request:\n"
            f"{payload}\n\n"
            f"Response Status: {response.status_code}\n\n"
            f"Response Body:\n"
            f"{response.text}",
            name="Empty Product - Request and Response",
            attachment_type=allure.attachment_type.TEXT
        )

    # 3. VALIDATE ERROR RESPONSE
    with allure.step("Validate that API rejects empty product"):
        assert response.status_code >= 400
