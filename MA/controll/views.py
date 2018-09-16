from django.shortcuts import render
from django.http import HttpResponse
import json
import sqlite3

# Create your views here.
def home(request):
	context = locals()
	layout = 'home.html'
	return render(request, layout, context)

def login(request):
	context = locals()
	layout = 'login.html'
	return render(request, layout, context)

def createMeeting(request):
	context = locals()
	layout = 'createMeeting.html'
	return render(request, layout, context)

def history(request):
	context = locals()
	layout = 'history.html'
	return render(request, layout, context)

def register(request):
	context = locals()
	layout = 'register.html'
	return render(request, layout, context)

def script(request):
	context = locals()
	layout = 'script.html'
	return render(request, layout, context)

# def authenticate(request):
# 	response_data = {}
# 	if request.is_ajax() :

# 		if request.method == 'POST':
# 			name = request.POST.get('email')
# 			password = request.POST.get('password')

# 			#result = dbauthenticate(username,password)
# 			sqlite_file = 'db.sqlite3'
# 			conn = sqlite3.connect(sqlite_file)
# 			c = conn.cursor()
# 			c.execute("SELECT name, password FROM controll_client WHERE name='" + name +"' AND password='"+ password+"'")
# 			result = c.fetchone()
# 			c.close()
# 			layout = 'login.html'

# 			if(result) :
# 				request.session['login'] = "success"
# 				response_data['message'] = 'success'
# 	return HttpResponse(json.dumps(response_data), content_type="application/json")
			#return render(request, layout, {'result' : result})
def authenticate(request):

	if request.is_ajax() :
		if request.method == 'POST':
			data = json.loads(request.body.decode('utf-8'))
			print(data)
			email = data["email"]
			password = data["password"]
			sqlite_file = 'db.sqlite3'
			conn = sqlite3.connect(sqlite_file)
			c = conn.cursor()
			c.execute("SELECT name, password FROM controll_client WHERE name='" + email +"' AND password='"+ password+"'")
			result = c.fetchone()
			c.close()
			print(result)
			if(result) :
 				request.session['login'] = "success"
 				response_data['message'] = 'success'
	return HttpResponse(json.dumps(response_data), content_type="application/json")
