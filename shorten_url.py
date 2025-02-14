import boto3
import json
import hashlib

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('URLShortener')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    original_url = body.get('url')

    if not original_url:
        return {
            'statusCode': 400,
            'body': json.dumps({"error": "Missing 'url' parameter"})
        }
    
    short_code = hashlib.md5(original_url.encode()).hexdigest()[:6]

    table.put_item(Item={'short_code': short_code, 'original_url': original_url})

    return {
        'statusCode': 200,
        'body': json.dumps({"short_url": f"https://example.com/{short_code}"}) ###TODO: Replace with your domain
    }