from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    # return HttpResponse("This is my Homepage (/)")
    context = {'name': 'Michael', 'course': 'Django'}
    return render(request, 'home.html', context)


def about(request):
    # return HttpResponse("This is my about (/about)")
    # context = {'name': 'Michael', 'course': 'Django'}
    return render(request, 'about.html')


def projects(request):
    # return HttpResponse("This is my projects (/projects)")
    return render(request, 'recreation.html')


def contact(request):
    # return HttpResponse("This is my contact (/contact)")
    return render(request, 'contact.html')
