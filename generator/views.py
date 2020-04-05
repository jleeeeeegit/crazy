from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.


def home(request):
    #return  HttpResponse('Hello there friend')

    # instead use the file home.html inside of the templates/generator
    #return render(request, 'generator/home.html',{'password':'jl0112'})

    return render(request, 'generator/home.html')



def password(request):



    characters = list('abdsadfdsafsafsadfdsaf')
    #length = 10
    #following 'length is from home.html <select name = 'lenth'> '

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('@&%$!*^'))

    if request.GET.get('numbers'):
       characters.extend(list('0123456789'))


    length = int(request.GET.get('length',12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html', {'password':thepassword})


def about(request):

    return render(request, 'generator/about.html')



def subscribe(request):

    return render(request, 'generator/subscribe.html')
