from domain.models.user_connect_request import User


class UserConnection:
    def call(self, user: User):
        raise NotImplementedError
