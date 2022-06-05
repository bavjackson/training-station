from selenium.webdriver.common.keys import Keys
import pytest
import time


TRAINER_EMAIL = "trainer@test.com"
TRAINER_PASSWORD = "trainerPassword1234!@#$"


@pytest.mark.functest
def test_trainer_can_create_an_exercise(
    live_server, django_user_model, django_db_serialized_rollback, selenium
):
    # Bill goes to the home page of his training app
    selenium.get(f"{live_server.url}/users/login")
    selenium.set_window_size(1920, 1080)

    trainer_user = django_user_model.objects.create_user(
        email=TRAINER_EMAIL, password=TRAINER_PASSWORD, is_trainer=True
    )

    assert "Login" in selenium.title

    email_input = selenium.find_element_by_id("id_username")
    password_input = selenium.find_element_by_id("id_password")

    email_input.send_keys(TRAINER_EMAIL)
    password_input.send_keys(TRAINER_PASSWORD)
    password_input.send_keys(Keys.ENTER)

    time.sleep(1)

    assert "Training Station" in selenium.title

    selenium.find_element_by_id("id_exercises_link").click()
    time.sleep(1)

    assert "Exercises" in selenium.title

    exercise_name = "Pullup"

    exercise_name_input = selenium.find_element_by_id("id_exercise_name")
    exercise_name_input.send_keys(exercise_name)
    exercise_name_input.send_keys(Keys.ENTER)

    time.sleep(1)

    exercise_list = selenium.find_element_by_id("id_exercises_list")

    list_items = exercise_list.find_elements_by_tag_name("li")

    assert exercise_name in [item.text for item in list_items]
