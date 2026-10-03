from unittest.mock import patch, Mock
import pytest
from app.main import can_access_google_page


@pytest.mark.parametrize("is_valid, has_internet, expected", [
    (True, True, "Accessible"),
    (True, False, "Not accessible"),
    (False, True, "Not accessible"),
    (False, False, "Not accessible"),
])
@patch('app.main.has_internet_connection')
@patch('app.main.valid_google_url')
def test_can_access_google_page(
    mock_valid_google_url: Mock,
    mock_has_internet_connection: Mock,
    is_valid: bool,
    has_internet: bool,
    expected: str,
) -> None:
    mock_valid_google_url.return_value = is_valid
    mock_has_internet_connection.return_value = has_internet


    assert (can_access_google_page
            ("[https://google.com](https://google.com)")
            == expected)
