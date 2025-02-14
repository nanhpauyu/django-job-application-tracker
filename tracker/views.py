from django.shortcuts import render, redirect, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .customer_decorator import login_required
from .gemini_ai import get_information
from .models import Application
from django.db.models import Count


# Create your views here.
@login_required
def home(request):
    context = {}
    apps = Application.objects.values('start_date').annotate(
        total=Count('id')
    ).order_by('start_date')
    line_date_date = []
    line_date_data = []
    for i in apps:
        line_date_date.append(i['start_date'])
        line_date_data.append(i['total'])
    context['line_date'] = line_date_date
    context['line_data'] = line_date_data
    # bar_location = Application.objects.values('location').annotate(total = Count('id')).order_by('location')
    # print(bar_location)
    bar_location = Application.objects.all()
    temp = {}
    for i in bar_location:
        i_split = i.location.split(',')
        if len(i_split) == 2:
            state = i_split[1].strip()
        else:
            state = i_split[0].strip()
        temp[state] = temp.get(state, 0) + 1
    context['bar_state'] = temp.keys()
    context['bar_value'] = temp.values()
    status = Application.objects.values('status').annotate(
        total=Count('id')).order_by('status')
    temp = []
    for i in status:
        temp.append(i.values())
    temp = list(zip(*temp))
    context['donut_label'] = temp[0]
    context['donut_data'] = temp[1]
    remote = Application.objects.values('remote').annotate(
        total=Count('id')).order_by('remote')
    temp = []
    for i in remote:
        temp.append(i.values())
    temp = list(zip(*temp))
    context['donut_label_remote'] = temp[0]
    context['donut_data_remote'] = temp[1]
    return render(request, 'home.html', context=context)
# Transaction.objects.all().values('actor').annotate(total=Count('actor')).order_by('-total')


@login_required
def applications(request):
    context = dict()
    context['applications'] = Application.objects.all().order_by('-id')

    return render(request=request, template_name='application.html', context=context)


@login_required
def update_status(request, pk):
    print(request.POST['status'])
    app = Application.objects.get(id=pk)
    app.status = request.POST['status']
    app.save()
    return redirect('applications')


@api_view(['POST'])
def add_post(request):
    post_data = request.data['result']
    info = get_information(post_data)
    # print(info)
    try:
        # text_lines = info.splitlines()
        save_db(info)
    except Exception as e:
        print(e)
    return Response('good')


def save_db(context):
    data = []
    data.append(context)
    context = context.splitlines()
    for i in range(10):
        info = context[i].split('=')
        if len(info) == 2:
            data.append(info[1].strip())
            # print(info[1].strip())
            if 'company' in info[0]:
                break
        # data.append(context[i])
    application = Application(text=data[0], title=data[1],
                              location=data[2], remote=data[3],
                              compensation=data[4], company=data[5])
    application.save()


def login(request):
    if 'user' in request.session:
        return redirect('home')
    else:
        if request.method == 'GET':
            return render(request, 'login.html')
        else:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is None:
                content = {'error': True}
                return render(request=request, template_name='login.html', context=content)
            else:
                request.session['user'] = user.username
                return redirect('home')


@login_required
def logout(request):
    try:
        del request.session["user"]
    except KeyError:
        pass
    return redirect('login')
