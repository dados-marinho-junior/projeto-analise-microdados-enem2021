from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

#Controle de versão
version = "Versão 1.0.1"
# @login_required


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


def hc(request):

    data = version
    

    return render(request, 'highcharts.html', 
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
