## Serverless with AWS and Google Cloud

This project allows you to deploy python 3.6 serverless code to AWS Lambda and have it call upon Google Cloud APIs, such as Google Speech-To-Text used here. 

This python script takes in an audio file (.flac) stored in an AWS S3 bucket and sends it to Google Cloud's Speech-To-Text to receive a JSON response with the written words. It returns a JSON response in Lambda that contains the words in the audio file.

sample.json contains an example of the JSON response from Google Cloud's Speech-To-Text API.

### Pre-requisites:
1. Sign up for your own Google Cloud account and download access credentials as "google_service_key.json"
2. Sign up for your own AWS account and setup AWS Lambda for Python 3.6 and AWS S3
3. Setup your environment with virtualenv
4. Install all 3rd party dependencies by running the command:
  ```console
    pip install requirements.txt
  ```

### Deployment
1. Build and package all python dependencies (including Google Cloud API)
2. Add the src/handler.py to the package
3. Add the Google Cloud API credentials (google_service_key.json) to the package
4. Zip the package and upload to AWS Lambda 

### Lambda Setup
1. Under Environment Variables, set the key to "GOOGLE_APPLICATION_CREDENTIALS" with the value "google_service_key.json".
2. You may need to increase the Lambda timeout to 15 seconds if you see timeout errors while Lambda is running. 
3. The Input JSON will require 3 key-value pairs with the following keys:
    1. bucket (name of the S3 bucket)
    2. key (name of the audio file)
    3. language (language of the audio file)
    ```json
    {
    "bucket": "<S3 BUCKET NAME>",
    "key": "<AUDIO FILE NAME>",
    "language": "<LANGUAGE>"
    }
    ```



