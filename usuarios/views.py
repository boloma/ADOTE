from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

def cadastro (request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        print(nome, email, senha, confirmar_senha)

        if len(nome.strip()) == 0 or len(email.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or len(confirmar_senha.strip()) == 0:
            return render(request, 'cadastro.html')

        if senha != confirmar_senha:
            return render (request, 'cadastro.html')

        try:
            user = User.objects.create.user(
                username = nome,
                email=email,
                password=senha
        )
        #mensagem sucess
            return render (request, 'cadastro.html')
        except:
            #mensagem de erro
            return render(request,'cadastro.html')

