import pytest
from rest_framework.test import APIClient
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from django.contrib.auth.models import Group

options = webdriver.FirefoxOptions()
options.headless = True


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture
def authenticated_user(client, django_user_model):
    email = "test@test.com"
    password = "password"
    user = django_user_model.objects.create(email=email, password=password)
    client.force_login(user)
    return user


@pytest.fixture
def authenticated_trainer(client, django_user_model):
    email = "test@test.com"
    password = "password"
    user = django_user_model.objects.create(email=email, password=password)
    trainer_group = Group.objects.get(name="Trainer")
    trainer_group.user_set.add(user)
    client.force_login(user)
    return user


@pytest.fixture
def browser():
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def driver_factory(request, driver_class, driver_kwargs):
    """
    Returns a factory function that returns a WebDriver instance when called,
    based on options and capabilities
    """
    request.node.drivers = []

    def factory():
        driver = driver_class(**driver_kwargs)
        request.node.drivers.append(driver)

        event_listener = request.config.getoption("event_listener")
        if event_listener is not None:
            # Import the specified event listener and wrap the driver instance
            mod_name, class_name = event_listener.rsplit(".", 1)
            mod = __import__(mod_name, fromlist=[class_name])
            event_listener = getattr(mod, class_name)
            if not isinstance(driver, EventFiringWebDriver):
                driver = EventFiringWebDriver(driver, event_listener())

        return driver

    yield factory

    for driver in request.node.drivers:
        driver.quit()


@pytest.fixture
def driver(driver_factory):
    return driver_factory()


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture
def chrome_options(chrome_options, pytestconfig):
    chrome_options.add_argument("--headless")
    return chrome_options


@pytest.fixture
def firefox_options(firefox_options, pytestconfig):
    firefox_options.set_headless(True)
    return firefox_options
