from django.shortcuts import render
from livros import models
from api_rest import serializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class LivroListServiceView(generics.ListCreateAPIView):
    queryset = models.Livro.objects.all()
    serializer_class = serializers.LivroSerializer

class CadastrarLivroServiceView(APIView):
    serializer_class = serializers.LivroSerializer

    def post(self, request, format=None):
        serializer = serializers.LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.erros, status.HTTP_400_BAD_REQUEST)

class AtualizarLivroServiceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Livro.objects.all()
    serializer_class = serializers.LivroSerializer

    def put(self, request, pk):
        livro = models.Livro.objects.get(pk=pk)
        serializer = serializers.LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExcluirLivroServiceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Livro.objects.all()
    serializer_class = serializers.LivroSerializer

    def delete(self, request, pk):
        livro = models.Livro.objects.get(pk=pk)
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
