from django.contrib import admin
from .models import User, Message, Topic, Room
# Register your models here.

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Room)
admin.site.register(Topic)