from abc import ABC
from dataclasses import dataclass
from typing import Type

from webify import Managed
from webify.db.types import Password


@dataclass
class BaseUser(Managed, ABC):
    username: str
    password: Password


def create_auth(user_class: Type[BaseUser]):  # TODO
    def log_in(username: str, password: Password) -> None:
        user = user_class.get_instance_by_id(username)
        assert user.password == password
        get_context().user = user

    def sign_up(username: str, password: Password, confirm_password: Password) -> None:
        try:
            user = user_class.get_instance_by_id(username)
        except Exception:
            pass
        else:
            assert user is None

        assert password == confirm_password

        user = user_class(username, password)
        user_class.register(user)
        get_context().user = user

    return log_in, sign_up
