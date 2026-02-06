from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('deletar-tarefa/<int:id>', views.deletar_tarefa, name='deletar_tarefa'),
    path('atualizar-tarefa/<int:id>', views.atualizar_tarefa, name='atualizar_tarefa'),
]