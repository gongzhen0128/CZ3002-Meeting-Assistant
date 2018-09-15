from django.shortcuts import render

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