from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.decorators import api_view
from rest_framework import mixins
from rest_framework.generics import GenericAPIView 
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status


# class snippet_list(ModelViewSet):
#     serializer_class = SnippetSerializer
#     queryset = Snippet.objects.all()




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

@api_view(['GET','POST'])
def snippet_list(request,format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        ser = SnippetSerializer(snippets, many=True)
        print(ser.data[0])
        return Response(ser.data)
        return JsonResponse(ser.data, safe=False,status=200)

    elif request.method == 'POST':
        data = request.data
        print(data)
        ser = SnippetSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201) #u can use response instead, check tut2
        return Response(ser.errors, status=400)
    

@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk,format=None):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        ser = SnippetSerializer(snippet)
        return Response(ser.data,status=200)

    elif request.method == 'PUT':
        data = request.data
        ser = SnippetSerializer(snippet, data=data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=201)
        return Response(ser.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=204)
