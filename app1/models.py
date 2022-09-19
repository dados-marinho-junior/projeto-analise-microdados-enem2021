from django.db import models

# Create your models here.

class TagDis(models.Model):
    uf = models.CharField(max_length=2,verbose_name="UF")
    media_geral = models.FloatField(verbose_name="Media Geral")
    media = models.FloatField(verbose_name="Media Participantes")
    inscritos = models.IntegerField(verbose_name="Inscritos")
    participantes = models.IntegerField(verbose_name="Participantes")
    faltantes = models.IntegerField(verbose_name="Faltantes")
    data = models.IntegerField(verbose_name="Ano",default=2022)