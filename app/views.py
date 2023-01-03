from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login

from app.models.disciplina_ofertada import DisciplinaOfertada
from app.models.mensagem import Mensagem

from .models.curso import Curso
from .models.aluno import Aluno
from .models.matricula import Matricula
from .models.atividade_vinculada import AtividadeVinculada

from .models.entrega_atividade import EntregaAtividade



class IndexView(ListView):
    model = Curso
    context_object_name = 'curso_list'
    template_name = 'app/home.html'

    def get_queryset(self):
        return Curso.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()
        context['img1'] = Curso.objects.order_by('?')[:3]
        return context

class CursoDetailView(DetailView):
    model = Curso
    context_object_name = 'curso_list'
    template_name = 'app/curso.html'

    def get_queryset(self):
        self.nome = get_object_or_404(Curso, pk=self.kwargs['pk'])
        return Curso.objects.filter(nome=self.nome)

    def get_context_data(self, **kwargs):
        context = super(CursoDetailView, self).get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()
        context['curso'] = Curso.objects.get(nome=self.nome)
        context['destaques'] = Curso.objects.get(id=self.nome.id)
        # context['coordenador'] = Curso.objects.get(nome__coordenador)
        return context

class LoginView(TemplateView):
    template_name = 'app/login.html'

class AlunoView(TemplateView):
    template_name = 'app.aluno.html'

class AlunoDetailView(DetailView):
    model = Aluno
    context_object_name = 'aluno_list'
    template_name = 'app/aluno.html'

    def get_queryset(self):
        self.user = get_object_or_404(Aluno, pk=self.kwargs['pk'])
        print(self.user)
        return Aluno.objects.filter(id__exact=self.user.id)

    def get_context_data(self, **kwargs):
        context = super(AlunoDetailView, self).get_context_data(**kwargs)
        context['aluno'] = Aluno.objects.get(usuario__email=self.user.usuario)
        aluno = context['matricula_aluno'] = Matricula.objects.get(aluno__usuario=self.user.usuario) 
        context['disciplinas'] = DisciplinaOfertada.objects.filter(curso=aluno.curso)

        context['atividades_turma'] = AtividadeVinculada.objects.filter\
        (disciplina_ofertada__turma=aluno.turma).order_by('?')[:3]

        context['atividades'] = AtividadeVinculada.objects.filter\
        (disciplina_ofertada__curso=aluno.curso).filter\
            (disciplina_ofertada__turma=aluno.turma).order_by('?')[:2]

        context['entregas'] = EntregaAtividade.objects.filter(aluno=aluno.id).order_by('?')[:2]
            

        context['aluno_all'] = Matricula.objects.get(aluno__usuario=self.user.usuario)

        context['mensagens'] = Mensagem.objects.filter(aluno__usuario=self.user.usuario)
        
        return context

class BoletimView(DetailView):
    model = Aluno
    context_object_name = 'aluno_list'
    template_name = 'app.boletim.html'

    def get_queryset(self):
        self.user = get_object_or_404(Aluno, pk=self.kwargs['pk'])
        return Aluno.objects.filter(id__exact=self.user.id)


# /////////////////////////////////////////////////////////////////////////////////////
# ///////////LOGIN////////////////

def login(request):
    username = request.POST['username']
    password = request.POST['password']

    print(username, password)

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('templates/login')
    