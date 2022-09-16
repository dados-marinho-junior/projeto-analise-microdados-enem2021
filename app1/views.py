from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


## @login_required
def index(request):

    data = "Versao 0.01"

    return render(request, 'index.html', 
        { 'dados' : data } 
    )

#@login_required
def db1(request):

    data = "Versao 0.01"

    return render(request, 'dashboard1.html', 
        { 'dados' : data } 
    )    

#@login_required
def db2(request):

    data = "Versao 0.01"
    

    return render(request, 'dashboard2.html', 
        { 'dados' : data } 
    )

#@login_required
def db3(request):

    data = "Versao 0.01"
    

    return render(request, 'dashboard3.html', 
        { 'dados' : data } 
    )

#@login_required
def db4(request):

    data = "Versao 0.01"
    

    return render(request, 'dashboard4.html', 
        { 'dados' : data } 
    )

#@login_required
def hc(request):

    data = "Versao 0.01"
    

    return render(request, 'highcharts.html', 
        { 'dados' : data } 
    )

#@login_required
def about(request):

    data = "Versao 0.01"
    

    return render(request, 'sobre.html', 
        { 'dados' : data } 
    )          
