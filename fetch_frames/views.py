from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
import cv2 as cv
import base64

@api_view(['POST'])
def getFrame(request):
  if request.method == 'POST':
    data = JSONParser().parse(request)
    image = base64.b64decode(data['base64'])
    print(image)
    return HttpResponse({ "message": "Ok" })
  return HttpResponse('Hello World')