from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import sqlite3

from django.views.decorators.csrf import csrf_exempt

from .models import meeting
from django.contrib import messages
from .models import client, meeting
from controll.forms import ClientRegisterForm
from django.core.paginator import Paginator
from .script_util import *

currentScript = None

# Create your views here.
def home(request):
    context = locals()
    layout = 'home.html'
    return render(request, layout, context)


def login(request):
    context = locals()
    layout = 'login.html'
    return render(request, layout, context)


def logout(request):
    context = locals()
    print(login)
    del request.session['login']
    del request.session['uname']
    print(login)
    layout = 'home.html'
    return render(request, layout, context)


@csrf_exempt
def createMeeting(request):
    if 'login' not in request.session:
        return redirect('home')
    print (request.session['uname'])
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        if 'script' in data:
            old_meeting = meeting.objects.get(sessionid=data['sessionid'])
            old_meeting.script = data['script']
            old_meeting.save()
            return redirect('script/' + data['sessionid'])
        else:
            new_meeting = meeting(sessionid=data['sessionid'], name=data['name'], user_name=request.session['uname'])
            new_meeting.save()
    context = locals()
    layout = 'createMeeting.html'
    return render(request, layout, context)


def history(request):
    if 'login' not in request.session:
        return redirect('home')
    else:
        user_name = request.session['uname']
        meetings = meeting.objects.filter(user_name=user_name)
        paginator = Paginator(meetings, 5)

        page = request.GET.get('page', '1')
        meeting_list = paginator.page(page)

        context = {
            'meeting_list': meeting_list,
        }
        layout = 'history.html'
        return render(request, layout, context)


def register(request):
    context = locals()
    layout = 'register.html'
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! Your account is successfully created!')
            return redirect('login')
        else:
            messages.error(request, 'Sorry, the email is registered.')
            return render(request, layout, {'form': form})
    else:
        form = ClientRegisterForm()
        return render(request, layout, {'form': form})


def script(request, sessionid):
    if 'login' not in request.session:
        return redirect('home')
    else:
        m = meeting.objects.get(sessionid=sessionid)
    context = {
        'meeting':m
    }
    layout = 'script.html'
    return render(request, layout, context)

# @require_POST
@csrf_exempt
def summary(request):
    global currentScript
    s = {}
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            t = data['type']
            text = data['text']
            if t == 'Topic Summary':
                currentScript = text
                s['text'] = get_summary(text)
            else:
                print(currentScript)
                s['text'] = currentScript
    return    HttpResponse(json.dumps(s), content_type='application/json')


def authenticate(request):
    response_data = {}
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            print(data)
            email = data["email"]
            password = data["password"]
            sqlite_file = 'db.sqlite3'
            conn = sqlite3.connect(sqlite_file)
            c = conn.cursor()
            c.execute(
                "SELECT email, nickName, password FROM controll_client WHERE email='" + email + "' AND password='" + password + "'")
            result = c.fetchone()
            c.close()
            print("result: " + str(result))
            if (result):
                request.session['login'] = result[0]
                request.session['uname'] = result[1]
                response_data['message'] = 'success'
    return HttpResponse(json.dumps(response_data), content_type="application/json")
