
import pytest
import allure


@pytest.mark.smoke
def test_health_smoke(api_client):

    # 1. HEALTH CHECK
    with allure.step("Verify application health"):
        response = api_client.get("/health")

        allure.attach(
            f"GET /health\n\n"
            f"Response Status: {response.status_code}\n\n"
            f"Response Body:\n"
            f"{response.text}",
            name="Health Smoke - Response",
            attachment_type=allure.attachment_type.TEXT
        )

        assert response.json()["status"] == "ok"
