from secrets import choice
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

#Controle de versão
version = "Versão 1.1.2"
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
    Anos = list(TagDis.objects.order_by(
        'data').values_list('data', flat=True).distinct())

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
        MediaGeral = TagDis.objects.filter(
            data=ano).aggregate(Avg('media_geral'))
        Media = TagDis.objects.filter(data=ano).aggregate(Avg('media'))

        # print("Inscritos.......:", Inscritos)
        # print("Participantes...:", Participantes)
        # print("Faltantes.......:", Faltantes)
        # print("Media Geral.....:", MediaGeral)
        # print("Media...........:", Media)

        inscritos.append(Inscritos['inscritos__sum'])
        participantes.append(Participantes['participantes__sum'])
        faltantes.append(Faltantes['faltantes__sum'])
        media_geral.append(round(MediaGeral['media_geral__avg'], 2))
        media.append(round(Media['media__avg'], 2))

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
