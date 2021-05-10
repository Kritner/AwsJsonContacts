FROM public.ecr.aws/lambda/python:3.7

COPY . ./aws_json_contacts/

WORKDIR aws_json_contacts

RUN python3.7 -m pip install -r requirements.txt

RUN python3.7 -m pip list

# Command can be overwritten by providing a different command in the template directly.
CMD ["aws_json_contacts/app.lambda_handler"]