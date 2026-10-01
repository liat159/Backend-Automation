
import pytest
import allure


@pytest.mark.api
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("Health API")
@allure.story("Health Check")
@allure.description("Verify that the API health endpoint is available and returns a healthy status.")
def test_health_endpoint(api_client):

    # 1. HEALTH CHECK
    with allure.step("Send health check request"):
        response = api_client.get("/health")

        allure.attach(
            f"GET /health\n\n"
            f"Response:\n"
            f"{response.text}",
            name="Health Check - Response",
            attachment_type=allure.attachment_type.TEXT
        )

    # 2. VALIDATE RESPONSE
    with allure.step("Validate health check response"):
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
