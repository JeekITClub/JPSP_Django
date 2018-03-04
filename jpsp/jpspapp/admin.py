from django.contrib import admin
from .models import Club, Activity, Classroom, Post, UserProfile, ClubMemberShip, ActivityParticipantShip
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'Name', 'Region', 'Date1', 'Date2']


class PostAdmin(admin.ModelAdmin):
    pass


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['UserName', 'Grade', 'Class', 'AttendYear']
    list_filter = ['Grade', 'Class', 'AttendYear']


class UserProfileInline(admin.TabularInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'user_profile'


class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)



class PostInline(admin.TabularInline):
    model = Post
    can_delete = True
    verbose_name_plural = 'post'

    # def get_min_num(self, request, obj=None, **kwargs):
    #     return 2
    #
    # def get_max_num(self, request, obj=None, **kwargs):
    #     return 2
    #
class ClubAdmin(admin.ModelAdmin):
    inlines = (PostInline,)
    list_display = ['ClubName', 'Type']
    list_filter = ['Type']



admin.site.register(Club, ClubAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Classroom)

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(ClubMemberShip)
admin.site.register(ActivityParticipantShip)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)