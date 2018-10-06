"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from controll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='open'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),

    path('createMeeting/', views.createMeeting, name='createMeeting'),
    path('history/', views.history, name='history'),
    path('register/', views.register, name='register'),
    path('script/', views.script, name='script'),
    path('logout/', views.logout, name='logout'),
    #login url function
    path('login/authenticate', views.authenticate, name='authenticate'),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
