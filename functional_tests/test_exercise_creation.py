import pytest


@pytest.mark.functest
def test_can_create_an_exercise(live_server, selenium):
    # Bill goes to the home page of his training app
    selenium.get(str(live_server))

    assert "Training Station" in selenium.title

    # Write rest of the test!
    assert False
