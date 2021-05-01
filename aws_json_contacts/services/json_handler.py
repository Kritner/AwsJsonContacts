import json

from aws_json_contacts.models.ContactInformation import ContactInformation
from aws_json_contacts.models.JsonParsedResult import JsonParsedResult


def get_json_from_string(candidate_json: str) -> JsonParsedResult:
    """
    Attempt to parse the candidate_json into a json object.
    If the loading fails return false, otherwise return true and the parsed object.

    :param candidate_json: the potential json string
    :return: JsonParsedResult
    """
    try:
        parsed_json = json.loads(candidate_json)
    except ValueError:
        return JsonParsedResult(False, None)

    return JsonParsedResult(True, parsed_json)


def get_contact_information_from_json(json_blob: dict) -> ContactInformation:
    """
    Attempts to get contact information from a json blob

    :param json_blob: The json blob to traverse
    :return: ContactInformation
    """

    return __traverse_json(json_blob, ContactInformation())


def __traverse_json(json_blob: dict, contact_information: ContactInformation) -> ContactInformation:
    """
    Traverses json, invoking itself recursively (if needed) in
    order to find specific contact information fields.
    Once traversal is completed, returns a constructed ContactInformation object.

    :param json_blob: The json blob to traverse
    :param contact_information: The working ContactInformation
    :return: ContactInformation
    """

    for key, value in json_blob.items():
        # if we encounter another dictionary within the json, invoke recursively
        if isinstance(value, dict):
            __traverse_json(value, contact_information)
            continue
        # if a list is found within the json, iterate through the list,
        # passing the object into the traversal recursively
        if isinstance(value, list):
            for v in value:
                __traverse_json(v, contact_information)
                continue

        # The actual fields we're looking for in the json
        if key == "first_name":
            contact_information.first_name = value
        if key == "middle_name":
            contact_information.middle_name = value
        if key == "last_name":
            contact_information.last_name = value
        if key == "zip_code":
            contact_information.zip_code = value

    return contact_information
