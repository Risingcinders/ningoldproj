from django.shortcuts import render, HttpResponse, redirect
import random


def index(request):
    console = ""
    if 'treats' in request.session:
        request.session['counter'] += 1
    else:
        request.session['treats'] = 0
        request.session['counter'] = 0
        request.session['console'] = ""
    context = {
        'treats': request.session['treats'],
        'count': request.session['counter'],
        'console': request.session['console']
    }
    return render(request, "index.html", context)


def money(request):
    new_treats = 0
    location = request.POST['location']
    if location == "rich":
        # del request.session['target']
        new_treats = random.randrange(30, 50)
    elif location == "witch":
        new_treats = random.randrange(-50, 100)
    elif location == "couch":
        new_treats = random.randrange(0, 2)
    elif location == "forest":
        new_treats = random.randrange(5, 10)
    request.session['console'] += f"\nYou visited the {location} and found {new_treats} treats."
    request.session['treats'] += new_treats
    return redirect('/')

def kill(request):
    del request.session['treats']
    return redirect('/')