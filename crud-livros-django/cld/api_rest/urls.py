from api_rest import views
from django.urls import path

app_name = 'api_rest'

urlpatterns = [
    path('livros/', views.LivroListServiceView.as_view(), name='livros'),
    path('cadastrarLivro/', views.CadastrarLivroServiceView.as_view(), name='cadastrarLivro'),
    path('atualizarLivro/<int:pk>/', views.AtualizarLivroServiceView.as_view(), name='atualizarLivro'),
    path('excluirLivro/<int:pk>/', views.ExcluirLivroServiceView.as_view(), name='excluirLivro'),
]
