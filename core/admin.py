from django.contrib import admin
from core.models import (ServiceType, Master, Photo, Feedback, Services, Booking,)




class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1




@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)




@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'typename', 'experience')
    list_filter = ('typename',)
    search_fields = ('name', 'experience')
    list_select_related = ('typename',)
    inlines = [PhotoInline]



@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'master', 'typename')
    list_filter = ('typename', 'master')
    search_fields = ('name', 'master__name')
    list_select_related = ('master', 'typename')



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'typename', 'rating', 'role')
    list_filter = ('typename', 'rating')
    search_fields = ('name', 'text')
    list_select_related = ('typename',)




@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'typename', 'money')
    list_filter = ('typename',)
    search_fields = ('name',)
    list_select_related = ('typename',)




@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'service', 'master','date', 'time', 'created_at',)
    list_filter = ('service', 'master', 'date')
    search_fields = ('name', 'phone')
    list_select_related = ('service', 'master')
    date_hierarchy = 'created_at'
