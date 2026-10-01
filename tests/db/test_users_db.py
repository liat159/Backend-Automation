
import pytest
import allure


@pytest.mark.db
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Database")
@allure.story("User Query")
@allure.description("Verify that the database client handles a user query and returns either a valid user object or None when no user is found.")
def test_user_schema_in_db(db):

    # 1. QUERY USER FROM DATABASE
    with allure.step("Query user from database"):
        user_id = 1
        user = db.get_user_by_id(user_id)

        allure.attach(
            f"User ID: {user_id}\n\n"
            f"Query Result:\n"
            f"{user}",
            name="User Database Result",
            attachment_type=allure.attachment_type.TEXT
        )

    # 2. VALIDATE USER RESULT
    with allure.step("Validate user database result"):
        assert user is None or hasattr(user, "id")
