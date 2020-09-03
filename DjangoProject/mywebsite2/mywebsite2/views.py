from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name': 'Alex', 'college': 'MIT'})

def details(request):
    detail = request.GET['yourIntro']
    word01 = detail.count('sakshi')
    total_words = detail.split()

    dictionary ={}
    for word in total_words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return render(request, 'details.html', {'detail' : detail, 'count' : word01, 'total_words' : len(total_words),'dictionary' : dictionary.items})


def about(request):
    loginId = request.GET['username']
    print(loginId)
    pwd = request.GET['pass']
    print(pwd)

    if loginId == 'sakshi' and pwd =='pass':
        return render(request, 'about.html', {'user' : loginId})
    elif loginId == 'sakshi':
        return render(request, 'home.html', {'errormsg' : 'Plz enter valid password'})
    else:
        return render(request, 'home.html', {'errormsg' : 'Plz enter valid credentials'})