import json
import io
import boto3

def analysis(event, context):

    #download file from S3    
    s3 = boto3.resource('s3')
        
    bucket = event['bucket']
    key=event['key']
    download_destination_path='/tmp/' + key

    s3.Bucket(bucket).download_file(key, download_destination_path)
    
    #analyze audio file using Google Speech To Text
    #languages codes such as cmn-Hans-CN can be found here: https://cloud.google.com/speech-to-text/docs/languages
    language_code=event['language'] 
    audio_ret = speechanalysis(download_destination_path,language_code)   

    body = {
        "message": "Recognized Characters:",
        "input": audio_ret
    }
    
    #this parameter ensure_ascii=false ensures chinese chars can be displayed in the final REST API response
    response = {
        "statusCode": 200,
        "body": json.dumps(body,ensure_ascii=False)
    }
    
    return response

def speechanalysis(filename,lang_code):
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    
    client = speech.SpeechClient()
    
    # Loads the audio into memory
    with io.open(filename, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    
    #Requires audio language and encoding 
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        language_code=lang_code)

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    #get final recognized words
    for result in response.results:
        finaloutput = result.alternatives[0].transcript
        
    return finaloutput
    
if __name__ == '__main__':
    analysis(' ',' ')