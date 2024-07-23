
'''
Best Practices

Error Handling for Event Structure: Added a check to ensure the event contains the necessary "Records" information and is not empty. Returns a 400 status code if the structure is invalid.
Try-Except Block for Key Extraction: Wrapped the bucket name and file name extraction in a try-except block to handle cases where the expected keys might be missing. Returns a 400 status code with a descriptive error message if a KeyError occurs.
Formatted Print Statement: Updated the print statement to use f-string for better readability.
Error Handling for Glue Job Start: Wrapped the call to glue.start_job_run in a try-except block to handle any exceptions that might occur when starting the Glue job. Returns a 500 status code with a descriptive error message if an exception occurs.
Comments: Added detailed comments to explain each step and the purpose of the code blocks.
'''

import json
import boto3

def lambda_handler(event, context):
    # Check if the event contains S3 bucket and object information
    if "Records" not in event or len(event["Records"]) == 0:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid event structure')
        }
    
    # Extract the bucket name and file name from the event object passed to the Lambda function
    try:
        record = event["Records"][0]
        bucket_name = record["s3"]["bucket"]["name"]
        file_name = record["s3"]["object"]["key"]
    except KeyError as e:
        # Handle the case where expected keys are missing
        return {
            'statusCode': 400,
            'body': json.dumps(f'Missing key in event data: {e}')
        }

    print(f"Bucket: {bucket_name}, File: {file_name}")

    # Initialize a Glue client using the boto3 library
    glue = boto3.client('glue')

    try:
        # Start a Glue job run with the specified job name and arguments
        response = glue.start_job_run(
            JobName='glueCDC-pyspark',
            Arguments={
                '--s3_target_path_key': file_name,  # Pass the file name as an argument to the Glue job
                '--s3_target_path_bucket': bucket_name  # Pass the bucket name as an argument to the Glue job
            }
        )
        # Return a successful response with a status code of 200 and a message
        return {
            'statusCode': 200,
            'body': json.dumps('Glue job started successfully!')
        }
    except Exception as e:
        # Handle any errors that occur when starting the Glue job
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error starting Glue job: {e}')
        }
