import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_user
from django.http import HttpResponseForbidden, Http404, HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomUserCreateForm, UserDataForm, ProcessoForm
from .models import UserData, Processo

# Create your views here.
tipos_processos_legenda = {
    'aproveitamento': 'Aproveitamento de Estudos',
    'adocao': 'Adoção do Nome Social',
    'desistencia': 'Desistência definitiva do Curso',
    'dilatacao': 'Dilatação do Prazo Máximo para Conclusão do Curso',
    'tirocinio_dispoensa': 'Dispensa de Tirocínio Docente',
    'superior_mat': 'Matrícula como Pordator de Diploma de Nível Superior de caráter especial',
    'ingresso_mat': 'Matrícula de Ingresso através de Processo Seletivo de Vagas Residuais',
    'permanencia': 'Permanência no Curso',
    'reconcideracao': 'Reconsideração de despacho/Recurso',
    'retificacao': 'Retificação de Histórico',
    'ex_oficio_transferencia': 'Transferência "ex-officio"',
    'especial_transferencia': 'Transferência Interna de Caráter Especial',
    'pos_transferencia': 'Transferência "ex-officio"',
    'trancamento': 'Trancamento',
    'trancamento-parcial': 'Parcial de inscrição em disciplinas',
    'trancamento-total': 'Total de inscrição em disciplinas (semestre corrente)',
    'trancamento-tempo': 'Por tempo determinado'
}


def home(request):
    return render(request, 'index.html')

def logout(request):
    logout_user(request)

    return redirect('home')

@login_required
def get_user_processos(request):
    processos = Processo.objects.filter(aluno=request.user).all()

    for processo in processos:
        tipos = processo.tipo_processo.split(',')
        new_tipos = ''

        for tipo in tipos:
            new_tipos += tipos_processos_legenda[tipo] + ', ' if tipo in tipos_processos_legenda else ''
        
        new_tipos = new_tipos[:-2]
        setattr(processo, 'tipo_processo', new_tipos)

    return render(request, 'processos.html', {'processos': processos})

@login_required
def add_user_processo(request):
    if request.method == 'POST':
        form = ProcessoForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            tipos = ''

            for tipo in request.POST.getlist('tipos[]'):
                tipos += tipo + ','

            obj.tipo_processo = tipos
            obj.aluno = request.user
            obj.save()

            return redirect('processos')
        else:
            print(form.errors)
    else:
        form = ProcessoForm()

    return render(request, 'processos_add_edit.html', {'form': form})

@login_required
def edit_user_processo(request, id_processo):
    try:
        processo = Processo.objects.get(id=id_processo)
    except Processo.DoesNotExist:
        raise Http404('Processo inexistente')

    if processo.aluno != request.user:
        return HttpResponseForbidden('Não autorizado')

    if request.method == 'POST':
        form = ProcessoForm(request.POST, instance=processo)

        if form.is_valid():
            obj = form.save(commit=False)
            tipos = ''

            for tipo in request.POST.getlist('tipos[]'):
                tipos += tipo + ','

            obj.tipo_processo = tipos
            obj.save()

            return redirect('processos')
        else:
            print(form.errors)
    else:
        form = ProcessoForm(instance=processo)

    return render(request, 'processos_add_edit.html', {'form': form})

@login_required
def clone_user_processo(request):
    id_processo = request.POST['id']

    try:
        processo = Processo.objects.get(id=id_processo)
    except Processo.DoesNotExist:
        raise Http404('Processo inexistente')

    if processo.aluno != request.user:
        return HttpResponseForbidden('Não autorizado')

    processo.pk = None
    processo.save()

    return HttpResponse(json.dumps({'url': reverse('processos')}), content_type='application/json')

@login_required
def remove_user_processo(request):
    id_processo = request.POST['id']

    try:
        processo = Processo.objects.get(id=id_processo)
    except Processo.DoesNotExist:
        raise Http404('Processo inexistente')

    if processo.aluno != request.user:
        return HttpResponseForbidden('Não autorizado')

    processo.delete()

    return HttpResponse(json.dumps({'url': reverse('processos')}), content_type='application/json')

@login_required
def view_user_processo(request, id_processo):
    try:
        processo = Processo.objects.get(id=id_processo)
    except Processo.DoesNotExist:
        raise Http404('Processo inexistente')

    if processo.aluno != request.user:
        return HttpResponseForbidden('Não autorizado')

    return render(request, 'processos_view.html', {
        'user_data': processo.user_data,
        'processo': processo
    })

def requerimento(request, id_processo):
    try:
        processo = Processo.objects.get(id=id_processo)
    except Processo.DoesNotExist:
        raise Http404('Processo inexistente')

    if processo.aluno != request.user:
        return HttpResponseForbidden('Não autorizado')

    return render(request, 'requerimento_escolar.html', {
        'processo': processo
    })

@login_required
def get_user_data(request):
    user_data = UserData.objects.filter(aluno=request.user).all()

    return render(request, 'data.html', { 'user_data': user_data })

@login_required
def add_user_data(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.aluno = request.user
            obj.save()

            return redirect('user_data')
        else:
            print(form.errors)
    else:
        form = UserDataForm()

    return render(request, 'data_add_edit.html', {'form': form})

@login_required
def edit_user_data(request, id_data):
    try:
        user_data = UserData.objects.get(id=id_data)
    except Processo.DoesNotExist:
        raise Http404('Dado inexistente')

    if user_data.aluno != request.user:
        return HttpResponseForbidden('Não autorizado')

    if request.method == 'POST':
        form = UserDataForm(request.POST, instance=user_data)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.aluno = request.user
            obj.save()

            return redirect('user_data')
        else:
            print(form.errors)
    else:
        form = UserDataForm(instance=user_data)

    return render(request, 'data_add_edit.html', {
        'form': form,
        'add': False
    })

class Registro(generic.CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'registration/registration.html'
