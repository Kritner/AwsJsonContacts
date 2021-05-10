import uuid
from datetime import datetime

from boto3 import client
import jsonpickle

from aws_json_contacts.models.ContactInformation import ContactInformation
from aws_json_contacts.services import environment_variable_provider


def upload_contact(contact_information: ContactInformation):
    """

    :param contact_information:
    :return:
    """

    key = datetime.now().strftime("%m/%d/%Y_%H%M%S") + '_' + str(uuid.uuid4()) + '.json'
    json_object_bytes = jsonpickle.encode(contact_information, unpicklable=False)

    s3 = client('s3')

    bucket_name = environment_variable_provider.get_environment_variable_or_default("bucket_name", "badvaluejustcheckingenvvarcomingthrough")

    return s3.put_object(Body=json_object_bytes,
                         Bucket=bucket_name,
                         Key=key)

