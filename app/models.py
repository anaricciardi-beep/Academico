from django.db import models


class Ocupacao(models.Model):
    """RF02 - Gerenciar ocupação de pessoas"""
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    """RF12 - Gerenciar cidades"""
    nome = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

    def __str__(self):
        return f"{self.nome} - {self.uf}"


class Pessoa(models.Model):
    """RF01 - Gerenciar pessoas"""
    nome = models.CharField(max_length=150)
    nome_do_pai = models.CharField(max_length=150, blank=True, null=True)
    nome_da_mae = models.CharField(max_length=150, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_nasc = models.DateField()
    email = models.EmailField()
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True, related_name='pessoas')
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, blank=True, related_name='pessoas')

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.nome


class Instituicao(models.Model):
    """RF03 - Gerenciar instituição de ensino"""
    nome = models.CharField(max_length=150)
    site = models.URLField(blank=True, null=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, blank=True, related_name='instituicoes')

    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"

    def __str__(self):
        return self.nome


class AreaSaber(models.Model):
    """RF04 - Gerenciar áreas do saber"""
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"

    def __str__(self):
        return self.nome


class Turno(models.Model):
    """RF06 - Gerenciar turnos"""
    nome = models.CharField(max_length=50)  # Ex: Matutino, Noturno

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

    def __str__(self):
        return self.nome


class Curso(models.Model):
    """RF05 - Gerenciar cursos"""
    nome = models.CharField(max_length=150)
    carga_horaria_total = models.IntegerField()
    duracao_meses = models.IntegerField()
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, related_name='cursos')
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, related_name='cursos')

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    """RF07 - Gerenciar disciplinas"""
    nome = models.CharField(max_length=150)
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, related_name='disciplinas')

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

    def __str__(self):
        return self.nome


class CursoDisciplina(models.Model):
    """RF14 - Manter disciplinas por cursos"""
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas_curso')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='cursos_disciplina')
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()

    class Meta:
        verbose_name = "Disciplina do Curso"
        verbose_name_plural = "Disciplinas dos Cursos"

    def __str__(self):
        return f"{self.curso.nome} - {self.disciplina.nome}"


class Turma(models.Model):
    """RF11 - Gerenciar turmas"""
    nome = models.CharField(max_length=100)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Pessoa, related_name='turmas', blank=True)

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

    def __str__(self):
        return self.nome


class TipoAvaliacao(models.Model):
    """RF15 - Manter tipos de avaliação"""
    nome = models.CharField(max_length=100)  # Ex: Prova, Projeto, Lista, Trabalho, Seminário

    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliação"

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    """RF09 - Gerenciar avaliações"""
    descricao = models.CharField(max_length=255)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='avaliacoes')
    tipo_avaliacao = models.ForeignKey(TipoAvaliacao, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

    def __str__(self):
        return f"{self.descricao} - {self.disciplina.nome}"


class Matricula(models.Model):
    """RF08 - Gerenciar Matrículas"""
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"

    def __str__(self):
        return f"{self.pessoa.nome} - {self.curso.nome}"


class Frequencia(models.Model):
    """RF10 - Gerenciar frequência"""
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    numero_faltas = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"

    def __str__(self):
        return f"{self.pessoa.nome} - {self.disciplina.nome}: {self.numero_faltas} faltas"


class Ocorrencia(models.Model):
    """RF13 - Gerenciar ocorrências"""
    descricao = models.TextField()
    data = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

    def __str__(self):
        return f"{self.pessoa.nome} - {self.data}"