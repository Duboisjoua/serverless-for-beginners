import boto3

client = boto3.client('lambda')

def lambda_handler(event, context):
    response = client.list_functions()
    return response
