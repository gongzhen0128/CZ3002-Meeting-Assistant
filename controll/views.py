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
    s = {}
    if request.is_ajax():
        if request.method == 'POST':
            data = json.loads(request.body.decode('utf-8'))
            t = data['type']
            text = data['text']
            if t == 'Topic Summary':
                s['text'] = get_summary(text)
            else:
                s['text'] = """
        A meeting is a gathering of two or more people that has been convened[by whom?] for the purpose of achieving a common goal through verbal interaction, such as sharing information or reaching agreement.[2] Meetings may occur face-to-face or virtually, as mediated by communications technology, such as a telephone conference call, a skyped conference call or a videoconference.One can distinguish a meeting from other gatherings, such as a chance encounter (not convened), a sports game or a concert (verbal interaction is incidental), a party or the company of friends (no common goal is to be achieved) and a demonstration (whose common goal is achieved mainly through the number of demonstrators present, not through verbal interaction).Meeting planners and other meeting professionals may use the term "meeting" to denote an event booked at a hotel, convention center or any other venue dedicated to such gatherings.[2][3] In this sense, the term "meeting" covers a lecture (one presentation), seminar (typically several presentations, small audience, one day), conference (mid-size, one or more days), congress (large, several days), exhibition or trade show (with manned stands being visited by passers-by), workshop (smaller, with active participants), training course, team-building session and kick-off event. Although the Occupational Information Network (O*NET), sponsored by the United States Department of Labor and Employment and Training Administration, identified this occupation as "meeting and convention planner," other titles are more commonly used. These titles include event planner, meeting planner, and meeting manager. In addition, a number of other titles specific to the categories of events produced are used, such as corporate planner and party plannerThe banquet event order (BEO), a standard form used in the hospitality industry to document the requirements of an event as pertinent to the venue,[3] has presented numerous problems to meeting and convention planners due to the increasing complexity and scope of modern events. In response, Convention Industry Council developed the event specifications guide (ESG) that is currently replacing the BEO.[4]Additionally, the Convention Industry Council is spearheading The Accepted Practices Exchange (APEX). By bringing planners and suppliers together to create industry-wide accepted practices and a common terminology, the profession continues to enhance the professionalism of the meetings, conventions and exhibitions industry.
        """
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
