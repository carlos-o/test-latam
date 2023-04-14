from index import PropertyInformation
from mock import patch
import pytest


class TestPropertyInformation:

    @pytest.fixture
    def property_instance(self):
        return PropertyInformation(189549429)

    @pytest.fixture
    def property_instance_2(self):
        return PropertyInformation(1895494293)

    @patch('builtins.print')
    def test_find_property_correctly(self, mock_print, property_instance):
        property_instance.find_property()
        mock_print.assert_called_with("U$S 850000")

    @patch('builtins.print')
    def test_find_property_not_found(self, mock_print, property_instance_2):
        with pytest.raises(SystemExit) as e:
            property_instance_2.find_property()
        mock_print.assert_called_with("Price not found for id 1895494293")

    @patch('builtins.print')
    @patch('index.requests.post')
    def test_exception_requests(self, mock_request, mock_print, property_instance_2):
        mock_request.side_effect = Exception("Connection error")
        with pytest.raises(SystemExit) as e:
            property_instance_2.find_property()
        mock_print.assert_called_with("An error has occurred please try again Connection error")

    @patch('builtins.print')
    @patch('index.requests.post')
    def test_request_status_code_not_200(self, mock_request, mock_print, property_instance_2):
        mock_request.return_value.status_code = 400
        with pytest.raises(SystemExit) as e:
            property_instance_2.find_property()
        mock_print.assert_called_with("Price not found for id 1895494293")

