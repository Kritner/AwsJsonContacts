import json

import jsonpickle

from aws_json_contacts.services import json_handler, persistence_provider


def lambda_handler(event, context):
    """
    Lambda function processes json to determine if contact information is present.
    If present, add to s3.

    :param event:
    :param context:
    :return:
    """

    # Parse event json
    potential_json = json_handler.get_json_from_string(event['body'])

    # if not valid json, return 400
    if not potential_json.is_valid_json:
        return {
            "statusCode": 400,
            "body": "string provided in body not valid json.",
            "string_attempted": str(event['body'])
        }

    # check / get first_name, middle_name, last_name, zip_code from json
    contact_information = json_handler.get_contact_information_from_json(potential_json.json)

    # if none of the above fields exist return 400
    if not contact_information.is_valid_contact:
        return {
            "statusCode": 400,
            "body": 'None of the expected fields: "first_name", "middle_name", "last_name", or "zip_code" were '
                    'present in the json. '
        }

    # otherwise, insert into s3 bucket
    persistence_provider.upload_contact(contact_information)

    return {
        "statusCode": 200,
    }
