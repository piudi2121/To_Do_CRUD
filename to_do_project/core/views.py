from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tarefa

# Create your views here.
def index(request):
    if request.method == 'POST':
        tarefa_text = request.POST.get('tarefa_text')
        dificuldade = request.POST.get('dificuldade')
        data_conclusao = request.POST.get('data_conclusao')
        tarefa = Tarefa(tarefaText = tarefa_text,dificuldade = dificuldade,dataConclusao = data_conclusao)
        tarefa.save()
        return redirect('/')
    elif request.method == 'GET':
        tarefas = Tarefa.objects.all()
        return render(request, 'index.html', {'Tarefas':tarefas})
    
def deletar_tarefa(request, id):
    tarefa = Tarefa.objects.get(id = id)
    tarefa.delete()
    return redirect('/')

def atualizar_tarefa(request, id):
    tarefa = Tarefa.objects.get(id = id)

    tarefa_text = request.POST.get('tarefa_text')
    dificuldade = request.POST.get('dificuldade')
    dataConclusao = request.POST.get('data_conclusao')

    tarefa.tarefaText = tarefa_text
    tarefa.dificuldade = dificuldade
    tarefa.dataConclusao = dataConclusao

    tarefa.save()
    return redirect('/')