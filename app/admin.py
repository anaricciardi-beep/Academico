from django.contrib import admin
from .models import (
    UF, Cidade, Ocupacao, Pessoa, Estudante, Professor, Instituicao,
    AreaSaber, Turno, Curso, Disciplina, CursoDisciplina,
    Turma, TipoAvaliacao, Avaliacao, Matricula, Frequencia, Ocorrencia
)


class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1 #qtde de linhas em branco para cadastro

class UFAdmin(admin.ModelAdmin):
    inlines = [CidadeInline]

admin.site.register(UF, UFAdmin)


class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class OcupacaoAdmin(admin.ModelAdmin):
    inlines = [PessoaInline]

admin.site.register(Ocupacao, OcupacaoAdmin)


class CursoInstituicaoInline(admin.TabularInline):
    model = Curso
    extra = 1

class InstituicaoAdmin(admin.ModelAdmin):
    inlines = [CursoInstituicaoInline]

admin.site.register(Instituicao, InstituicaoAdmin)


class CursoAreaInline(admin.TabularInline):
    model = Curso
    extra = 1

class AreaSaberAdmin(admin.ModelAdmin):
    inlines = [CursoAreaInline]

admin.site.register(AreaSaber, AreaSaberAdmin)


class CursoDisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class CursoAdmin(admin.ModelAdmin):
    inlines = [CursoDisciplinaInline]

admin.site.register(Curso, CursoAdmin)


class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AvaliacaoInline]

admin.site.register(Disciplina, DisciplinaAdmin)


class TurmaAlunoInline(admin.TabularInline):
    model = Turma.alunos.through
    extra = 1

class TurmaAdmin(admin.ModelAdmin):
    inlines = [TurmaAlunoInline]
    exclude = ('alunos',)

admin.site.register(Turma, TurmaAdmin)


class FrequenciaInline(admin.TabularInline):
    model = Frequencia
    extra = 1

class PessoaAdmin(admin.ModelAdmin):
    inlines = [FrequenciaInline]

admin.site.register(Pessoa, PessoaAdmin)


admin.site.register(Cidade)
admin.site.register(Estudante)
admin.site.register(Professor)
admin.site.register(Turno)
admin.site.register(TipoAvaliacao)
admin.site.register(Matricula)
admin.site.register(Ocorrencia)