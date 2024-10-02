import pytest
from user_credential import *


@pytest.mark.parametrize("username, password", [('user1', 'Admin@123'),
                                                ('user2', 'Admin@123'),
                                                ('user3', 'Admin@1234'),
                                                ('user4', 'user@123'),
                                                ('user5', 'root@123'), ])
def test_login(username, password):
    print("username :", username)
    print("password :", password)


@pytest.mark.parametrize("username, password", user_credential)
def test_login_with_external_data(username, password):
    print("\n username :", username)
    print("\n password :", password)
