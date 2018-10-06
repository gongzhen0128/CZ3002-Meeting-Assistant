from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
import sqlite3
from .models import meeting
from django.contrib import messages
from .models import client, meeting
from controll.forms import ClientRegisterForm
from django.core.paginator import Paginator

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

def createMeeting(request):
	if 'login' not in request.session:
		return redirect('home')
	else:
		context = locals()
		layout = 'createMeeting.html'
		return render(request, layout, context)

def history(request):
	if 'login' not in request.session:
		return redirect('home')
	else:
		context = locals()
		user_name = 'zesheng'
		if request.user.is_authenticated:
			user_name = request.user.username
		# meetings = meeting.objects.filter(user_name=user_name)
		meetings = meeting.objects.all()
		paginator = Paginator(meetings, 1)

		page = request.GET.get('page','1')
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

def script(request):
	if 'login' not in request.session:
		return redirect('home')
	else:
		context = locals()
		layout = 'script.html'
		return render(request, layout, context)

def authenticate(request):
	response_data = {}
	if request.is_ajax() :
		if request.method == 'POST':
			data = json.loads(request.body.decode('utf-8'))
			print(data)
			email = data["email"]
			password = data["password"]
			sqlite_file = 'db.sqlite3'
			conn = sqlite3.connect(sqlite_file)
			c = conn.cursor()
			c.execute("SELECT email, nickName, password FROM controll_client WHERE email='" + email +"' AND password='"+ password+"'")
			result = c.fetchone()
			c.close()
			print("result: "+str(result))
			if(result) :
 				request.session['login'] = result[0]
 				request.session['uname'] = result[1]
 				response_data['message'] = 'success'
	return HttpResponse(json.dumps(response_data), content_type="application/json")
