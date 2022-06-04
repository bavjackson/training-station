import pytest

USER_EMAIL = 'test@example.com'
USER_PASSWORD = 'foo'

def test_create_user(django_user_model):
    user = django_user_model.objects.create_user(email=USER_EMAIL, password=USER_PASSWORD)

    assert user.email == USER_EMAIL
    assert user.is_active == True
    assert user.is_staff == False
    assert user.is_superuser == False
    assert not hasattr(user, 'username')

def test_creating_user_with_no_args_raises_error(django_user_model):
    with pytest.raises(Exception) as e_info:
        user = django_user_model.objects.create_user()

def test_creating_user_with_empty_email_and_no_password_raises_error(django_user_model):
    with pytest.raises(Exception) as e_info:
        user = django_user_model.objects.create_user(email='')

def test_creating_user_with_empty_email_raises_error(django_user_model):
    with pytest.raises(Exception) as e_info:
        user = django_user_model.objects.create_user(email='', password="foo")

def test_create_superuser(django_user_model):
    user = django_user_model.objects.create_superuser(email=USER_EMAIL, password=USER_PASSWORD)

    assert user.email == USER_EMAIL
    assert user.is_active == True
    assert user.is_staff == True
    assert user.is_superuser == True
    assert not hasattr(user, 'username')
    