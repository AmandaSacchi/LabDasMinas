from django.shortcuts import render
from .models import Candidato 
from .forms import CandidatoForm
from django.shortcuts import redirect
# from django.http import HttpResponse


# Create your views here.
#Views: requisicao 
def index(request):
    return render(request, 'index.html') #renderizando (interpretando e colocando na pagina html)

def cadastro(request):
    if request.method == "POST":
      form = CandidatoForm(request.POST)
      if form.is_valid():
            candidado = form.save()
            msg = "Cadastro realizado com sucesso!"
            contexto = {'form':form, 'msg':msg}
            return render(request, 'cadastro.html', contexto)
    else:
        form = CandidatoForm()
        contexto = {'form':form}       
    return render(request, 'cadastro.html', contexto)

# def sobre(request):
#     return render(request, 'sobre.html')

def cadastrados(request):
    cadastrados = Candidato.objects.all()
    return render(request, 'cadastrados.html', {'cadastrados': cadastrados})



 #ENTRAR PELA PRIMEIRA VEZ NO SITE USA METODO REQUEST.GET
    #ENTRA PELO CLICK ENVIANDO O FORMULARIO USA O METODO REQUEST.POST)  
# def fazer_cadastro(request):
#     candidatos = Candidato.objects.all()
#     formulario = CandidatoForm(request.POST or None)
#     msg = ''
#     if formulario.is_valid():
#         formulario.save()
#         formulario = CandidatoForm() #depois de enviar, apaga
#         msg = 'Cadastro realizado com sucesso'

#     contexto = {
#         'form' : formulario,
#         'msg' : msg
#     }

#     #CONTEXTO: MANDA COISAS DO PYTHON PRO HTML (ACESSA FORMULARIO DO BACKEND PRO FRONTEND)
#     return render(request, 'cadastro.html', contexto)