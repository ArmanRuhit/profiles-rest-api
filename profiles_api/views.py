from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Tset Api View"""

    def get(self, request, formal = None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses Http methods as (get, post, patch)',
            'Is similar to a traditional Django View',
            "Is mapped manually to urls",
            'Gives you the most control over your application logic'
        ]

        return Response({'message': "Hello!", 'an_apiview':an_apiview})