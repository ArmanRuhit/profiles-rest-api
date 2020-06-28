from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from . import permissions
from rest_framework import filters

class HelloApiView(APIView):
    """Tset Api View"""

    serializer_class = serializers.HelloSerializers

    def get(self, request, formal = None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses Http methods as (get, post, patch)',
            'Is similar to a traditional Django View',
            "Is mapped manually to urls",
            'Gives you the most control over your application logic'
        ]

        return Response({'message': "Hello!", 'an_apiview':an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = "Hello "+ name
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk = None):
        """Handle update an object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request, pk = None):
        """Handle a partial update of an object"""
        return Response({'method': 'Patch'})

    def delete(self, request, pk=None):
        #Delete an object
        return Response({'method': 'Delete'})

class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializers
    #Test api viewset
    def list(self, request):
        #return a hello message
        a_viewset = [
            'Uses actions(list, create, retrive, update, patial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello', 'a_viewset':a_viewset})
    
    def create(self, request):
        #Create a new hello message
        serializer = self.serializer_class(data= request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = "hello"+name
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        #Handle getting an object by its Id
        return Response({'http_metod': 'GET'})

    def update(self, request, pk=None):
        #Handle update an object
        return Response({'http_metod': 'Update'})
    
    def partial_update(self, request, pk = None):
        return Response({'http_metod': 'Patch'})
    
    def destroy(self, request, pk=None):
        return Response({'http_metod': 'Delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    #Handle creating and updating Profiles
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')