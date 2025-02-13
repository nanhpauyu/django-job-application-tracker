from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

def home(request):
    context = {}
    context['my_title'] = "my graph"
    return render(request, 'home.html',context=context)


def application(request):
    context = dict()
    return render(request=request,template_name='application.html',context= context)

@api_view(['POST'])
def add_post(request):
    post_data = request.data['result']
    print(post_data)
    return Response('good')