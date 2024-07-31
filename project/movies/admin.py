from django.contrib import admin
from . models import Movieinfo,Indistry,Actor,Awards,Director,Genre

# Register your models here.
admin.site.register(Movieinfo)
admin.site.register(Indistry)
admin.site.register(Actor)
admin.site.register(Awards)
admin.site.register(Director)
admin.site.register(Genre)
