import pytest

from aws_json_contacts.services import json_handler


@pytest.mark.parametrize(('candidate_json', 'is_expected_json'), [
    ('{"test": 5}', True),
    ("qwerty", False),
    ("{qwerty}", False)
])
def test_should_get_json_from_string(candidate_json: str, is_expected_json: bool):
    result = json_handler.get_json_from_string(candidate_json)
    assert is_expected_json == result.is_valid_json


@pytest.mark.parametrize(('candidate_json', 'expected_valid_contact_information', 'expected_first_name',
                         'expected_middle_name', 'expected_last_name', 'expected_zip_code'), [
    ('{}', False, None, None, None, None),
    ('{"first_name": "Russ",	"middle_name": "Lloyd",	"last_name": "Hammett",	"zip_code": "21158"}', True, "Russ", "Lloyd", "Hammett", "21158"),
    ('{"middle_name": "Lloyd",	"last_name": "Hammett",	"zip_code": "21158"}', True, None, "Lloyd", "Hammett", "21158"),
    ('{"first_name": "Russ",	"last_name": "Hammett",	"zip_code": "21158"}', True, "Russ", None, "Hammett", "21158"),
    ('{"first_name": "Russ",	"middle_name": "Lloyd",	"zip_code": "21158"}', True, "Russ", "Lloyd", None, "21158"),
    ('{"first_name": "Russ",	"middle_name": "Lloyd",	"last_name": "Hammett"}', True, "Russ", "Lloyd", "Hammett", None),
    ('{"someProperty": "hello world"}', False, None, None, None, None),
    ('{"first_name": "Russ","last_name": "Hammett","zip_code": "21158",' +
     '"someNestedObject": {"andAnother": [{"middle_name": "first"},{"middle_name": "second"}]}}',
     True, "Russ", "first", "Hammett", "21158")
])
def test_should_get_contact_information_from_json(candidate_json: str, expected_valid_contact_information: bool,
                                                  expected_first_name: str, expected_middle_name: str,
                                                  expected_last_name: str, expected_zip_code: str):
    potential_contact = json_handler.get_json_from_string(candidate_json)
    contact = json_handler.get_contact_information_from_json(potential_contact.json)

    assert expected_valid_contact_information == contact.is_valid_contact
    assert expected_first_name == contact.first_name
    assert expected_middle_name == contact.middle_name
    assert expected_last_name == contact.last_name
    assert expected_zip_code == contact.zip_code
