# image description

# endpoint: https://asdfsadfsafdsfsdfasdf.cognitiveservices.azure.com/
# 
#  pip install azure-cognitiveservices-vision-computervision
#  pip install dlib
#  pip install pillow

import io
import json
import requests
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes, VisualFeatureTypes
from  PIL import Image, ImageDraw, ImageFont

#credential = json.load(open('credential.json'))
#API_KEY = credential['YOUR API KEY']
#ENDPOINT = credential['https://asdfsadfsafdsfsdfasdf.cognitiveservices.azure.com/']
API_KEY = 'YOUR API KEY'
ENDPOINT = 'https://asdfsadfsafdsfsdfasdf.cognitiveservices.azure.com/'
cv_client = ComputerVisionClient(ENDPOINT, CognitiveServicesCredentials(API_KEY))

myimage = open("", "rb")

# URL = 'https://scienceofmomdotcom.files.wordpress.com/2014/09/family_eating_meal.jpg'

#response = cv_client.describe_image(URL,3) # for internet images
response = cv_client.describe_image_in_stream(myimage) # for local images


print (response)
for caption in response.captions:
    print('I see: {0}'.format(caption.text))



#cv_client.describe_image()
#cv_client.analyze_image()
#cv_client.detect_objects()


