
import pytest
import allure


@pytest.mark.api
def test_get_customers_list(api_client):

    # 1. GET CUSTOMERS
    with allure.step("Get customers list via API"):
        response = api_client.get("/customers")

        allure.attach(
            f"GET /customers\n\n"
            f"Response Status: {response.status_code}\n\n"
            f"Response Body:\n"
            f"{response.text}",
            name="Get Customers - Response",
            attachment_type=allure.attachment_type.TEXT
        )

    # 2. VALIDATE RESPONSE
    with allure.step("Validate customers API response"):
        assert response.status_code in [200, 404]
