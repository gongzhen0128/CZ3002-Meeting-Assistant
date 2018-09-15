from django.shortcuts import render
from .models import meeting

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
	user_name = 'zesheng'
	if request.user.is_authenticated:
		user_name = request.user.username
	meeting_list = meeting.objects.filter(user_name=user_name)
	context = {
		'meeting_list': meeting_list,
	}
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