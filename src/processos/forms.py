import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, UserData, Processo

class CustomUserCreateForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'matricula')


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = User
        fields = ('email', 'matricula')

class UserDataForm(forms.ModelForm):

    class Meta:
        model = UserData
        fields = ('nome', 'doc_identificacao', 'doc_tipo',
            'endereco', 'bairro', 'telefone', 'curso')

    nome = forms.CharField(
        label='Nome do Requerente',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-alternative'}),
        required=True
    )

    doc_identificacao = forms.CharField(
        label='Documento de Identificação',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-alternative'}),
        required=True
    )

    doc_tipo = forms.CharField(
        label='Tipo de documento',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-alternative'}),
        required=True
    )

    endereco = forms.CharField(
        label='Endereço',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-alternative'}),
        required=True
    )

    bairro = forms.CharField(
        label='Bairro',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-alternative'}),
        required=True
    )

    telefone = forms.CharField(
        label='Telefone',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-alternative'}),
        required=True
    )

    cep = forms.CharField(
        label='CEP',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-alternative'}),
        required=True
    )

    curso = forms.CharField(
        label='Curso',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-alternative'}),
        required=True
    )

class ProcessoForm(forms.ModelForm):
    
    class Meta:
        model = Processo
        fields = ('numero', 'esclarecimentos', 'tipo_processo',
            'natureza_processo', 'parecer', 'user_data')

    numero = forms.CharField(
        label='Número do Processo',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-alternative'}),
        required=False
    )

    tipo_processo = forms.CharField(
        label='Objeto do requerimento',
        widget=forms.Textarea(),
        required=False
    )

    esclarecimentos = forms.CharField(
        label='Esclarecimentos',
        widget=forms.Textarea(),
        required=True
    )

    natureza_processo = forms.CharField(
        label='Natureza do processo',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-alternative'}),
        required=False
    )

    parecer = forms.CharField(
        label='Parecer',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-alternative'}),
        required=False
    )

    user_data = forms.ModelChoiceField(
        label='Dados cadastrados',
        widget=forms.Select(
            attrs={'class': 'form-control'}
        ),
        queryset=UserData.objects.all(),
        required=True
    )
