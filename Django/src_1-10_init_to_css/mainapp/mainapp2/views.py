from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #print(request.user) # print to the console
    #user = request.user
    #return HttpResponse("<h1>Welcome {}!</h1>".format(user))
    #user = request.user
    #context = {
    #    'user': user,
    products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Wastermelons"]
    context = {
        'products': products # products: key, products: value, context is passed into home.html page
    }
    return render(request, "home.html", context) # basic typical response with home.html