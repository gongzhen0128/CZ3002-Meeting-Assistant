from django.contrib import admin

# Register your models here.
from .models import client
from .models import meeting

class clientAdmin(admin.ModelAdmin):
	class Meta:
		model = client

admin.site.register(client,clientAdmin)

class meetingAdmin(admin.ModelAdmin):
	class Meta:
		model = meeting

admin.site.register(meeting,meetingAdmin)