from secrets import choice
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

#Controle de versão
version = "Versão 2.0.0"
# @login_required

## imports to Dict to Highcharts
from .models import TagDis
from django.db.models import Avg, aggregates, Sum


def index(request):

    data = version

    return render(request, 'index.html',
                  {'dados': data}
                  )

# @login_required


def db1(request):

    data = version

    return render(request, 'dashboard1.html',
                  {'dados': data}
                  )

# @login_required


def db2(request):

    data = version

    return render(request, 'dashboard2.html',
                  {'dados': data}
                  )

# @login_required


def db3(request):

    data = version

    return render(request, 'dashboard3.html',
                  {'dados': data}
                  )

# @login_required


def db4(request):

    data = version

    return render(request, 'dashboard4.html',
                  {'dados': data}
                  )

# @login_required


def faq(request):

    data = version
    

    return render(request, 'faq.html', 
        { 'dados' : data } 
    )



#def hc(request):

 #   data = "Versao 0.01"
    
    #tagdis = TagDis.objects.all()

    #import json
    #tagdis_json = json.dumps(tagdis)


#     SELECT 
# DATA AS Ano,
# SUM(INSCRITOS) AS Inscritos,
# SUM(PARTICIPANTES) AS Participantes,
# SUM(FALTANTES) AS Faltas,
# ROUND(AVG(MEDIA_GERAL),2 ) AS Media_Inscritos,
# ROUND(AVG(MEDIA),2 ) AS Media_Participantes,
# FROM 'base aqui' 
# GROUP BY DATA ORDER BY DATA ASC


    #return render(request, 'highcharts.html', 
       # { 'dados' : data, 'tagdis' : tagdis_json } 
    #)

def about(request):

    data = version

    return render(request, 'sobre.html',
                  {'dados': data}
                  )


#  salvar aqui
def DadosHicharts(choice):

        ''' 

        Para esta view existe um tests.py verifique.
        Utilize o comando abaixo para testar:
            (venv) $ python manage.py test app1.tests

        '''

        Anos = list(TagDis.objects.order_by(
            'data').values_list('data', flat=True).distinct())

        Ufs = list(TagDis.objects.order_by(
            'uf').values_list('uf', flat=True).distinct())

        # print("Anos............:", Anos)

        categories = []
        inscritos = []
        participantes = []
        faltantes = []
        media_geral = []
        media = []


        for ano in Anos:
            # print(f'Ano.............: {ano}')
            

            categories.append(ano)

            Inscritos = TagDis.objects.filter(
                data=ano).aggregate(Sum('inscritos'))
            Participantes = TagDis.objects.filter(
                data=ano).aggregate(Sum('participantes'))
            Faltantes = TagDis.objects.filter(
                data=ano).aggregate(Sum('faltantes'))

            MediaGeral_UF = 0 
            Media_UF = 0 
            for uf in Ufs:
                #print (f'Uf..........: {uf}')
                tagAno = TagDis.objects.filter(data=ano)
                Participantes_UF = tagAno.filter(uf=uf).aggregate(Sum('participantes'))
                Inscritos_UF = tagAno.filter(uf=uf).aggregate(Sum('inscritos'))

                soma_media_uf = tagAno.filter(uf=uf).aggregate(Sum('media_geral'))

                MediaGeral_UF = MediaGeral_UF + ( 
                                                (sum(Participantes_UF[x] for x in Participantes_UF)) * 
                                                (sum(soma_media_uf[x] for x in soma_media_uf))
                                                )
                    
                
                soma_media_uf = tagAno.filter(uf=uf).aggregate(Sum('media'))

                Media_UF      = Media_UF + (
                                            (sum(Inscritos_UF[x] for x in Inscritos_UF)) * 
                                            (sum(soma_media_uf[x] for x in soma_media_uf))
                                            )

            # print(type(MediaGeral_UF))
            # print(type(Participantes))
            # print(type(Media_UF))   
            # print(type(Inscritos))

            MediaGeral = (MediaGeral_UF / (sum(Participantes[x] for x in Participantes)))
            Media = (Media_UF/ (sum(Inscritos[x] for x in Inscritos)))

            # print("Inscritos.......:", Inscritos)
            # print("Participantes...:", Participantes)
            # print("Faltantes.......:", Faltantes)
            # print("Media Geral.....:", MediaGeral)
            # print("Media...........:", Media)

            inscritos.append(Inscritos['inscritos__sum'])
            participantes.append(Participantes['participantes__sum'])
            faltantes.append(Faltantes['faltantes__sum'])
            media_geral.append(round(MediaGeral, 2))
            media.append(round(Media, 2))

        # print("x"*30)
        # print(categories)
        # print(inscritos)
        # print(participantes)
        # print(faltantes)
        # print(media_geral)
        # print(media)


        chart1 = {             
            'title': {
                'text': 'Frequência de alunos de 2017 a 2021',
                'align': 'left'},
            
            'xAxis':
            {
            'categories': categories
            },
            'yAxis': {
                'title': {
                    'text': 'Inscritos'
                }
            },
            'series': [
                {
                'type': 'column',
                'name': 'Inscritos',
                'data': inscritos,
                },
                {
                'type': 'column',
                'name': 'Partcipantes',
                'data': participantes
                },
                {
                'type': 'spline',
                'name': 'Faltantes',
                'data': faltantes,
                'marker': {
                    'lineWidth': 2,
                    'lineColor': 'green',
                    'fillColor': 'white'
                }
                }]
            }
           
    

        chart2 = {
                    'title': {
                        'text': 'Média Inscritos x Média Participantes de 2017 a 2021',
                        'align': 'left'},
                    
                    'xAxis':
                    {
                    'categories': categories
                    },
                    'yAxis': {
                        'title': {
                            'text': 'Médias'
                        }
                    },
                    'series': [
                        {
                        'type': 'column',
                        'name': 'Média Inscritos',
                        'data':media_geral,
                        },
                        {
                        'type': 'column',
                        'name': 'Média Participantes',
                        'data': media
                        },                       
                        ]

                    }
        if choice == 1:
            return chart1
        if choice == 2:
            return chart2                     
                           



def hc(request):
    data = version

    high1 = DadosHicharts(1)
    high2 = DadosHicharts(2)  
       
    # return (request,data)

    return render(request, 'highcharts.html', 
        { 'charts1' : high1,
         'charts2' : high2,
          'dados' : data  }      
    )
