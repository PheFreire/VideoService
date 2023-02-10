from unittest.mock import Mock

import pytest

from domain.models import UserConnectRequest
from domain.usecases import Login
from domain.services import UserConnection, User, UserRepository

# Verify if user exists
# Verify if email is valid
# Verify enter account
# Verify connect User


@pytest.fixture()
def user_connect_request():
    return Mock(spec=UserConnectRequest)


@pytest.fixture()
def user_repository():
    return Mock(spec=UserRepository)


@pytest.fixture()
def user_connection():
    return Mock(spec=UserConnection)


def test_should_(user_connect_request: UserConnectRequest, users_repository: UserRepository, user_connection: UserConnection):
    login_usecase = Login(
        user_connect_request,
        user_connection,
        users_repository
    )

    login_usecase.call()
    user_repository.user_exists.assert_called_once_with(user_connect_request)
    

    
