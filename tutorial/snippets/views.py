from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework.generics import GenericAPIView 
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse


# class snippet_list(ModelViewSet):
#     serializer_class = SnippetSerializer
#     queryset = Snippet.objects.all()

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#please check out, intersting

class snippet_list(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class snippet_detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class snippet_list(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class snippet_detail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class snippet_list(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

#     serializer_class = SnippetSerializer
#     queryset = Snippet.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class snippet_detail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):

#     serializer_class = SnippetSerializer
#     queryset = Snippet.objects.all()

#     def get(self, request, *args, **kwargs):
#         print(args)
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)


#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# @api_view(['GET','POST'])
# def snippet_list(request,format=None):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         ser = SnippetSerializer(snippets, many=True)
#         print(ser.data[0])
#         return Response(ser.data)
#         return JsonResponse(ser.data, safe=False,status=200)

#     elif request.method == 'POST':
#         data = request.data
#         print(data)
#         ser = SnippetSerializer(data=data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=201) #u can use response instead, check tut2
#         return Response(ser.errors, status=400)
    

# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request,pk,format=None):
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         ser = SnippetSerializer(snippet)
#         return Response(ser.data,status=200)

#     elif request.method == 'PUT':
#         data = request.data
#         ser = SnippetSerializer(snippet, data=data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data,status=201)
#         return Response(ser.errors, status=400)

#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=204)
