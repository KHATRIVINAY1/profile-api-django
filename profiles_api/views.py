from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    '''Test API view '''

    def get(self,request,format =None):
        an_apiview= [
            'Uses HTTP methods as function (get,postmpatch,put,delete)',
            'Is similar to a Traditional Django View',
            'Give the most control over you application',
            'Is mapped mannualy to Urls'
        ]

        return Response({'message':'hello','an_apiview':an_apiview})
