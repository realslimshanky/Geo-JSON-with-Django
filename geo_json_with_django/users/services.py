# Third Party Stuff
from django.contrib.auth import get_user_model, authenticate

# Geo JSON with Django Stuff
from geo_json_with_django.base import exceptions as exc


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise exc.WrongArguments("Invalid username/password. Please try again!")

    return user


def create_user_account(email, password, name, phone_number, language, currency):
    user = get_user_model().objects.create_user(
        email=email, password=password, name=name, phone_number=phone_number, language=language, currency=currency
    )
    return user


def get_user_by_email(email: str):
    return get_user_model().objects.filter(email__iexact=email).first()
