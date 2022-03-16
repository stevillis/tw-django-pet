from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render


def login_usuario(request):
    if request.method == 'POST':
        form_login = AuthenticationForm(data=request.POST)
        if form_login.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('listar-clientes')
            else:
                messages.error(request, 'Nome de usuário ou senha incorreta.')
                return redirect('login')
    else:
        form_login = AuthenticationForm()
    return render(request, 'autenticacao/login.html', {'form_login': form_login})


def deslogar_usuario(request):
    logout(request)
    return redirect('login')
