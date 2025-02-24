import boto3
import json
import hashlib

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('URLShortener')

def lambda_handler(event, context):
    short_code = event['pathParameters']['shortCode']
    response = table.get_item(Key = {'short_code': short_code})

    if 'Item' not in response:
        return {
            'statusCode': 404,
            'body': json.dumps({"error": "Short URL not found"})
        }
    
    return {
        'statusCode': 301,
        'headers': {
            'Location': response['Item']['original_url']
        },
        'body': ''
    }