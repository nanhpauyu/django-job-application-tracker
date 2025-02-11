from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):
    context = {}
    context['my_title'] = "my graph"
    return render(request, 'home.html',context=context)


def application(request):
    context = dict()
    return render(request=request,template_name='application.html',context= context)