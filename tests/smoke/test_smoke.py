
import pytest
import allure


@pytest.mark.smoke
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature("System Health")
@allure.story("System Availability")
@allure.description("Verify that the application is available and the health endpoint returns HTTP 200.")
def test_basic_system_alive(api_client):

    # 1. VERIFY SYSTEM IS ALIVE
    with allure.step("Verify system is alive"):
        response = api_client.get("/health")

        allure.attach(
            f"GET /health\n\n"
            f"Response Status: {response.status_code}\n\n"
            f"Response Body:\n"
            f"{response.text}",
            name="System Health - Response",
            attachment_type=allure.attachment_type.TEXT
        )

        assert response.status_code == 200
