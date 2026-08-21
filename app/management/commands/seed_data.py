import datetime

from django.core.management.base import BaseCommand

from app.models import (
    UF, Cidade, Ocupacao, Pessoa, Estudante, Professor, Instituicao,
    AreaSaber, Turno, Curso, Disciplina, CursoDisciplina, Turma,
    TipoAvaliacao, Avaliacao, Matricula, Frequencia, Ocorrencia,
)


class Command(BaseCommand):
    help = "Popula o banco de dados com registros de exemplo"

    def handle(self, *args, **options):
        uf_sp, _ = UF.objects.get_or_create(sigla='SP', defaults={'nome': 'São Paulo'})
        uf_rj, _ = UF.objects.get_or_create(sigla='RJ', defaults={'nome': 'Rio de Janeiro'})
        uf_mg, _ = UF.objects.get_or_create(sigla='MG', defaults={'nome': 'Minas Gerais'})

        cid_sp, _ = Cidade.objects.get_or_create(nome='São Paulo', uf=uf_sp)
        cid_campinas, _ = Cidade.objects.get_or_create(nome='Campinas', uf=uf_sp)
        cid_rj, _ = Cidade.objects.get_or_create(nome='Rio de Janeiro', uf=uf_rj)
        cid_bh, _ = Cidade.objects.get_or_create(nome='Belo Horizonte', uf=uf_mg)

        oc_dev, _ = Ocupacao.objects.get_or_create(nome='Desenvolvedor(a) de Software')
        oc_prof, _ = Ocupacao.objects.get_or_create(nome='Professor(a)')
        oc_analista, _ = Ocupacao.objects.get_or_create(nome='Analista de Dados')

        pessoas_data = [
            {'nome': 'Ana Clara Silva', 'cpf': '111.111.111-11', 'data_nasc': datetime.date(2001, 3, 15),
             'email': 'ana.silva@example.com', 'cidade': cid_sp, 'ocupacao': oc_dev},
            {'nome': 'Bruno Costa Lima', 'cpf': '222.222.222-22', 'data_nasc': datetime.date(1999, 7, 22),
             'email': 'bruno.lima@example.com', 'cidade': cid_campinas, 'ocupacao': oc_analista},
            {'nome': 'Carla Mendes Souza', 'cpf': '333.333.333-33', 'data_nasc': datetime.date(2002, 11, 5),
             'email': 'carla.souza@example.com', 'cidade': cid_rj, 'ocupacao': oc_dev},
        ]
        for dados in pessoas_data:
            Pessoa.objects.get_or_create(cpf=dados['cpf'], defaults=dados)

        estudantes_data = [
            {'nome': 'Diego Fernandes Rocha', 'cpf': '444.444.444-44', 'data_nasc': datetime.date(2003, 5, 10),
             'email': 'diego.rocha@example.com', 'cidade': cid_bh, 'ocupacao': None, 'codigo_estudante': 'EST0001'},
            {'nome': 'Elisa Martins Alves', 'cpf': '555.555.555-55', 'data_nasc': datetime.date(2004, 1, 28),
             'email': 'elisa.alves@example.com', 'cidade': cid_sp, 'ocupacao': None, 'codigo_estudante': 'EST0002'},
        ]
        for dados in estudantes_data:
            Estudante.objects.get_or_create(cpf=dados['cpf'], defaults=dados)

        professores_data = [
            {'nome': 'Fábio Ribeiro Nunes', 'cpf': '666.666.666-66', 'data_nasc': datetime.date(1978, 9, 3),
             'email': 'fabio.nunes@example.com', 'cidade': cid_rj, 'ocupacao': oc_prof, 'titulacao': 'Doutor'},
            {'nome': 'Gisele Pereira Dias', 'cpf': '777.777.777-77', 'data_nasc': datetime.date(1985, 4, 19),
             'email': 'gisele.dias@example.com', 'cidade': cid_bh, 'ocupacao': oc_prof, 'titulacao': 'Mestre'},
        ]
        for dados in professores_data:
            Professor.objects.get_or_create(cpf=dados['cpf'], defaults=dados)

        inst_a, _ = Instituicao.objects.get_or_create(
            nome='Faculdade Horizonte', defaults={
                'site': 'https://horizonte.edu.br', 'email': 'contato@horizonte.edu.br',
                'telefone': '(11) 4000-1000', 'cidade': cid_sp,
            })
        inst_b, _ = Instituicao.objects.get_or_create(
            nome='Instituto Tecnológico Vale Verde', defaults={
                'site': 'https://valeverde.edu.br', 'email': 'contato@valeverde.edu.br',
                'telefone': '(21) 4000-2000', 'cidade': cid_rj,
            })

        area_ti, _ = AreaSaber.objects.get_or_create(nome='Tecnologia da Informação')
        area_adm, _ = AreaSaber.objects.get_or_create(nome='Administração')

        turno_manha, _ = Turno.objects.get_or_create(nome='Manhã')
        turno_noite, _ = Turno.objects.get_or_create(nome='Noite')

        curso_adsi, _ = Curso.objects.get_or_create(
            nome='Análise e Desenvolvimento de Sistemas', defaults={
                'carga_horaria_total': 2400, 'duracao_meses': 24,
                'area_saber': area_ti, 'instituicao': inst_a,
            })
        curso_adm, _ = Curso.objects.get_or_create(
            nome='Administração de Empresas', defaults={
                'carga_horaria_total': 3200, 'duracao_meses': 48,
                'area_saber': area_adm, 'instituicao': inst_b,
            })

        disc_bd, _ = Disciplina.objects.get_or_create(nome='Banco de Dados', defaults={'area_saber': area_ti})
        disc_prog, _ = Disciplina.objects.get_or_create(nome='Programação Web', defaults={'area_saber': area_ti})
        disc_gestao, _ = Disciplina.objects.get_or_create(nome='Gestão de Pessoas', defaults={'area_saber': area_adm})

        CursoDisciplina.objects.get_or_create(
            curso=curso_adsi, disciplina=disc_bd, turno=turno_manha, defaults={'carga_horaria': 80})
        CursoDisciplina.objects.get_or_create(
            curso=curso_adsi, disciplina=disc_prog, turno=turno_noite, defaults={'carga_horaria': 100})
        CursoDisciplina.objects.get_or_create(
            curso=curso_adm, disciplina=disc_gestao, turno=turno_manha, defaults={'carga_horaria': 60})

        turma_a, _ = Turma.objects.get_or_create(nome='ADS 2026/1 - Manhã', turno=turno_manha)
        turma_b, _ = Turma.objects.get_or_create(nome='ADM 2026/1 - Noite', turno=turno_noite)

        estudante_diego = Estudante.objects.get(cpf='444.444.444-44')
        estudante_elisa = Estudante.objects.get(cpf='555.555.555-55')
        turma_a.alunos.add(estudante_diego.pessoa_ptr, estudante_elisa.pessoa_ptr)

        tipo_prova, _ = TipoAvaliacao.objects.get_or_create(nome='Prova')
        tipo_trabalho, _ = TipoAvaliacao.objects.get_or_create(nome='Trabalho')

        Avaliacao.objects.get_or_create(
            descricao='Prova 1 - Banco de Dados', curso=curso_adsi, disciplina=disc_bd,
            tipo_avaliacao=tipo_prova, defaults={'nota': 8.5})
        Avaliacao.objects.get_or_create(
            descricao='Trabalho 1 - Programação Web', curso=curso_adsi, disciplina=disc_prog,
            tipo_avaliacao=tipo_trabalho, defaults={'nota': 9.0})

        Matricula.objects.get_or_create(
            instituicao=inst_a, curso=curso_adsi, pessoa=estudante_diego.pessoa_ptr,
            defaults={'data_inicio': datetime.date(2026, 2, 1), 'data_previsao_termino': datetime.date(2028, 2, 1)})
        Matricula.objects.get_or_create(
            instituicao=inst_a, curso=curso_adsi, pessoa=estudante_elisa.pessoa_ptr,
            defaults={'data_inicio': datetime.date(2026, 2, 1), 'data_previsao_termino': datetime.date(2028, 2, 1)})

        Frequencia.objects.get_or_create(
            curso=curso_adsi, disciplina=disc_bd, pessoa=estudante_diego.pessoa_ptr, defaults={'numero_faltas': 2})
        Frequencia.objects.get_or_create(
            curso=curso_adsi, disciplina=disc_prog, pessoa=estudante_elisa.pessoa_ptr, defaults={'numero_faltas': 0})

        Ocorrencia.objects.get_or_create(
            descricao='Chegou atrasado à aula', data=datetime.date(2026, 3, 10),
            curso=curso_adsi, disciplina=disc_bd, pessoa=estudante_diego.pessoa_ptr)

        self.stdout.write(self.style.SUCCESS('Registros de exemplo inseridos com sucesso.'))
