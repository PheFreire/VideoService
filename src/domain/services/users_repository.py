from domain.models import User, UserConnectRequest, UserRegister
from domain.services.cursor import Cursor


class UserRepository:
    def user_exists(
        self, cursor: Cursor, user_connect_request: UserConnectRequest
    ) -> bool:
        raise NotImplementedError

    def email_is_verified(
        self, cursor: Cursor, user_connect_request: UserConnectRequest
    ) -> bool:
        raise NotImplementedError

    def enter_account(
        self, cursor: Cursor, user_connect_request: UserConnectRequest
    ) -> User:
        raise NotImplementedError

    def create_account(
        self, cursor: Cursor, user_connect_request: UserRegister
    ) -> User:
        raise NotImplementedError


class UserDosntExistsError(Exception):
    pass


class EmailNotVerifiedError(Exception):
    pass
