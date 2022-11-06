from django.db import models
from .user_manager import get_file_path
from .coordenador import Coordenador
from stdimage import StdImageField


class Curso(models.Model):
    MATUTINO = 'MATUTINO'
    NOTURNO = 'NOTURNO'

    escolha_periodo = [(MATUTINO, 'MATUTINO'),
                        (NOTURNO, 'NOTURNO')]

    PRESENCIAL = 'PRESENCIAL'
    ONLINE = 'ONLINE'

    escolha_modalidade = [(PRESENCIAL, 'PRESENCIAL'),
                            (ONLINE, 'ONLINE')]

    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=2000, default=None)
    destaque = models.CharField(max_length=255, default=None)
    mercado_trabalho = models.TextField(max_length=1000)
    periodo = models.CharField(max_length=10, choices = escolha_periodo, default=MATUTINO)
    duracao = models.CharField(max_length=255, blank=True)
    modalidade = models.CharField(max_length=12, choices = escolha_modalidade, default=PRESENCIAL)
    coordenador = models.ForeignKey(Coordenador, on_delete=models.CASCADE, default=None)
    # disciplina_ofertada = models.ManyToManyField(DisciplinaOfertada, related_name='groups')
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumbnail': {'width': 1500, 'height': 500, 'crop': True}})
    imagem2 = StdImageField('Imagem dois', upload_to=get_file_path, variations={'thumbnail': {'width': 480, 'height': 480, 'crop': True}})
    imagem3 = StdImageField('Imagem tres', upload_to=get_file_path, variations={'thumbnail': {'width': 1100, 'height': 330, 'crop': True}}, blank=True)
    
    def is_upperclass(self):
        return self.periodo in {self.MATUTINO, self.NOTURNO}

    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.nome