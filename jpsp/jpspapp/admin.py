from django.contrib import admin
from .models import Club, Activity, Classroom, Token, Message, Post, UserProfile, Cevent

# Register your models here.
class CeventAdmin(admin.ModelAdmin):
    list_display = ('cusername','datetime1','datetime2','ctype','content')


admin.site.register(Club)
admin.site.register(Activity)
admin.site.register(Classroom)
admin.site.register(Token)
admin.site.register(Message)
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Cevent,CeventAdmin)
