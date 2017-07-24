from django.contrib import admin
from .models import Club, Activity, Classroom, Token, Post, UserProfile


# Register your models here.
class ClubAdmin(admin.ModelAdmin):
    list_display = ('Type')


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('Region', 'Date1', 'Date2')


class PostAdmin(admin.ModelAdmin):
    #
    pass


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('Grade', 'Class', 'AttendYear')


admin.site.register(Club, ClubAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Classroom)
admin.site.register(Token)
admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
