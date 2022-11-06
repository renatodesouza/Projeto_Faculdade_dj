from django.db import models
from .curso import Curso
# from .disciplina_ofertada import DisciplinaOfertada




class Turma(models.Model):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    escolha_turma = [(A, 'A'), (B, 'B'), (C, 'C'), (D, 'D'),]
    
    turma = models.CharField(max_length=4, choices=escolha_turma)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, default=1)
    # disciplina_ofertada = models.ManyToManyField(DisciplinaOfertada, related_name='groups')

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'

    def __str__(self):
        return self.turma