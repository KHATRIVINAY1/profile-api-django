from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

# Create your views here.

class HelloApiView(APIView):
    '''Test API view '''
    serializer_class =serializers.HelloSerializer

    def get(self,request,format =None):
        an_apiview= [
            'Uses HTTP methods as function (get,postmpatch,put,delete)',
            'Is similar to a Traditional Django View',
            'Give the most control over you application',
            'Is mapped mannualy to Urls'
        ]

        return Response({'message':'hello','an_apiview':an_apiview})

    def post(self,request):
        '''Create a hello message'''
        serializer =self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        '''Handel updating Object'''
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        '''Handel a Partial Update of an Object'''
        return Response({'method':'Patch'})

    def delete(self,request,pk=None):
        '''Delete an Object'''
        return Response({'method':'Delete'})


