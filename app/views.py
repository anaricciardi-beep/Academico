from django.shortcuts import render
from .models import (
    Pessoa, Estudante, Professor, Instituicao, AreaSaber, 
    Turno, Curso, Disciplina, CursoDisciplina, Turma, 
    TipoAvaliacao, Avaliacao, Matricula, Frequencia, Ocorrencia, UF, Cidade
)

def index(request):
    return render(request, 'index.html')

def lista_pessoas(request):
    pessoas = Pessoa.objects.all().select_related('cidade', 'ocupacao').order_by('nome')
    return render(request, 'pessoas.html', {'pessoas': pessoas})

def lista_estudantes(request):
    estudantes = Estudante.objects.all().select_related('cidade', 'ocupacao').order_by('nome')
    return render(request, 'estudantes.html', {'estudantes': estudantes})

def lista_professores(request):
    professores = Professor.objects.all().select_related('cidade', 'ocupacao').order_by('nome')
    return render(request, 'professores.html', {'professores': professores})

def lista_instituicoes(request):
    instituicoes = Instituicao.objects.all().select_related('cidade').order_by('nome')
    return render(request, 'instituicoes.html', {'instituicoes': instituicoes})

def lista_cursos(request):
    cursos = Curso.objects.all().select_related('area_saber', 'instituicao').order_by('nome')
    return render(request, 'cursos.html', {'cursos': cursos})

def lista_disciplinas(request):
    disciplinas = Disciplina.objects.all().select_related('area_saber').order_by('nome')
    return render(request, 'disciplinas.html', {'disciplinas': disciplinas})

def lista_curso_disciplinas(request):
    relacoes = CursoDisciplina.objects.all().select_related('curso', 'disciplina', 'turno')
    return render(request, 'curso_disciplinas.html', {'relacoes': relacoes})

def lista_turmas(request):
    turmas = Turma.objects.all().select_related('turno').order_by('nome')
    return render(request, 'turmas.html', {'turmas': turmas})

def lista_avaliacoes(request):
    avaliacoes = Avaliacao.objects.all().select_related('curso', 'disciplina', 'tipo_avaliacao')
    return render(request, 'avaliacoes.html', {'avaliacoes': avaliacoes})

def lista_matriculas(request):
    matriculas = Matricula.objects.all().select_related('instituicao', 'curso', 'pessoa')
    return render(request, 'matriculas.html', {'matriculas': matriculas})

def lista_frequencias(request):
    frequencias = Frequencia.objects.all().select_related('curso', 'disciplina', 'pessoa')
    return render(request, 'frequencias.html', {'frequencias': frequencias})

def lista_ocorrencias(request):
    ocorrencias = Ocorrencia.objects.all().select_related('curso', 'disciplina', 'pessoa').order_by('-data')
    return render(request, 'ocorrencias.html', {'ocorrencias': ocorrencias})

def lista_cidades(request):
    cidades = Cidade.objects.all().select_related('uf').order_by('nome')
    return render(request, 'cidades.html', {'cidades': cidades})