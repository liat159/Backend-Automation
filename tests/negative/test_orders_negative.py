
import pytest
import allure
from data.factories.order_factory import OrderFactory


@pytest.mark.negative
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Orders API")
@allure.story("Invalid Order Payload")
@allure.description("Verify that the Orders API rejects an invalid order payload with an appropriate HTTP error response.")
def test_invalid_order_payload(api_client):

    # 1. BUILD INVALID TEST DATA
    with allure.step("Build invalid order payload"):
        payload = OrderFactory.build(trait="invalid")

        allure.attach(
            str(payload),
            name="Invalid Order Payload",
            attachment_type=allure.attachment_type.TEXT
        )

    # 2. SEND INVALID REQUEST
    with allure.step("Send invalid order request via API"):
        response = api_client.create_order(**payload)

        allure.attach(
            f"POST /orders\n\n"
            f"Request:\n"
            f"{payload}\n\n"
            f"Response Status: {response.status_code}\n\n"
            f"Response Body:\n"
            f"{response.text}",
            name="Invalid Order - Request and Response",
            attachment_type=allure.attachment_type.TEXT
        )

    # 3. VALIDATE ERROR RESPONSE
    with allure.step("Validate that API rejects invalid payload"):
        assert response.status_code >= 400
