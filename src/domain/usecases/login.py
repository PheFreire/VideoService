from domain.models import UserConnectRequest
from domain.services import (
    Cursor,
    EmailNotVerifiedError,
    UserConnection,
    UserDosntExistsError,
    UserRepository,
)


class Login:
    def __init__(
        self,
        cursor: Cursor,
        user_connect_request: UserConnectRequest,
        user_repository: UserRepository,
        user_connection: UserConnection,
    ):
        self.cursor = cursor
        self.user_connect_request = user_connect_request
        self.user_repository = user_repository
        self.user_connection = user_connection

    def call(self):
        exists = self.user_repository.user_exists(
            self.cursor, self.user_connect_request
        )

        if exists:
            if self.user_repository.email_is_verified(
                self.cursor, self.user_connect_request
            ):
                user = self.user_repository.enter_account(
                    self.cursor, self.user_connect_request
                )
                self.user_connection(user)
            else:
                raise UserDosntExistsError()
        else:
            raise EmailNotVerifiedError()
