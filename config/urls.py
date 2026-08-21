from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('pessoas/', views.lista_pessoas, name='pessoas'),
    path('estudantes/', views.lista_estudantes, name='estudantes'),
    path('professores/', views.lista_professores, name='professores'),
    path('instituicoes/', views.lista_instituicoes, name='instituicoes'),
    path('cursos/', views.lista_cursos, name='cursos'),
    path('disciplinas/', views.lista_disciplinas, name='disciplinas'),
    path('curso-disciplinas/', views.lista_curso_disciplinas, name='curso_disciplinas'),
    path('turmas/', views.lista_turmas, name='turmas'),
    path('avaliacoes/', views.lista_avaliacoes, name='avaliacoes'),
    path('matriculas/', views.lista_matriculas, name='matriculas'),
    path('frequencias/', views.lista_frequencias, name='frequencias'),
    path('ocorrencias/', views.lista_ocorrencias, name='ocorrencias'),
    path('cidades/', views.lista_cidades, name='cidades'),
]