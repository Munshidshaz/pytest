import pytest
from service import APIClient, UserService

def test_get_username_with_mock(mocker):
    mock_api_client = mocker.Mock(spec=APIClient)

    mock_api_client.get_user_data.return_value = {"user_id":1, "name":"Alice"}

    service = UserService(mock_api_client)
    result = service.get_username(1)

    assert result== "ALICE"
    mock_api_client.get_user_data.assert_called_once_with(1)





