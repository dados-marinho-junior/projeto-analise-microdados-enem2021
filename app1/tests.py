from typing import Dict
from django.test import TestCase

# Create your tests here.


from .models import TagDis
from django.db.models import Avg, aggregates, Sum


class Teste1(TestCase):    
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once.")
        pass


    def setUp(self):
        print("setUp: Run once ...setup clean data.")
        pass


# SELECT DATA AS Ano, SUM(INSCRITOS) AS Inscritos, SUM(PARTICIPANTES) AS Participantes,
# SUM(FALTANTES) AS Faltas, ROUND(AVG(MEDIA_GERAL),2 ) AS Media_Inscritos,
# ROUND(AVG(MEDIA),2 ) AS Media_Participantes FROM app1_tagdis GROUP BY DATA ORDER BY DATA ASC;

    def test_Inscriots(self):
        Anos = list(TagDis.objects.order_by('data').values_list('data', flat=True).distinct())

        print("Anos............:", Anos)

        categories = []
        inscritos = []    
        participantes = []
        faltantes = []
        media_geral = []
        media = []

        for ano in Anos:
            print (f'Ano.............: {ano}')                   

            categories.append(ano)
            
            Inscritos = TagDis.objects.filter(data=ano).aggregate(Sum('inscritos'))
            Participantes = TagDis.objects.filter(data=ano).aggregate(Sum('participantes'))        
            Faltantes = TagDis.objects.filter(data=ano).aggregate(Sum('faltantes'))                    
            MediaGeral = TagDis.objects.filter(data=ano).aggregate(Avg('media_geral'))
            Media = TagDis.objects.filter(data=ano).aggregate(Avg('media'))                    
            
            print("Inscritos.......:", Inscritos)
            print("Participantes...:", Participantes)
            print("Faltantes.......:", Faltantes)
            print("Media Geral.....:", MediaGeral)
            print("Media...........:", Media)

            inscritos.append(Inscritos['inscritos__sum'])
            participantes.append(Participantes['participantes__sum'])
            faltantes.append(Faltantes['faltantes__sum'])
            media_geral.append( round(MediaGeral['media_geral__avg'],2))
            media.append( round(Media['media__avg'],2))
            


        print("x"*30)
        print(categories)
        print(inscritos)
        print(participantes)
        print(faltantes)
        print(media_geral)
        print(media)
        

        # chart = {
        #             'container' : 
        #                 {                    
        #                 'title': {
        #                     'text': 'Frequência de alunos de 2017 a 2021',
        #                     'align': 'left'
        #                 },
        #                 'xAxis': 
        #                 {
        #                 'categories': categories
        #                 },
        #                 'yAxis': {
        #                 'title': {
        #                     'text': 'Inscritos'
        #                     }
        #                 },
        #                 'series': [
        #                     {
        #                     'type': 'column',
        #                     'name': 'Inscritos',
        #                     'data': inscritos,
        #                     },          
        #                     {
        #                     'type': 'column',
        #                     'name': 'Partcipantes',
        #                     'data': participantes
        #                     }, 
        #                     'type': 'spline',
        #                     'name': 'Faltas',
        #                     'data': faltantes,
        #                     'marker': {
        #                         'lineWidth': 2,
        #                         'lineColor': Highcharts.getOptions().colors[2],
        #                         'fillColor' : 'white'
        #                     }]
        #                 }          
        #                 }              
                        
                
        # print ("x"*50)
        # print (chart)

#(venv) $ python manage.py test app1.tests 




print(Teste1())